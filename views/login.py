from flask import render_template, Blueprint, request, redirect, url_for, session,flash
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *


login_blueprint = Blueprint('login',__name__)
@login_blueprint.route('/login', methods=["GET", "POST"])

def login():

     if request.form.get('login') == 'login':
        E_mail= request.form.get('E_mail')
        Password= request.form.get('Password')
        user1 = db(f"SELECT * FROM customer where E_Mail = '{E_mail}'")

        try:
            if len(user1) > 0:
                if Password == user1[7] :
                    session['Cid'] = user1[0]
                    session['Roleid']=user1[8]
                else:
                    return "Error password and email not match"
        except:
            return 'erorr'
        if session['Roleid']==1 :
            return redirect('/')
        elif session["Roleid"]==2:
            return redirect('/admin')
     return render_template("login.html")




