import mysql.connector
from mysql.connector import connect, Error


def db(sqlquery):
    myhost = 'localhost'
    mydatabase = 'health_insurance_company'
    myuser = 'root'
    mypass = 'root'
    try:
        con = connect(host = myhost,
                      database = mydatabase,
                      user = myuser,
                      password = mypass)
    except:
        print(Error)
    cur = con.cursor()

    try:
        cur.execute(sqlquery)
    except:
        print("Eception",Error)

    try:
        user = cur.fetchone()
    except:
        print("Eception",Error)


    con.commit()
    con.close()
    try:
        return user
    except:
        pass



def dsp(sqlquery):
    myhost = 'localhost'
    mydatabase = 'health_insurance_company'
    myuser = 'root'
    mypass = 'root'
    try:
        con = connect(host = myhost,
                      database = mydatabase,
                      user = myuser,
                      password = mypass)
    except:
        print(Error)
    cur = con.cursor()

    try:
        cur.execute(sqlquery)
    except:
        print("Eception",Error)

    try:
        user = cur.fetchall()
    except:
        print("Eception",Error)


    con.commit()
    con.close()
    try:
        return user
    except:
        pass


# def inset(sqlquery):
#     myhost = 'localhost'
#     mydatabase = 'health_insurance_company'
#     myuser = 'root'
#     mypass = 'root'
#
#
#     con = connect(host = myhost,
#                       database = mydatabase,
#                       user = myuser,
#                       password = mypass)
#     cur = con.cursor()
#
#     cur.execute(sqlquery)
#
#     con.commit()
#     con.close()
