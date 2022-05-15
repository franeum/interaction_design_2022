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

# Sensori

---

### un dispositivo che acquisisce in `ingresso` una certa grandezza e ne fornisce in `uscita` una di natura differente

---

### permette di acquisire `informazioni` dal `mondo reale` per una futura elaborazione

---

### Oggi i sensori ci permettono di acquisire ed elaborare moltissime informazioni diverse

---

#### *luce, suono, presenza, accelerazione, temperatura, radiazioni, pressione, movimento, orientamento, prossimità, distanza*  

---

### I segnali captati vengono tradotti e convertiti in un segnale `analogico` o `digitale`  

---

### ...e, eventualmente, inviati ad un dispositivo (computer o microcontroller) in grado di elaborarli per `scopi diversi` 

---

<img src=images/distance_sensor.svg style="background:none; border:none; box-shadow:none;" />

---

### Un sensore può inviare al microcontroller un segnale già elaborato, `digitale` o `analogico`. Questo implica che per ogni sensore il trattamento del segnale è di tipo diverso   

---

### Quello che interessa è la tipologia del segnale elaborato:
1.  sensori che inviano segnali `0/1` (acceso/spento, presente/assente, on/off, click del mouse, etc...)
2.  sensori che inviano segnali `continui` (distanza in cm, temperatura in gradi, coordinate del mouse, etc...)   

---

### Osservando il comportamento di un sensore collegato al microcontroller possiamo pensare al segnale di un sensore come un oggetto (grafico) di *Cycling74 Max*   

---

### Un sensore del tipo 1 (0/1) può essere pensato come un `bang` oppure talvolta come un `toggle`, mentre un sensore continuo può essere pensato come uno `slider` o un `fader`.

---

## Esempi   

---

### sensore PIR (infrarossi) di presenza: rileva la presenza di un corpo vivo (uomo o animale) inviando un segnale di `1` quando il corpo entra nel campo d'azione del sensore

--

`BANG`

---

### tasto del mouse: invia `1` quando viene premuto, invia `0` quando viene rilasciato

--

`TOGGLE`

---

### Sensore di distanza a ultrasuoni, invia la distanza in cm

--

`SLIDER`

---

## SENSORI NEL KIT

---

### POTENZIOMETRO

--

#### permette di inviare un segnale elettrico variabile sulla base dell'azione manuale su una manopola

---

### PUSH BUTTON

--

#### pulsante a pressione manuale

---

### KEYPAD

--

#### matrice di pulsanti

---

### DHT-11 (TEMPERATURA)

--

#### invia un voltaggio che varia in base alla temperatura

---

### PHOTORESISTOR (LUCE)

--

#### invia un voltaggio che varia in base alla luminosità

---

### INFRARED MOTION SENSOR (PRESENZA)

--

#### memorizza una posizione attuale con un raggio a infrarossi, quindi basato sul calore cirocstante. Se l'ambiente cambia per la presenza di un corpo, il sensore invia un segnale pari a 1

---

### ULTRASONIC RANGING MODULE (DISTANZA)

--

#### invia un segnale digitale che rappresenta la distanza di un ostacolo dal sensore

---

### MPU-6050 MODULE (ACCELEROMETRO E GIROSCOPIO)

--

#### `accelerometro`: misura la deviazione di un oggetto in movimento rispetto al piano verticale
#### `giroscopio`: misura l'orientamento rispetto a 3 assi

---

### VIDEOCAMERA

--

#### ...


