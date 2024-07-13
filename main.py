import numpy as np

temperaturas = np.array([22, 21, 19, 18.5, 20.3, 25, 1])

media_temperatura = np.mean(temperaturas)
print(f"Média das temperaturas: {media_temperatura:.2f}°C")

max_temperatura = np.max(temperaturas)
min_temperatura = np.min (temperaturas)
print(f"Temperatura máxima: {max_temperatura}°C")
print(f"Temperatura mínima: {min_temperatura}°C")

altas_temperaturas = temperaturas[temperaturas > 21]
print(f"Temperatura acima de 21°C; {altas_temperaturas}")