from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key="Benny bob wuz heer."

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['localizacion'] = request.form['localizacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']
    return redirect('/resultado')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

if __name__=="__main__":
    app.run(debug=True)