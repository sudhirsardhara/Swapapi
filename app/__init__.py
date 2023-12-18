# app/__init__.py

from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Initialize caching
cache = Cache(app)

# Initialize database
db = SQLAlchemy(app)

# Import routes
from app import routes