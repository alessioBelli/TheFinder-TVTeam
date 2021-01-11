# Progetto comunicazioni multimediali
Il progetto denominato *The Finder* punta a creare un motore di ricerca in grado di estrarre le immagini più simili rispetto ad una inserita dall'utente 

## Architettura
L'architettura scelta, per la nostra applicazione, è di tipo *client-server*. Abbiamo effettuato questa scelta perchè così facendo, sarà possibile accedervi in facilità e con qualsiati dispositivo 
avente un browser. Inoltre, non sarà richiesto all'utente di scaricare nessun file all'interno del dispositivo.

La nostra web app è composta da 4 pagine: index.html, results.html, gallery.html e upload.html

## Istruzioni
Per utilizzare l'applicazione è necessario avere installato python sul proprio terminale. Inoltre è necessario installare
le seguenti librerie che non sono comprese nella libreria standard di Python.
- tensorflow
- flask
- openCV
- numpy
- pillow

Per installare le librerie è sufficiente eseguire sul proprio terminale il comando `pip install -r requirements.txt`.
Qualora non si volessero installare le librerie direttamente sul proprio terminale c'è la possibilità di creare un ambiente 
virtuale, ossia uno spazio indipendente dal resto del sistema in cui è possibile testare e lavorare con Python e pip.

### Come creare un ambiente virtuale
Per creare un ambiente virtuale, è sufficiente eseguire i seguenti comandi all'interno del terminale:
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

Dopo aver attivato l'ambiente virtuale, è sufficiente digitare il comando `pip install -r requirements.txt` per installare tutte le librerie necessarie. Infine, per eseguire l'applicativo da terminale, bisogna digitare il comando `python3 theFinder.py` (posizionandosi dentro la cartella del progetto). 
Una volta fatta partire l'applicazione, è possibile accedervi semplicemente usando un browser, mediante l'indirizzo `localhost:4555`.
