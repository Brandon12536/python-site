from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html') #direcciona hacia el archivo html creando rutinas

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
        app.run(debug=True)#la interfaz debuguea secuencialmente cuando se hace un cambio
