import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from openai import OpenAI

client = OpenAI (
    api_key = os.getenv('chat_api_key')
)

from datetime import datetime
import pytz



def fetch():
    return