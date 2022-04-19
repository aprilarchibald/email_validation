from flask import Flask
app = Flask(__name__)
app.secret_key = "security"



from flask_app.controller import controller