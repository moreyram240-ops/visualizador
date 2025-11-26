# Visualizador de Ordenamientos  
*(Trabajo Práctico)*

Este proyecto implementa un visualizador interactivo para algoritmos de ordenamiento utilizando **Python ejecutado directamente en el navegador** 

---

## Características
- Ejecución de algoritmos Python sin servidor.
- Visualización paso a paso.
- Barras numéricas o imagen dividida en columnas.
- Controles interactivos:
  - Play / Pausa / Paso / Reset
  - Velocidad ajustable
  - Cantidad de elementos
  - Recarga en caliente del código Python
- Algoritmos totalmente editables desde la carpeta `algorithms/`.

---

## Estructura del Proyecto

```
visualizador/
│
├── algorithms/
│   ├── sort_bubble.py
│   ├── sort_insertion.py
│   ├── sort_selection.py
│   ├── sort_template.py
│
├── README.md
└── index.html
```

---

##  Cómo funciona Pyodide + JS
Cada algoritmo debe implementar dos funciones:

```python
def init(vals):
    ...

def step():
    return {
        'a': i,
        'b': j,
        'swap': True/False,
        'done': True/False
    }
```

El visualizador en JavaScript ejecuta `step()` repetidamente y dibuja cada acción en el canvas.

---

## Ejecución del programa
Este proyecto "no necesita Python instalado".

Solo hay que abrir un terminal en la carpeta del proyecto y ejecutar:

python -m http.server
```

Luego, ingresar a:

```
http://localhost:8000
```

---

## Agregar los algoritmos
1. Copiá `algorithms/sort_template.py` con otro nombre:  
   `sort_mi_algoritmo.py`
2. Implementá tu lógica dentro de `init()` y `step()`.
3. Agregá tu opción en el selector del `index.html`.

---

## Personalización visual
El proyecto incluye:
- Colores modernos
- Efectos neon
- Animaciones suaves
- Tema adaptado para buena visibilidad del texto

---

## Integrantes:Moreyra Milagros, Ibañez Tiago, Carrizo Octavio 
Curso: Introduccion a la programación 
Año: 2025

---

## 📜 Licencia
Proyecto educativo — libre para uso académico.
