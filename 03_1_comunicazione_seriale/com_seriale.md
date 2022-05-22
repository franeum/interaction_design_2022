---

theme: "white"
transition: "slide"
transitionSpeed: "slow"
slideNumber: false
overview: false
previewLinks: false
controls: true
dataState: "no-title-footer"

---

<style>
    .reveal code {
        background-color: #66b3ff;
        color: #000000;
        padding: 0.2em 0.25em 0.2em 0.25em;
    }

    #title-footer {
        display: none;
    }
</style>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
<script>
    mermaid.initialize({ theme: 'neutral' })
</script>

# Comunicazione Seriale

---

#### Quando inviamo alla nostra scheda un comando in python
#### l'interprete che risiede nella scheda interpreta in comando e lo `esegue`

---

### Modalità di comunicazione fra utente e scheda
1.  Possiamo eseguire istruzioni interattivamente (una per volta), usando il REPL (READ-EVAL-PRINT-LOOP)
                    `>>>` {: .fragment}
2.  Oppure possiamo inviare alla scheda sequenze di istruzioni. Le istruzioni vengono inviate a gruppi
                    `script` {: .fragment}

---

### In entrambi i casi la scheda è collegata al computer e comunica con esso (quindi con l'utente) tramite un protocollo seriale, che permnette ai dati che viaggiano sul cavo (usb) di essere correttamente interpretati.

---

<img src=images/sercom_01.svg style="background:none; border:none; box-shadow:none;" />

---

### Se stacchiamo il cavo della scheda, non potremo più comunicare con essa, per due motivi:
1.  La scheda perderà l'alimentazione (ma ci sono altri modi per alimentarla) {: .fragment}
2.  Si interrompe la comunicazione seriale {: .fragment}

---

### Rimedio

--

### Possiamo caricare degli script in python direttamente all'interno della scheda, in modo che vengano eseguiti quando viene accesa

---

<img src=images/sercom_02.svg style="background:none; border:none; box-shadow:none;" />

---

### La scheda contiene al suo interno un file chiamato `boot.py`, che contiene varie configurazioni della scheda e che viene eseguito appena la scheda viene avviata

---

### Un secondo file, chiamato `main.py` viene *cercato*. Se viene trovato è eseguito subito dopo, altrimenti la scheda si mette in attesa di istruzioni dall'utente

---

### Per rendere la scheda `autonoma` dobbiamo quindi scrivere del codice python all'interno del file `main.py`

---

## Esercitazione 1 - Inviare dati dalla porta seriale

--

### Creiamo il file `main.py` con le seguenti istruzioni:
1.  Ogni secondo stampa la stringa `bang`
2.  Ogni secondo accendi/spegni un led
3.  Chiudere Mu-editor, staccare la scheda e ricollegarla per verificare che tutto funzioni

---

## Caratteristiche della comunicazione seriale
### SPEDIZIONE
1.  I dati, di qualunque tipo essi siano (int, float, str) sono convertiti in bytes
2.  I bytes (gruppi di 8 valori binari 0/1) vengono spediti lungo il cavo seriale
3.  Ogni bit uguale a zero sarà un voltaggio basso, altrimenti sarà un voltaggio alto

---

### RICEZIONE
#### Percorso inverso rispetto al precedente
1. Si riceve un segnale elettrico binario
2. Si converte in byte
3. Si interpretano i bytes come caratteri

---

<img src=images/sercom_03.svg style="background:none; border:none; box-shadow:none;" />

---

<img src=images/sercom_04.svg style="background:none; border:none; box-shadow:none;" />

---

### Quando micropython riceve dei dati sulla scheda tramite la porta seriale, li converte automaticamente in string (*str*)
### Quando li spedisce, il dispositivo che li riceve acquisisce dei bytes, e dobbiamo convertirli programmaticamente
### In max i dati ricevuti sulla seriale sono tradotti automaticamente in byte. Per avere dati meno grezzi bisogna convertirli

---

## Esercitazione 2 - Acquisire in Max i dati inviati dalla scheda

--

### Creiamo una patch `serial_data.maxpat` con il seguente comportamento:
1.  Quando riceve un messaggio inviato dalla ESP32, catturiamo i bytes e li convertiamo in `symbol` 
2. Interpretiamo il contenuto del *symbol* e, se è un `bang` accendiamo l'oggetto grafico *bang*


---

## Lettura di dati tramite ESP32 e python

---

### Oltre che inviare dati la scheda ESP32, grazie all'interprete python integrato, può ricevere (e interpretare) dati in entrata dalla porta seriale

---

### input()

---

### Se per inviare dati sulla seriale python usa **print()**, per acquisire dati dalla seriale si può usare `input()`, che interrompe l'esecuzione di uno script finché non si riceva qualcosa dalla seriale

---

## Esercitazione 3 - Inviare dati da Max sulla seriale

--

### Creare una patch che invii i seguenti messaggi sulla porta seriale:
    `accendi` e `spegni`

---

## Esercitazione 4 - Ricevere i dati sulla ESP32 inarrivo dalla porta seriale

--

### Creare uno script che:
1. Accenda un led quando dalla porta seriale arriva il messaggio `accendi`
2. Spenga un led quando dalla porta seriale arriva il messaggio `spegni`
