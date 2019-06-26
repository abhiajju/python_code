#!/usr/bin/python
# coding: latin-1

from flask import Flask, redirect, url_for,request, render_template
import commands,mysql.connector

app = Flask(__name__)
'''
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="abhi",
	database="cloud"  
)

mycursor = mydb.cursor()
'''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/trying')
def abcd(lnk='abcd'):
	return render_template('index1.html',res=lnk)


@app.route('/nafis',methods = ['POST', 'GET'])
def login():
    print request.method
    print request.form
    if request.method == 'POST':
        user = request.form['username']
	passwd = request.form['password']
	sql = "SELECT * FROM users WHERE name = %s and passwd = %s"
	val = (user,passwd)
	mycursor.execute(sql,val)
	myresult = mycursor.fetchall()
	if len(myresult)==0:
		return render_template('extra.html',result=user,passw=passwd)

if __name__ == '__main__':
	app.run(port=5000)
