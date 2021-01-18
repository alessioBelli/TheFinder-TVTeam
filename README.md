# Progetto comunicazioni multimediali
Il progetto denominato *The Finder* punta a creare un motore di ricerca in grado di estrarre le immagini più simili rispetto ad una inserita dall'utente.

## Architettura
L'architettura scelta, per la nostra applicazione, è di tipo *client-server*. Abbiamo effettuato questa scelta perchè così facendo, sarà possibile accedervi in facilità e con qualsiasi dispositivo 
avente un browser. Inoltre, non sarà richiesto all'utente di scaricare nessun file all'interno del dispositivo.

La nostra web app è composta da 4 pagine: index.html, results.html, gallery.html e upload.html


Per i dettagli si rimanda al report completo: [Report finale](https://github.com/alessioBelli/TheFinder-TVTeam/blob/main/documentation/Report%20The%20Finder%20-%20TVTeam.pdf)

## Istruzioni
Per testare l'applicazione (creando un server localmente nella propria macchina) è necessario avere installato python sul proprio terminale. 
Inoltre è necessario installare
le seguenti librerie che non sono comprese nella libreria standard di Python.
- tensorflow
- flask
- openCV
- numpy
- pillow

NB: Per poter installare la libreria TensorFlow, è stato riscontrato su Windows che potrebbe essere necessario aver abilitato l'opzione "Removing the MAX_PATH Limitation" contestualmente all'installazione di Python. Per maggiori dettagli: https://docs.python.org/3/using/windows.html#removing-the-max-path-limitation

Dopo aver scaricato lo zip da GitHub e averlo decompresso, per installare le librerie è sufficiente eseguire sul proprio terminale il comando `pip install -r requirements.txt` dopo essersi posizionati al percorso della cartella decompressa.

Infine, per eseguire l'applicativo da terminale, bisogna digitare il comando `python3 theFinder.py`. 
Una volta fatta partire l'applicazione, è possibile accedervi semplicemente usando un browser, mediante l'indirizzo `localhost:4555`.

Nota: Al primo avvio assoluto dell'applicazione, verrà scaricato e salvato localmente in maniera automatica un pacchetto di circa 90 MB contenente i parametri pre-addestrati dell'algoritmo ResNet50.
Per quanto riguarda le feature del dataset di immagini, esse sono già presenti nello zip. Se si volesse ricalcolarle, basta eliminare la cartella "features" oppure aggiungere/rimuovere immagini alla cartella "gallery". Al primo avvio dell'applicazione dopo un'aggiunta o una modifica di features saranno necessari alcuni minuti per il ricalcolo e il salvataggio.


### Come creare un ambiente virtuale
Qualora non si volessero installare le librerie direttamente sul proprio terminale c'è la possibilità di creare un ambiente 
virtuale, ossia uno spazio indipendente dal resto del sistema in cui è possibile testare e lavorare con Python e pip.

E' sufficiente eseguire i seguenti comandi all'interno del terminale:
```
$ cd TheFinder
$ python3 -m venv venv
```

Windows:
`$ py -3 -m venv venv`

Una volta creato l'ambiente virtuale, basterà attiavarlo mediante il comando:
```
$ . venv/bin/activate
```

Windows: `> venv\Scripts\activate`

Dopo aver attivato l'ambiente virtuale, digitando il comando `pip install -r requirements.txt` vengono installate le librerie necessarie.

### Accedere al server da un altro dispositivo nella stessa rete
Se si volesse avviare il server in una macchina e accedere all'applicazione da un dispositivo qualsiasi **collegato alla stessa rete**, è necessaria una modifica al codice:
all'ultima riga del file theFinder.py, 
modificare
```
app.run(port=4555, debug=True, use_reloader=False)
```
con 

```
app.run(host="0.0.0.0", port=4555, debug=True, use_reloader=False)
```

Successivamente, dopo aver lanciato l'applicativo nella macchina server, prendere nota dell'indirizzo IP di quest'ultima.
Per collegarsi da un altro dispositivo, sarà sufficiente usare un browser, mediante l'indirizzo `indirizzoip_server:4555`. 
