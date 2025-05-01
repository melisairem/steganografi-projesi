import numpy as np
from scipy.io import wavfile

# Bit dizisini 8 bitlik parçalara bölüp byte dizisine çeviren fonksiyon
def bits_to_bytes(bits):
    return bytes([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)])

# Ses dosyasından gizli veriyi çözüp bir dosyaya yazan fonksiyon
def extract_file(audio_path, output_file_path):
    samplerate, data = wavfile.read(audio_path)
    bits = ""

    for sample in data:
        if isinstance(sample, np.ndarray):
            sample = sample[0]
        bits += str(sample & 1)

        # 16 bitlik bitiş işareti bulunduğunda döngüyü sonlandıracak
        if bits[-16:] == '1111111111111110':  # End marker
            break

    # Bitiş işaretinden önceki bitleri byte dizisine çevirecek
    file_bytes = bits_to_bytes(bits[:-16]) 
    # Elde edilen byte verisi belirtilen dosyaya yazılır
    with open(output_file_path, 'wb') as f:
        f.write(file_bytes)
    print(f"Gizli dosya başarıyla çıkarıldı: {output_file_path}")

extract_file('output_ses_2.wav', 'çözülen_gizli.txt')