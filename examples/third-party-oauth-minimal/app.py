"""Minimal WorkBuddy OAuth 2.1 server-side demo.

Reference only. Tokens are stored in process memory and disappear on restart.
Do not use this storage model in production.
"""

from __future__ import annotations
import os
import secrets
from urllib.parse import urlencode

import requests
from flask import Flask, abort, jsonify, redirect, request, session

AUTHORIZE_URL="https://www.workbuddy.cn/openapi/v2/authorize"
TOKEN_URL="https://www.workbuddy.cn/openapi/v2/token"
PROFILE_URL="https://www.workbuddy.cn/openapi/v2/user/profile"

CLIENT_ID=os.environ["WORKBUDDY_CLIENT_ID"]
CLIENT_SECRET=os.environ["WORKBUDDY_CLIENT_SECRET"]
REDIRECT_URI=os.environ["WORKBUDDY_REDIRECT_URI"]
SCOPE=os.environ.get("WORKBUDDY_SCOPE","user.profile.readable")

app=Flask(__name__)
app.secret_key=os.environ["FLASK_SECRET_KEY"]
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

# Demo-only server-side memory store. Replace with an encrypted persistent store.
TOKEN_STORE={}

def session_key():
    key=session.get("demo_key")
    if not key:
        key=secrets.token_urlsafe(24)
        session["demo_key"]=key
    return key

def token_request(form):
    r=requests.post(
        TOKEN_URL,
        data=form,
        headers={"Accept":"application/json"},
        timeout=20,
    )
    r.raise_for_status()
    return r.json()

@app.get("/")
def index():
    return {
        "demo":"WorkBuddy OAuth 2.1 minimal reference",
        "login":"/login",
        "profile":"/profile",
        "refresh":"/refresh",
    }

@app.get("/login")
def login():
    state=secrets.token_urlsafe(32)
    session["oauth_state"]=state
    params={
        "response_type":"code",
        "client_id":CLIENT_ID,
        "redirect_uri":REDIRECT_URI,
        "scope":SCOPE,
        "state":state,
    }
    return redirect(AUTHORIZE_URL+"?"+urlencode(params))

@app.get("/callback")
def callback():
    expected=session.pop("oauth_state",None)
    received=request.args.get("state")
    if not expected or not received or not secrets.compare_digest(expected,received):
        abort(400,"OAuth state mismatch")

    code=request.args.get("code")
    if not code:
        abort(400,"missing authorization code")

    token=token_request({
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":REDIRECT_URI,
        "client_id":CLIENT_ID,
        "client_secret":CLIENT_SECRET,
    })
    TOKEN_STORE[session_key()]=token

    # Never return access_token / refresh_token to the browser in a real app.
    return jsonify({
        "authorized":True,
        "token_type":token.get("token_type"),
        "expires_in":token.get("expires_in"),
        "scope":token.get("scope"),
        "open_id":token.get("open_id"),
    })

@app.get("/profile")
def profile():
    token=TOKEN_STORE.get(session_key())
    if not token:
        return redirect("/login")
    access=token.get("access_token")
    if not access:
        abort(401,"missing access token")
    r=requests.get(
        PROFILE_URL,
        headers={"Authorization":f"Bearer {access}","Accept":"application/json"},
        timeout=20,
    )
    if r.status_code==401:
        return jsonify({"error":"access_token expired; call /refresh"}),401
    r.raise_for_status()
    return jsonify(r.json())

@app.get("/refresh")
def refresh():
    current=TOKEN_STORE.get(session_key())
    if not current or not current.get("refresh_token"):
        return redirect("/login")

    token=token_request({
        "grant_type":"refresh_token",
        "refresh_token":current["refresh_token"],
        "client_id":CLIENT_ID,
        "client_secret":CLIENT_SECRET,
    })
    TOKEN_STORE[session_key()]=token
    return jsonify({
        "refreshed":True,
        "token_type":token.get("token_type"),
        "expires_in":token.get("expires_in"),
        "scope":token.get("scope"),
        "open_id":token.get("open_id"),
    })

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=False)
