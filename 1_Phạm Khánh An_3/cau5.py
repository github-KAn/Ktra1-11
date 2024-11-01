from flask import Flask, request, jsonify, render_template,redirect,flash
import requests
import sqlite3,json
#Create a flask app
app=Flask(__name__)
dbname="db/ShoppingDB.db"
base_url="http://127.0.0.1:5000/Supplier"
#define a route
@app.route("/")
def index():
    response=requests.get(base_url)
    #check if the response is successful
    if response.status_code==200:
        #Parse the response as a json object
        suppliers=response.json()
        #return render template
        # return suppliers
        return render_template("suppliers.html",suppliers=suppliers)
    else:
        flash("something went wrong please try again later")
    return render_template("suppliers.html")
if __name__=="__main__":
    app.run(debug=True,port=5001)