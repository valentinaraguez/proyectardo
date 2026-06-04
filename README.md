# proyectardo
Colaboración y Flujo de  Trabajo en GitHub
# 🎮 Wordle en Python

Un juego inspirado en el popular **Wordle**, desarrollado completamente en **Python** para ejecutarse desde la consola.

El objetivo es adivinar una palabra secreta antes de que se agoten los intentos disponibles.

---

## 📸 Vista General

El juego permite:

- Elegir diferentes niveles de dificultad.
- Jugar con palabras de distintas longitudes.
- Recibir pistas visuales después de cada intento.
- Consultar estadísticas de victorias.
- Jugar múltiples partidas sin reiniciar el programa.

---

## ✨ Características

- 🌟 Dificultad Fácil (3 letras)
- 📘 Dificultad Normal (4 letras)
- 🎯 Dificultad Media (5 letras)
- 🔥 Dificultad Difícil (6 letras)
- 💀 Dificultad Experta (7 letras)
- 🎲 Modo Aleatorio
- 📊 Estadísticas de partidas
- 🔤 Registro de letras utilizadas
- 🎨 Indicadores visuales mediante emojis
- ✅ Validación de entradas del usuario

---

## 🟩 Sistema de Pistas

Después de cada intento, el juego muestra una pista visual:

| Símbolo | Significado |
|----------|-------------|
| 🟩 | Letra correcta en la posición correcta |
| 🟨 | Letra existe pero está en otra posición |
| ⬛ | La letra no está en la palabra |

### Ejemplo

Palabra secreta:

```text
PERRO
```

Intento:

```text
PATIO
```

Resultado:

```text
🟩 ⬛ ⬛ ⬛ 🟩
```

---

## 🎮 Niveles de Dificultad

| Nivel | Letras | Intentos |
|---------|---------|---------|
| Fácil | 3 | 4 |
| Normal | 4 | 6 |
| Medio | 5 | 6 |
| Difícil | 6 | 8 |
| Experto | 7 | 8 |
| Aleatorio | Variable | Variable |

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/valentinaraguez/proyectardo.git
```

### 2. Entrar al directorio

```bash
cd recoyork-python
```

### 3. Ejecutar el programa

```bash
python recoyork.py
```

o

```bash
python3 recoyork.py
```

---

## 📂 Estructura del Proyecto

```text
proyectardo/
│
├── recoyork.py
└──  README.md
```

---

## 🛠 Tecnologías Utilizadas

- Python 3
- Random (librería estándar)
- Consola / Terminal

---

## 📈 Estadísticas

El programa registra:

- Partidas jugadas
- Partidas ganadas
- Porcentaje de victorias

Ejemplo:

```text
Partidas jugadas: 15
Partidas ganadas: 9
Porcentaje de victorias: 60%
```

---

## 🔮 Mejoras Futuras

- Guardar estadísticas en archivos.
- Ranking de jugadores.
- Más palabras por dificultad.
- Interfaz gráfica con Tkinter.
- Versión web con HTML, CSS y JavaScript.
- Modo multijugador.
- Sistema de puntuación.

---

## 👨‍💻 Autor

**Ema Valle y valentinaraguez**

Proyecto realizado como práctica de programación en Python.

---

## 📜 Licencia

Este proyecto es de uso educativo y puede modificarse libremente para aprendizaje y mejora.

---

⭐ Si te gustó el proyecto, no olvides darle una estrella al repositorio.