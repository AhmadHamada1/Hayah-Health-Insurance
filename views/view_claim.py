from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

view_claim = Blueprint("view_claim",__name__)

@view_claim.route('/view_claim', methods=["GET", "POST"])
def ViewClaim ():
    claim_id=request.args.get("claim_id")
    print(claim_id)

    info = dsp(f"select * from claim where claimid={claim_id};")[0]
    print(info)
    print(info[8])
    hospital=dsp(f"select hname from hospital where hid={info[8]};")[0][0]
    print(hospital)

    if request.form.get("Close")=="Close":
        return redirect('/admin')
    if request.form.get("Check As Resolved")=="Check As Resolved":
        db(f"update claim set resolved = 1 where claimid={claim_id}")
        return redirect('/admin')

    return render_template("view_claim.html",info=info, hospital=hospital)