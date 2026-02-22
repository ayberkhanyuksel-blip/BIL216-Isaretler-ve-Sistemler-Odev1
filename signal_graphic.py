import numpy as np
import matplotlib.pyplot as plt

# 1. Temel frekans f0 hesaplama (38, 63, 02)
f0 = 38 + 63 + 2 

# 2. Frekansların tanımlanması
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# 3. Örnekleme Frekansı (fs) seçimi (Nyquist: fs > 2 * f3)
fs = 20 * f3 

# 4. Görselleştirme (Subplot)
fig, axes = plt.subplots(4, 1, figsize=(10, 12))
plt.subplots_adjust(hspace=0.6)

# Sinyal 1 (f1)
t1 = np.arange(0, 3/f1, 1/fs)
y1 = np.sin(2 * np.pi * f1 * t1)
axes[0].plot(t1, y1)
axes[0].set_title(f'Sinyal 1: f1 = {f1} Hz (3 Periyot)')
axes[0].set_xlabel('Zaman (s)')
axes[0].grid(True)

# Sinyal 2 (f2)
t2 = np.arange(0, 3/f2, 1/fs)
y2 = np.sin(2 * np.pi * f2 * t2)
axes[1].plot(t2, y2)
axes[1].set_title(f'Sinyal 2: f2 = {f2} Hz (3 Periyot)')
axes[1].set_xlabel('Zaman (s)')
axes[1].grid(True)

# Sinyal 3 (f3)
t3 = np.arange(0, 3/f3, 1/fs)
y3 = np.sin(2 * np.pi * f3 * t3)
axes[2].plot(t3, y3)
axes[2].set_title(f'Sinyal 3: f3 = {f3} Hz (3 Periyot)')
axes[2].set_xlabel('Zaman (s)')
axes[2].grid(True)

# Sinyallerin Toplamı
# Görünürlük için en düşük frekansın (f2) zaman penceresi kullanılmıştır
t_sum = np.arange(0, 3/f2, 1/fs)
y_sum = np.sin(2 * np.pi * f1 * t_sum) + np.sin(2 * np.pi * f2 * t_sum) + np.sin(2 * np.pi * f3 * t_sum)
axes[3].plot(t_sum, y_sum)
axes[3].set_title('Sinyallerin Toplamı (f1 + f2 + f3)')
axes[3].set_xlabel('Zaman (s)')
axes[3].grid(True)

plt.show()