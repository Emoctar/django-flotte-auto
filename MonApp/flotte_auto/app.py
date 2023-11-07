from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page de tableau de bord
@app.route('/gestionnaire_parc_profile')
def dashboard():
    # Récupération des données de la base de données ou d'où vous stockez vos données
    data = {
        'total_vehicules': 50,
        'vehicules_en_service': 40,
        'vehicules_en_panne': 5,
        'vehicules_disponibles': 35
    }

    return render_template('GesParc/Dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
