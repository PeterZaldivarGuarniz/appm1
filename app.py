from flask import Flask, jsonify, request, render_template
import joblib
import sklearn

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

@app.route("/predecir", methods = ["GET", "POST"])
def predecir():
    if request.method == "POST":
        clf = joblib.load("modelo_arbol.pkl")
        hrs = request.form["hrs"]
        prediccion = clf.predict(hrs)
        pre = round(prediccion)
    # try:
    #     resultado = request.form
    #     clf = joblib.load("modelo_arbol.pkl")
    #     prediccion = clf.predict(resultado)
    #     prediccion = round(prediccion)
    # except:
    #     prediccion = None
    return render_template('http://127.0.0.1:8050', Prediccion=pre)

if __name__ == '__main__':
    app.run()
