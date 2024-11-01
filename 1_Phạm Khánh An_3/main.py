#a
from asyncio import timeout
from importlib.metadata import files

from flask import Flask, request,jsonify
import sqlite3,json
#Create a flask app
app=Flask(__name__)
dbname="db/ShoppingDB.db"

@app.route("/")
def Index():
    return "1_Phạm Khánh An_3"
@app.route("/Supplier",methods=["GET"])
def get_Supplier():
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM Supplier")
    conn.commit()
    suppliers=cur.fetchall()
    supplier_list=[]
    for supplier in suppliers:
        supplier_list.append({"SupplierId":supplier[0],"SupplierName":supplier[1],"EmailAddress":supplier[2],"Password":supplier[3],
                              "Tel":supplier[4],"TotalEmployee":supplier[5]
                              })
    return jsonify(supplier_list)
@app.route("/Supplier",methods=["DELETE"])
def delete_Supplier():
    id = request.json.get("id")
    conn = sqlite3.connect(dbname,timeout=200)
    cur = conn.cursor()
    cur.execute("DELETE FROM Supplier WHERE SupplierID=?",(id,))
    conn.commit()
    #check if supplier exist
    if cur.rowcount >0:
        return jsonify({"message":"supplier deteted successfully"})
    else:
        return "Supplier not found"
@app.route("/Supplier",methods=["POST"])
def add_Supplier():
    conn = sqlite3.connect(dbname,timeout=200)
    cur = conn.cursor()
    suppplier_ID=request.json.get("ID")
    supplier_name=request.json.get("name")
    supplier_email=request.json.get("email")
    supplier_pass=request.json.get("pass")
    supplier_Tel = request.json.get("tel")
    supplier_TotalE = request.json.get("totalE")
    if (suppplier_ID and supplier_email and supplier_pass):
        #insert supplier into database
        cur.execute("INSERT INTO Supplier (SupplierID,SupplierName, EmailAddress, Password, Tel, TotalEmployee)"
                    "values (?,?,?,?,?,?)",(suppplier_ID,supplier_name,supplier_email,supplier_pass,supplier_Tel,supplier_TotalE))
        conn.commit()
        #get the id of the inserted supplier
        suppplier_id=cur.lastrowid
        return jsonify(suppplier_id)
    else:
        return "data required"
@app.route('/Supplier', methods=["PUT"])
def update_Supplier():
    conn = sqlite3.connect(dbname, timeout=200)
    cur = conn.cursor()
    suppplier_ID = request.json.get("ID")
    supplier_name = request.json.get("name")
    supplier_email = request.json.get("email")
    supplier_pass = request.json.get("pass")
    supplier_Tel = request.json.get("tel")
    supplier_TotalE = request.json.get("totalE")
    if
if __name__=="__main__":
    app.run(debug=True,port=5000)