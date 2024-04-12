import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from scipy import ndimage
from scipy.io import wavfile as wav
from scipy.fftpack import fft, ifft, fftfreq, fftshift

# assume existing signal x
# frequency_data = fft(x)
# x = ifft(frequency_data) <- x blir komplex

# Numpy Lab 2
# ___________
# Uppgift 1
'''
def mandelbrot(c):
    n = 0
    z = 0
    while abs(z) <= 2 and n < 100:
        z = z * z + c
        n += 1
    return n


M = np.zeros((401, 401))
a = np.arange(-2, 2, 0.005)
b = np.arange(-2, 2, 0.005)
min = -2
max = 2

for A in a:
    for B in b:
        M[(round((A + 2) * 100), round((B + 2) * 100))] = mandelbrot(complex(A, B))
plt.imshow(M, cmap='hot', extent=(min, max, min, max))

plt.show()
'''
# Uppgift 2
# _________
'''
im = plt.imread("/Users/benjaminschmidt/Desktop/schmidt.png")

r = im[:, :, 0] / 3
g = im[:, :, 1] / 3
b = im[:, :, 2] / 3
picture = (r + g + b)
print(im.dtype)
# plt.imshow(picture, cmap="gray")
print(im.shape)
# plt.show()
print(picture.shape)
Gx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
Gy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

xd = ndimage.convolve(picture, Gx, mode='constant')
yd = ndimage.convolve(picture, Gy, mode='constant')
width = picture.shape[0]
height = picture.shape[1]
S = np.zeros([width, height])

for i in range(width):
    for j in range(height):
        S[i, j] = np.sqrt(xd[i, j]**2 + yd[i, j]**2)

S[S>0.1] = 1
# plt.imshow(S, cmap=plt.get_cmap("gray"))
plt.imshow(S, cmap="gray")
plt.show()
'''
# Uppgift 3 a)

# Fourier transformerar hela signalen som en serie av diskreta frekvenser
# Hur hög volym finns av första frekvensen? Andra frekvensen, etc.
# Frekvensanalys
t = np.arange(0, 2, 0.2)
sample_rate, sample = wav.read("./Piano_1_C (1).wav")
Fourier = fft(sample)

frequencies = fftfreq(Fourier.size, 1/sample_rate)
# plt.plot(fftshift(frequencies), fftshift(Fourier))
print(frequencies)
plt.plot(abs(Fourier[:int(len(Fourier)/2)]))
plt.show()


# 3 b)
def frequency_finder(sound_file):
    sample_rate_file, sample_file = wav.read(sound_file)
    freqy = np.argmax(abs(fft(sample_file)))
    # frequency_array = fftfreq(F.size, 1/sample_rate_file)
    # print(frequency_array)
    if freqy < 440:
        while freqy < 440:
            freqy = freqy * 2
    else:
        while freqy > 600:
            freqy = freqy / 3
            if freqy > 600:
                freqy = freqy / 2
    return freqy


def tone_finder(sound_file):
    # frequencies for: A Bb B C C# D Eb E F F# G G#
    key_list = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'A#', 'B', 'C']
    freq_list = [261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9, 523.3]
    
    biggest_frequency = frequency_finder(sound_file)
    tone = min(freq_list, key=lambda x: abs(x - biggest_frequency))
    i = 0
    for m in freq_list:
        if tone == m:
            tone_index = i
        i += 1
    n = 12*np.log2(biggest_frequency / 440.0) + 49
    # returnerar key för tonen
    return key_list[tone_index]


print(frequency_finder("./Piano_1_C (1).wav"))
print(tone_finder("./Piano_1_C (1).wav"))

print(tone_finder("./Piano_2.wav"))
print(tone_finder("./Piano_3.wav"))
print(tone_finder("./Piano_4.wav"))
print(tone_finder("./Piano_5.wav"))
print(tone_finder("./Piano_6.wav"))


# Gå från dur till moll
def major_to_minor(key):
    rate, data = wav.read("./Cdur.wav")
    N = len(data)   # Length
    T = float(N) / float(rate)  # Time duration in seconds

    x = np.linspace(0, rate, N)

    frq_data = fft(data)
    list = frq_data.tolist()

    for i in



