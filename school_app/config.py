import os


class Config:
    SECRET_KEY = '3ea982a71d379d837581fda1bf6ecee4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "dilshaat@gmail.com"#os.environ.get('EMAIL_USER')
    MAIL_email = "stadtjena3641"#os.environ.get('EMAIL_PASS')