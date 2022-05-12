# import sys
# sys.path.insert(0,"..")

import json
import requests 
from App import app
from flask import Flask, render_template, request, redirect, url_for, flash
from Model.EmpresaItemModel import *
from ApiResConfig import *



 
@app.route('/Empresa')
def Index():
    data = requests.get(Api+'GLGetEmpresaItems') 
    data = data.json() 
    data = json.dumps(data)
    data = json.loads(data)

    ListaEmpresa =  [] 

    for row in data:
        ListaEmpresa.append(EmpresaItemModel(**row))



    return render_template("CatProducto.html", lstEmpresa  = ListaEmpresa)
