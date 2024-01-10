from flask import Flask, render_template, request, redirect, url_for
from database import db, Activitati, Simptome, StareDeSpirit, Obiectiv
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

with app.app_context():
        db.init_app(app)
        migrate = Migrate(app, db)
        date = datetime.now().date()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activitati')
def activitati():
    activitati = Activitati.query.all()
    return render_template('activitati.html', activitati = activitati)

@app.route('/proceseaza_activitati', methods=['POST'])
def proceseaza_formular_activitati():
    if request.method == 'POST':
        ore_dormite = request.form['somn']
        durata_activitati = request.form['sport']
        mic_dejun = request.form['mic']
        pranz = request.form['pranz']
        cina = request.form['cina']

        exist = Activitati.query.filter_by(data = date).first()

        if not exist:
            activitate = Activitati(data = date, ore_dormite = ore_dormite, durata_activitati = durata_activitati, mic_dejun = mic_dejun, pranz=pranz, cina=cina)
            db.session.add(activitate)
            db.session.commit()
            message = 'success'
        else : 
            message = 'Inregistrarea exista deja, daca vrei sa modifici, te rog sa stergi vechia inregistrare'

    return redirect(url_for('activitati', message = message))

@app.route('/sterge_activitate', methods=['POST'])
def sterge_activitate():
    id = request.form['id']
    
    activitate_de_sters = Activitati.query.get(id)
    if activitate_de_sters:
        db.session.delete(activitate_de_sters)
        db.session.commit()
    
    return redirect(url_for('activitati'))

@app.route('/simptome')
def simptome():
    simptome = Simptome.query.all()
    return render_template('simptome.html', simptome = simptome)

@app.route('/proceseaza_simptome', methods=['POST'])
def proceseaza_formular_simptome():
    if request.method == 'POST':
        simptome_input = request.form['simptome-input']
        simptome = request.form['simptome']

        simptom = Simptome(data=date, simptom_input = simptome_input, simptom_select = simptome)
        db.session.add(simptom)
        db.session.commit()

    return redirect(url_for('simptome'))

@app.route('/sterge_simptom', methods=['POST'])
def sterge_simptom():
    id = request.form['id']
    
    simptom_de_sters = Simptome.query.get(id)
    if simptom_de_sters:
        db.session.delete(simptom_de_sters)
        db.session.commit()
    
    return redirect(url_for('simptome'))

@app.route('/stare_de_spirit')
def stare_de_spirit():
    stari_de_spirit = StareDeSpirit.query.all()
    return render_template('stare_de_spirit.html', stari_de_spirit = stari_de_spirit)

@app.route('/proceseaza_stare_de_spirit', methods=['POST'])
def proceseaza_formular_stare_de_spirit():
    if request.method == 'POST':
        stare_de_spirit = request.form['stare_spirit']
        emotie = request.form['emotie']

        stare = StareDeSpirit(data=date, stare = stare_de_spirit, emotie = emotie)
        db.session.add(stare)
        db.session.commit()

    return redirect(url_for('stare_de_spirit'))

@app.route('/sterge_stare_de_spirit', methods=['POST'])
def sterge_stare_de_spirit():
    id = request.form['id']
    
    stare_de_sters = StareDeSpirit.query.get(id)
    if stare_de_sters:
        db.session.delete(stare_de_sters)
        db.session.commit()
    
    return redirect(url_for('stare_de_spirit'))

@app.route('/rezumat')
def rezumat():
    result_zilnic = db.session.query(Activitati, Simptome, StareDeSpirit).outerjoin(Simptome, Activitati.data == Simptome.data).outerjoin(StareDeSpirit, Activitati.data == StareDeSpirit.data).order_by(desc(Activitati.data)).limit(1).all()
    result_saptamana = db.session.query(Activitati, Simptome, StareDeSpirit).outerjoin(Simptome, Activitati.data == Simptome.data).outerjoin(StareDeSpirit, Activitati.data == StareDeSpirit.data).order_by(desc(Activitati.data)).limit(7).all()
    obiectiv = Obiectiv.query.order_by(desc(Obiectiv.id)).limit(1).all()
    return render_template('rezumat.html', result_zilnic = result_zilnic, result_saptamana = result_saptamana, obiectiv = obiectiv)

@app.route('/obiective')
def obiective():
    obiectiv = Obiectiv.query.order_by(desc(Obiectiv.id)).limit(1).all()

    return render_template('obiective.html', obiectiv = obiectiv)

@app.route('/proceseaza_obiectiv', methods=['POST'])
def proceseaza_obiectiv():
    ore_dormite = request.form['somn']
    durata_activitati = request.form['sport']
    obiectiv = Obiectiv(ore_dormite = ore_dormite, durata_activitati = durata_activitati)
    db.session.add(obiectiv)
    db.session.commit()

    return redirect(url_for('obiective'))

if __name__ == '__main__':
    app.run(debug=True)