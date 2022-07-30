from flask import Flask, jsonify, request, render_template
import joblib
import json
import pandas as pd

app = Flask(__name__)
def prec(x):
    if round(x) == 0:
        r = "Tumor benigno"
    else:
        r = "Tumor maligno"
    return r
@app.route("/")
def home():
    return 'hola mundo'
@app.route("/predecir", methods = ["POST"])
def predecir():
    clf = joblib.load("./modelo_arbol.pkl")
    hrs = json.loads(request.data)
    dato = pd.DataFrame(columns=list(hrs.keys()))
    dato = dato.append(hrs, ignore_index=True)
    prediccion = round(clf.predict(dato)[0])
    pre = prec(round(prediccion))
    return jsonify({"Predicción": pre})

if __name__ == '__main__':
    app.run()
