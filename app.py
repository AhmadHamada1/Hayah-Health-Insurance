from flask import Flask, render_template , Blueprint, request, redirect, url_for,session
import mysql.connector
from mysql.connector import connect, Error
from views.__init import *


from views.home import home
from views.register import register
from views.login import login_blueprint
from views.profile import profile
from views.add_dependent import add_dependent
from views.plan import plan
from views.admin import admin
from views.claims import claims
from views.file_claim import file_claim
from views.file_claim2 import file_claim2
from views.view_claim import view_claim

app = Flask (__name__)
app.register_blueprint(view_claim)
app.register_blueprint(file_claim2)
app.register_blueprint(file_claim)
app.register_blueprint(claims)
app.register_blueprint(admin)
app.register_blueprint(login_blueprint)
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(plan)
app.register_blueprint(register)
app.register_blueprint(add_dependent)
app.secret_key = "^A%DJAJU^JJ123"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ =="__main__" :

    app.run(debug =True,port=8000)
    