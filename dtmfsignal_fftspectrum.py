import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# --- 1. SABİTLER VE PARAMETRELER ---
# Ödevde belirtilen standart örnekleme hızı [cite: 68]
FS = 8000  
# Ödevde istenen süre aralığı (0.2 - 0.5 sn) [cite: 69]
SURE = 0.3 

# Standart DTMF Frekans Tablosu [cite: 48, 49]
DTMF_TABLE = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477), 'A': (697, 1633),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
}

def tus_basildi(tus):
    """Butona basıldığında sesi üreten, çalan ve spektrum analizini yapan ana fonksiyon."""
    f_low, f_high = DTMF_TABLE[tus]
    
    # Zaman dizisi oluşturma
    t = np.linspace(0, SURE, int(FS * SURE), endpoint=False)
    
    # Sinyal Sentezi: İki sinüs dalgasının toplamı [cite: 48, 73]
    # Normalizasyon: Cızırtıyı (clipping) önlemek için 0.5 ile çarpıyoruz [cite: 74]
    sinyal = 0.5 * (np.sin(2 * np.pi * f_low * t) + np.sin(2 * np.pi * f_high * t))
    
    # Sesi hoparlörden çalma [cite: 56, 75]
    sd.play(sinyal, FS)
    
    # --- SPEKTRUM GÖZLEMİ (FFT) - ARTI PUAN BÖLÜMÜ  ---
    n = len(sinyal)
    frekanslar = np.fft.fftfreq(n, 1/FS)
    fft_degerleri = np.fft.fft(sinyal)
    
    # Sadece pozitif frekansları filtrele
    pozitif = frekanslar > 0
    f_ekseni = frekanslar[pozitif]
    genlik_ekseni = np.abs(fft_degerleri[pozitif])

    # --- GÖRSELLEŞTİRME [cite: 55] ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.4)

    # 1. Grafik: Zaman Domaini (Sinyal Şekli)
    ax1.plot(t[:200], sinyal[:200], color='blue') # Netlik için ilk 200 örnek
    ax1.set_title(f"{tus} Tuşu: Zaman Domaini Grafiği")
    ax1.set_xlabel("Zaman (s)")
    ax1.set_ylabel("Genlik")
    ax1.grid(True)

    # 2. Grafik: Frekans Domaini (FFT Spektrumu)
    ax2.plot(f_ekseni, genlik_ekseni, color='red')
    ax2.set_title(f"{tus} Tuşu: Frekans Domaini (FFT Spektrumu)")
    ax2.set_xlabel("Frekans (Hz)")
    ax2.set_ylabel("Enerji")
    ax2.set_xlim(500, 2000) # Tuş frekanslarını görmek için 500-2000Hz arası
    ax2.grid(True)
    
    # Frekansların üzerine değerlerini yazma
    ax2.text(f_low, max(genlik_ekseni), f'{f_low} Hz', color='black', fontweight='bold')
    ax2.text(f_high, max(genlik_ekseni), f'{f_high} Hz', color='black', fontweight='bold')

    plt.show()

# --- 2. ARAYÜZ (GUI) TASARIMI  ---
root = tk.Tk()
root.title("ISTUN-BIL216 DTMF Sinyal Sentezi")

tus_takimi = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D'
]

# Butonları 4x4 Izgara (Grid) yapısında oluşturma
for i, tus in enumerate(tus_takimi):
    # lambda t=tus yapısı, her butonun kendi değerini fonksiyona göndermesini sağlar
    btn = tk.Button(root, text=tus, width=12, height=4, font=('Arial', 12, 'bold'),
                   command=lambda t=tus: tus_basildi(t))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)

print("DTMF Arayüzü Başlatıldı. Bir tuşa basarak sesi ve spektrumu görebilirsiniz.")
root.mainloop()