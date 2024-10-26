import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime
import pytz

api_key = "api_key"

def fetch():
    return