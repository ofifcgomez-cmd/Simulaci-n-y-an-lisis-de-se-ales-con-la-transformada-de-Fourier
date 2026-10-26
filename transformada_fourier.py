# ACTIVIDAD FORMATIVA 2
# Simulación y análisis de señales con la Transformada de Fourier

import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración del muestreo
fs = 1000
N = 2048
t = np.arange(N) / fs
df = fs / N

# 2. Generación de señales
pulso = np.where((t >= 0.5) & (t < 0.6), 1.0, 0.0)
escalon = np.where(t >= 1.0, 1.0, 0.0)
frecuencia = 50
senoidal = np.sin(2 * np.pi * frecuencia * t)

senales = {
    "Pulso rectangular": pulso,
    "Función escalón": escalon,
    "Señal senoidal": senoidal,
}

# 3. Transformada Discreta de Fourier y gráficas
frecuencias = np.fft.fftshift(np.fft.fftfreq(N, d=1 / fs))
fig, axes = plt.subplots(3, 3, figsize=(15, 10))

for columna, (nombre, x) in enumerate(senales.items()):
    X = np.fft.fft(x)
    X_centrada = np.fft.fftshift(X)
    magnitud = np.abs(X_centrada) / N
    fase = np.angle(X_centrada)

    # La fase de componentes de magnitud casi cero no es significativa.
    umbral = 0.01 * np.max(magnitud)
    fase_visible = np.where(magnitud > umbral, fase, np.nan)

    axes[0, columna].plot(t, x)
    axes[0, columna].set_title(nombre + " - Dominio del tiempo")
    axes[0, columna].set_xlabel("Tiempo (s)")
    axes[0, columna].set_ylabel("Amplitud")
    axes[0, columna].grid(True)

    axes[1, columna].plot(frecuencias, magnitud)
    axes[1, columna].set_xlim(-250, 250)
    axes[1, columna].set_title(nombre + " - Magnitud")
    axes[1, columna].set_xlabel("Frecuencia (Hz)")
    axes[1, columna].set_ylabel("|X(f)|")
    axes[1, columna].grid(True)

    axes[2, columna].plot(frecuencias, fase_visible)
    axes[2, columna].set_xlim(-250, 250)
    axes[2, columna].set_ylim(-np.pi, np.pi)
    axes[2, columna].set_title(nombre + " - Fase")
    axes[2, columna].set_xlabel("Frecuencia (Hz)")
    axes[2, columna].set_ylabel("Fase (rad)")
    axes[2, columna].grid(True)

plt.tight_layout()
plt.savefig("resultados_fourier.png", dpi=200)
plt.show()

# 4. Verificación de linealidad
x1 = np.sin(2 * np.pi * 50 * t)
x2 = np.cos(2 * np.pi * 120 * t)
a, b = 2, 0.5

transformada_combinada = np.fft.fft(a * x1 + b * x2)
combinacion_transformadas = a * np.fft.fft(x1) + b * np.fft.fft(x2)
error_linealidad = np.max(
    np.abs(transformada_combinada - combinacion_transformadas)
)
print("Error máximo de linealidad:", error_linealidad)

# 5. Verificación del desplazamiento circular
desplazamiento_muestras = 100
x_desplazada = np.roll(x1, desplazamiento_muestras)
X_original = np.fft.fft(x1)
X_desplazada = np.fft.fft(x_desplazada)
k = np.arange(N)
factor = np.exp(-2j * np.pi * k * desplazamiento_muestras / N)
X_teorica_desplazada = X_original * factor
error_desplazamiento = np.max(
    np.abs(X_desplazada - X_teorica_desplazada)
)
print("Error máximo de desplazamiento:", error_desplazamiento)

plt.figure(figsize=(10, 4))
plt.plot(t[:300], x1[:300], label="Original")
plt.plot(t[:300], x_desplazada[:300], "--", label="Desplazada")
plt.title("Propiedad de desplazamiento temporal (circular)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("desplazamiento_temporal.png", dpi=200)
plt.show()

# 6. Comparación de dos frecuencias
seno_30 = np.sin(2 * np.pi * 30 * t)
seno_60 = np.sin(2 * np.pi * 60 * t)

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t[:200], seno_30[:200])
plt.title("Señal senoidal de 30 Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t[:200], seno_60[:200])
plt.title("Señal senoidal de 60 Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.savefig("escalamiento_frecuencia.png", dpi=200)
plt.show()

print("Resolución en frecuencia:", df, "Hz")
print("Frecuencia de muestreo:", fs, "Hz")
print("Simulación finalizada correctamente.")


