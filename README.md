# Actividad formativa 2: Simulación y análisis de señales con la Transformada de Fourier

## Descripción
Proyecto académico en Python para generar señales elementales y analizarlas en los dominios del tiempo y la frecuencia mediante la Transformada Discreta de Fourier (DFT), calculada con FFT.

## Señales incluidas
- Pulso rectangular
- Función escalón
- Señal senoidal de 50 Hz

## Propiedades analizadas
- Linealidad
- Desplazamiento temporal circular
- Comparación de señales senoidales de 30 Hz y 60 Hz

## Requisitos
- Python 3
- NumPy
- Matplotlib

## Instalación en Windows
1. Instala Python 3 desde https://www.python.org/downloads/ y, durante la instalación, activa **Add Python to PATH**.
2. Extrae el archivo ZIP en una carpeta.
3. Abre esa carpeta y haz clic en la barra de dirección del Explorador de archivos, escribe `cmd` y presiona Enter.
4. Ejecuta:

```bash
python -m pip install -r requirements.txt
```

5. Ejecuta la simulación:

```bash
python transformada_fourier.py
```

El programa abrirá las gráficas y guardará los archivos PNG en la carpeta desde la que se ejecuta.

## Archivos generados
- `resultados_fourier.png`
- `desplazamiento_temporal.png`
- `escalamiento_frecuencia.png`

## Interpretación breve
El pulso rectangular contiene un espectro amplio; la función escalón tiene una componente continua y componentes de baja frecuencia; la señal senoidal concentra su contenido alrededor de su frecuencia. La linealidad y el desplazamiento se verifican numéricamente mediante el error máximo.

## Autor
Alejandro Gomez Jimenez
