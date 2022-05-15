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

# Electronics tip'n'tricks

---

### electrical circuit
- closed path consisting of a set of components connected by *conductive* material and where there is a flow of **electrical current**

---

<img src=images/01_circuito.png style="background:none; border:none; box-shadow:none;" />

---

#### minimal fundamentals elements of an electrical circuit are:
  1.    *voltage generator* (*potential difference generator*)
  2.    *resistive* components

---

<img src=images/02_circuito+generatore.png style="background:none; border:none; box-shadow:none;" />

---

- the circuit is populated by electrons (atomic negative particles) that in the absence of force move disorderly, *de facto* remaining stationary
- if a potential difference (voltage) is activated in the circuit, electrons flow *neatly* along the conductors of the circuit

---

### *minimal* circuit (battery)

[battery + resistor](https://tinyurl.com/yjbjum7w)

---

- a potential difference is achieved through an **imbalance**
- an excess of electrons is created at one pole of the generator, a lack of electrons at the other pole
- the flow of electrons proceeds from the pole with excess toward the pole with lack
- the voltage generator maintains the imbalance


---


### the potential difference, otherwise called *voltage*, is measured in **Volt**
$$V$$

---

- voltage acts as a pressure force for the electrons
- the flow of electrons has a *speed*, determined by the voltage and resistance of the circuit
- this speed is called **current intensity**

---

### *minimal* circuit (generator)

[generator + resistor](https://tinyurl.com/ygcd335o)

---

### current intensity is measured in **Ampere**
$$A$$
##### often we will use milliAmpere
$$mA$$

---

#### Current intensity and Voltage are proportional:
- if the voltage increases, the intensity also increases

---

### the third element of an electrical circuit is the Resistance
- Resistance is a measure of the opposition to current flow in an electrical circuit
- you can keep the current constant increasing the **resistance**

---

### resistance is measured in **ohm**
$$\Omega$$

- and its multiples:
$$k\Omega$$
$$M\Omega$$

---

### Voltage, Current and Resistance are related
- the ohm law expresses this correlation:

$$V = IR$$
$$I = \frac{V}{R}$$
$$R = \frac{V}{I}$$

---

[ohm law](https://tinyurl.com/ydnows9b)

---

### example 1

---

- In a circuit, if it has a current of $15 mA$ (then $0.015 A$) and a resistance of $100\Omega$, what is the voltage?
- for the ohm law we have:
$$V = IR$$
- so: 
$$V = 0.015\cdot100 \implies 1.5 V$$

---

### example 2

- In a circuit , if it has a voltage of $5V$ and a resistance of $220\Omega$, what is the current?
- for the ohm law we have:
$$I = \frac{V}{R}$$
- so:
$$I = 5 / 220 \implies 0.0227A$$ (then $22.7mA$) 

---

### example 3

- In a circuit, if it has a voltage of $5V$ and a current of $25mA$, what is the resistence?
- for the ohm law:
$$R = \frac{V}{I}$$
- so:
$$R = 5 / 0.025 \implies 200\Omega$$ 

---

### in a circuit
- the current is **constant** in every point of circuit
- the voltage presents drops near every component

---

### voltage drops

[drops](https://tinyurl.com/yjosb9ls)

---

### led

- diode that produces fotons (light)
- led produces a drop voltage caused by his forward voltage

[circuit](https://tinyurl.com/ydzfyfew)

---

### calculate resistor for a led

$$R=\frac{(V-V_f)}{I}$$
