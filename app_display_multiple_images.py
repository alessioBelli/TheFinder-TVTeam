import os
from flask import Flask, request, render_template, send_from_directory
from flask import Flask, session, request, redirect, url_for
import shutil
import comparazione
import createAndSaveHisto
import query
import string
import random
import json
import estrai_da_database

__author__ = 'io'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/")
def index():
    image_names = os.listdir('./gallery')
    return render_template("index.html", numeroImage = len(image_names))

@app.route("/upload", methods=['GET'])
def upload_get():

    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    if not session.get('user') is None:
        print("loggato")
    else:
        print("Nuovo Utente, creazione sessione")
        session["user"] = id_generator(10)
    print(session.get("user"))
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if os.path.isdir("./images") == True:
        print("Directory già presente")
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):
        listImmagini = os.listdir("./images")
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        estensione = filename[-3:]
        print(session.get("user") +"."+ estensione)
        filename = session.get("user") +"."+ estensione
        if filename in listImmagini:
            os.remove("./images/"+filename)
        
        session["quantity"] = request.form.get('quantity')
        session["lastImage"] = filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        
    dati = elaborazioneImmagini()


    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("upload.html", image_name=filename)
    return render_template("complete.html", input_image=session.get("lastImage"), dati=dati)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./gallery')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

@app.route('/gallery/<filename>')
def send_image(filename):
    return send_from_directory("gallery", filename)


def elaborazioneImmagini():
    #elabora(session.get("lastImage"),session.get("quantity"))
    filenames = comparazione.compara(session.get("lastImage"),session.get("quantity"))
   
    dati = json.loads(filenames)

    for filename in dati:
        filename["percentage"] = '%.1f'%(float(filename["percentage"]))
    
    return dati


@app.route('/complete')
def complete():
    
    if session.get("user") == None:
        return render_template('404.html'), 404
    
    return render_template("complete.html")

@app.route('/complete/<filename>')
def send_image_complete(filename):
    print(filename)
    if filename in session.get("lastImage"):
        source = "images"
    else:
        source = "gallery"
    return send_from_directory(source, filename)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def scriviFile(nomeFile, testo):
    file1 = open(nomeFile, "w")
    file1.write(testo)
    file1.close()

if __name__ == "__main__":
    createAndSaveHisto.saveHisto()
    #estrai_da_database.creazioneFeature()
    app.secret_key = 'super secret key'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(port=4555, debug=True)