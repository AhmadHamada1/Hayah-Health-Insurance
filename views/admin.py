from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

admin = Blueprint("admin",__name__)

@admin.route('/admin', methods=["GET", "POST"])
def Register():
    plantype = dsp(f"SELECT TypeID,TypeName FROM plantype;")
    customers=dsp(f"select Cid, Fname,Lname from customer;")
    all = dsp(f"(SELECT claimID ,CONCAT(customer.FName, ' ', customer.LName) AS CName, customer.CID, Resolved FROM claim,customer WHERE BenificiaryID = customer.Cid) UNION (SELECT claimID ,DName, Did, Resolved FROM claim,dependents WHERE BenificiaryID = Did);")
    all2 = dsp(f"(SELECT claimID ,CONCAT(customer.FName, ' ', customer.LName) AS CName, customer.CID, Resolved FROM claim,customer WHERE BenificiaryID = customer.Cid and resolved=0) UNION (SELECT claimID ,DName, Did, Resolved FROM claim,dependents WHERE BenificiaryID = Did and resolved=0);")

    print(customers)
    print(all)
    print(all2)

    if request.form.get('ADD') == 'ADD':
        name=request.form.get('name')
        phonenum=request.form.get('phonenum')
        location=request.form.get('location')
        db(f"INSERT INTO hospital(Hname,PhoneNo) Values('{name}','{phonenum}')")
        db(f"INSERT INTO hospital_location VALUES ('{location}',(SELECT Hid FROM hospital ORDER BY Hid DESC LIMIT 1))")
        variable = request.form.getlist('plantype')
        print(variable)
        for i in variable:
            db(f"INSERT INTO enrolled VALUES ({i},(SELECT Hid FROM hospital ORDER BY Hid DESC LIMIT 1))")
        return redirect('/admin')
    for i in all :
        print(i[0])
        if request.form.get("ViewClaim")==f"view {i[0]}" :
            print(i[0])
            return redirect(f'/view_claim?claim_id={i[0]}')



    return render_template("admin.html", plantype=plantype,customers=customers,all=all,all2=all2)

