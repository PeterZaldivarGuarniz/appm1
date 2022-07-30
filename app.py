from flask import Flask, jsonify, request, render_template
import joblib
import json

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
    clf = joblib.load("modelo_arbol.pkl")
    hrs = json.loads(request.data)
    prediccion = clf.predict(hrs)
    pre = prec(round(prediccion))
    return jsonify({"Predicción": str(pre)})

if __name__ == '__main__':
    app.run()
