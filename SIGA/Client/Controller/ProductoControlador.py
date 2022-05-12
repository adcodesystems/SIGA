# import sys
# sys.path.insert(0,"..")

import json
import requests 
from App import app
from flask import Flask, render_template, request, redirect, url_for, flash
from Model.ProductoModel import *
from ApiResConfig import *




data = requests.get('http://127.0.0.1:3030/producto') 
data = data.json() 
data = json.dumps(data)
data = json.loads(data)

ListaEmpresa =  [] 

for row in data:
    ListaEmpresa.append(ProductoModel(**row))
    print(row)

