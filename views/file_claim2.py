from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from datetime import date, datetime
from views.__init import *

file_claim2 = Blueprint("file_claim2",__name__)

@file_claim2.route('/file_claim2', methods=["GET", "POST"])
def FileClaim2 ():
    # print(session["mylist"])
    # print(session["mylist"][0])

    data2=dsp(f"Select * from hospital,enrolled where hospital.Hid = enrolled.Hid AND TypeID = {session['mylist'][5]};")

    if request.form.get("submit claim")=="submit claim" :

        details=request.form.get("Details")
        # print(details)
        cost = request.form.get("cost")
        # print(cost)
        hid=request.form.get("hospital")
        # print(hid)
        today = date.today()

        date1 = today.strftime("%d/%m/%Y")
        # print(date1)
        db(f"INSERT INTO claim(Cost, Details, Date, BenificiaryID, PlanID, Cid, Hid) VALUES ({cost},'{details}','{date1}','{session['mylist'][0]}',{session['mylist'][2]},'{session['Cid']}',{hid});")
        return redirect('/')

    return render_template("file_claim2.html",data2=data2)