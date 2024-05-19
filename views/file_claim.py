from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

file_claim = Blueprint("file_claim",__name__)

@file_claim.route('/file_claim', methods=["GET", "POST"])
def FileClaim ():
    data1=dsp(f"Select * from ((SELECT Cid AS UserID,concat(FName, ' ', LName) AS Username,PlanID FROM customer where cid = '{session['Cid']}'  AND PlanID is not null) UNION (SELECT Did ,DName,PlanID FROM dependents where cid = '{session['Cid']}' AND PlanID is not null)) AS Clients,plan where Clients.PlanID = plan.PlanID ; ")
    # print(data1)
    if request.form.get('chk_hospital') == "Check Available Hospitals":
        for i in data1:
            if request.form.get("benf")==i[0]:
                session["mylist"]=i
                return redirect(f'/file_claim2')


    return render_template("file_claim.html",data1=data1)