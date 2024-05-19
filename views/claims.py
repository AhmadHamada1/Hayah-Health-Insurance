from flask import render_template, Blueprint, request, redirect, url_for, session
import mysql.connector
from mysql.connector import connect, Error
import numpy as np
from views.__init import *

claims = Blueprint("claims",__name__)

@claims.route('/claims', methods=["GET", "POST"])
def Claims ():
    var1 = request.args.get('var1')
    return render_template("claims.html",var1=var1)