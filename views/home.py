from flask import render_template , Blueprint, request, redirect, url_for , session
import mysql.connector
from mysql.connector import connect, Error
from views.__init import *

home = Blueprint("home",__name__)

@home.route('/' , methods=["GET", "POST"])
def Home():
    basic = dsp(f"SELECT * FROM hospital,enrolled Where TypeID = 1 AND hospital.Hid = enrolled.Hid;")
    premium = dsp(f"SELECT * FROM hospital,enrolled Where TypeID = 2 AND hospital.Hid = enrolled.Hid;")
    golden = dsp(f"SELECT * FROM hospital,enrolled Where TypeID = 3 AND hospital.Hid = enrolled.Hid;")

    if request.form.get('buybasic'):
        try:
            if session['Cid']:
                session['p'] = 1
                return redirect(f'/plan')
        except:
            return redirect('/login')


    if request.form.get('buypremium'):
        try:
            if session['Cid']:
                session['p'] = 2
                return redirect(f'/plan')
        except:
            return redirect('/login')

    if request.form.get('buygold'):
        try:
            if session['Cid']:
                session['p'] = 3

                return redirect(f'/plan')
        except:
            return redirect('/login')

    return render_template("home.html", basic=basic, premium=premium, golden=golden)


