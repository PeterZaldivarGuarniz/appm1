from flask import Flask, jsonify, request, render_template
import joblib
import sklearn

#curl -d "{\"Medidas\":[[14.13,19.29,91.97,654.89,0.1,0.1,0.09,0.05,0.18,0.06,0.41,1.22,2.87,40.34,0.01,0.03,0.03,0.01,0.02,0.0,16.27,25.68,107.26,880.58,0.13,0.25,0.27,0.11,0.29,0.08]]}" -H "Content-Type: applocation/json" -X POST http://127.0.0.1:5000/predecir
#http get http://127.0.0.1:5000/predecir

#curl "{\"Medidas\":[[14.13,19.29,91.97,654.89,0.1,0.1,0.09,0.05,0.18,0.06,0.41,1.22,2.87,40.34,0.01,0.03,0.03,0.01,0.02,0.0,16.27,25.68,107.26,880.58,0.13,0.25,0.27,0.11,0.29,0.08]]}" -H "Content-Type: applocation/json" -X POST http://127.0.0.1:5000/predecir

app = Flask(__name__)

@app.route("/")
def home():
    return 'hola mundo'

 @app.route("/predecir", methods=["POST"])
 def predecir():
     try:
         resultado = request.form
         clf = joblib.load("modelo_arbol.pkl")
         prediccion = clf.predict(resultado)
         prediccion = round(prediccion)
     except:
         prediccion = None
     return render_template('http://127.0.0.1:8050', result={'Predicción': prediccion})

if __name__ == '__main__':
    app.run()
