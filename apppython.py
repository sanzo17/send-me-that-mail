from flask import Flask, request, render_template
from flask_mail import Mail, Message
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configuration du serveur de messagerie
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAYLI")
app.config['MAIL_PASSWORD'] = os.getenv("PASSIWORDI")

mail = Mail(app)

@app.route("/form", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/mail', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    heure_actuelle = datetime.now().time()
    heure = heure_actuelle.strftime('%H:%M:%S')
    pending_message = "Email en cours d'envoi"
    print(f"[{heure}] {pending_message}")

    msg = Message("Bienvenue sur Météojob", sender='meteojobcontact@gmail.com', recipients=[email])
    msg.html = render_template('mail.html', name=name)
    mail.send(msg)
    
    heure_actuelle = datetime.now().time()
    heure = heure_actuelle.strftime('%H:%M:%S')
    message = "Email envoyé avec succès"
    print(f"[{heure}] {message}")

    return render_template('mail.html', name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)
