import os

class Config:
    SECRET_KEY = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/IrisMar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    