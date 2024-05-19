from flask import render_template , Blueprint, request, redirect, url_for , session
import mysql.connector
from mysql.connector import connect, Error
from views.__init import *

plan = Blueprint("plan",__name__)

@plan.route('/plan' , methods=["GET","POST"])
def buyplan():
    # data = dsp(f"(SELECT Cid AS UserID,concat(FName, LName) AS Username FROM customer where cid = '{session['Cid']}') UNION (SELECT Did ,DName FROM dependents where cid = '{session['Cid']}');")
    data=dsp(f"(SELECT Cid AS UserID,concat(FName, LName, ' (Me)') AS Username,PlanID FROM customer where cid = '{session['Cid']}'  AND PlanID is null) UNION (SELECT Did ,DName,PlanID FROM dependents where cid = '{session['Cid']}' AND PlanID is null);")
    # print(data)

    if request.form.get('choose')=="choose" :
        db(f"insert into plan(Cid , typeid) values ('{session['Cid']}',{session ['p']});")
        var=dsp(f"SELECT PlanID FROM plan WHERE Cid = '{session['Cid']}' ORDER BY PlanID DESC;")

        variable = request.form.getlist('dep')
        for i in variable:
            if i == session['Cid']:
                db(f"update customer set planID = {var[0][0]} where Cid = '{i}';")
            else:
                db(f"update dependents set planID = {var[0][0]} where Did = '{i}';")




        return redirect('/')

    return render_template("plan.html" , data=data)
