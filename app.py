from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/activitati_zilnice')
def activitati_zilnice():
    return render_template('activitati_zilnice.html')



@app.route('/activitati')
def activitati():
    return render_template('activitati.html')

@app.route('/simptome')
def simptome():
    return render_template('simptome.html')

@app.route('/stare_de_spirit')
def stare_de_spirit():
    return render_template('stare_de_spirit.html')

@app.route('/rezumat')
def rezumat():
    return render_template('rezumat.html')

@app.route('/obiective')
def obiective():
    return render_template('obiective.html')

@app.route('/share')
def share():
    return render_template('share.html')

if __name__ == '__main__':
    app.run(debug=True)
    #nskmnnksjm
    