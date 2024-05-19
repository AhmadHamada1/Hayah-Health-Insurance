from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

add_dependent = Blueprint("add_dependent" ,__name__ )
@add_dependent.route('/add_dependent' , methods=['GET','POST'])

def addDependent():
    if request.form.get('add') == 'add':
        Did = request.form.get('Did')
        DName = request.form.get('DName')
        DateOfBirth = request.form.get('DateOfBirth')
        Address = request.form.get('Address')
        Cid=session['Cid']
        print(Did)
        print(DName)
        print(DateOfBirth)
        print(Address)
        print(Cid)
        db(f"INSERT INTO dependents (Did,DName,DateOfBirth,Address,Cid) VALUES ('{Did}','{DName}','{DateOfBirth}','{Address}','{Cid}');")
        return redirect('/profile')
    return render_template("profile.html")

