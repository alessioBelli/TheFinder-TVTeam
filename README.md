# Progetto comunicazioni multimediali
Il progetto denominato *The Finder* punta a creare un motore di ricerca in grado di estrarre le immagini più simili rispetto ad una inserita dall'utente.

## Architettura
L'architettura scelta, per la nostra applicazione, è di tipo *client-server*. Abbiamo effettuato questa scelta perchè così facendo, sarà possibile accedervi in facilità e con qualsiati dispositivo 
avente un browser. Inoltre, non sarà richiesto all'utente di scaricare nessun file all'interno del dispositivo.

La nostra web app è composta da 4 pagine: index.html, results.html, gallery.html e upload.html


Per i dettagli si rimanda al report completo: link report.pdf

## Istruzioni
Per testare l'applicazione (creando un server localmente nella propria macchina) è necessario avere installato python sul proprio terminale. Inoltre è necessario installare
le seguenti librerie che non sono comprese nella libreria standard di Python.
- tensorflow
- flask
- openCV
- numpy
- pillow

NB: Per poter installare le librerie, è stato riscontrato su Windows che potrebbe essere necessario aver abilitato l'opzione "Removing the MAX_PATH Limitation" contestualmente all'installazione di Python. Per maggiori dettagli: https://docs.python.org/3/using/windows.html#removing-the-max-path-limitation

Dopo aver scaricato lo zip da GitHub e averlo decompresso, per installare le librerie è sufficiente eseguire sul proprio terminale il comando `pip install -r requirements.txt` dopo essersi posizionati al percorso della cartella decompressa.

Infine, per eseguire l'applicativo da terminale, bisogna digitare il comando `python3 theFinder.py`. 
Una volta fatta partire l'applicazione, è possibile accedervi semplicemente usando un browser, mediante l'indirizzo `localhost:4555`.

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
