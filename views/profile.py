from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *
profile = Blueprint("profile",__name__)

@profile.route('/profile', methods=["GET", "POST"])

def Profile():
    data1 = dsp(f"SELECT * FROM relationship;")
    # print (data1)

    if request.form.get('ADD') == 'ADD':
        Did = request.form.get('Did')
        DName = request.form.get('DName')
        DateOfBirth = request.form.get('DateOfBirth')
        Address = request.form.get('Address')
        Cid=session['Cid']
        RelID = request.form.get('Rel')
        print(Did)
        print(DName)
        print(DateOfBirth)
        print(Address)
        print(Cid)
        db(f"INSERT INTO dependents (Did,DName,RelID,DateOfBirth,Address,Cid) VALUES ('{Did}','{DName}',{RelID},'{DateOfBirth}','{Address}','{Cid}');")
        return redirect('/profile')
    return render_template("profile.html",data1=data1)

