# adding new  customer
from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

register = Blueprint("register",__name__)

@register.route('/register', methods=["GET", "POST"])
def Register():

    if request.form.get('submit') == 'submit':
        Cid = request.form.get('Cid')
        FName = request.form.get('FName')
        LName = request.form.get('LName')
        Address =  request.form.get('Address')
        DateOfBirth = request.form.get('DateOfBirth')
        E_mail = request.form.get('E_mail')
        Password = request.form.get('Password')
        print(Cid)
        print(FName)
        print(LName)


        db(f"INSERT INTO customer (Cid, FName,LName,DateOfBirth,Address,E_mail ,Password) VALUES ('{Cid}','{FName}','{LName}','{DateOfBirth}','{Address}','{E_mail}','{Password}');")

        session['Cid'] = request.form['Cid']
        # session['name'] = request.form['name']
        # session['email'] = request.form['email']
        return redirect('/')
    return render_template("register.html")



