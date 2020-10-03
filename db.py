from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fq2azxj9zx0r1yqw:ms26mvut3rse9ah7@d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/y36a2emvyntb2g3g'

db = SQLAlchemy(app)