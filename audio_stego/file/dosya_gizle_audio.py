import numpy as np
from scipy.io import wavfile

# gizli.txt dosyasını ikilik (binary) biçime çeviren fonksiyon
def file_to_bits(file_path):
    with open(file_path, 'rb') as f:
        byte_data = f.read()

    # Her byte 8 bitlik binary string'e çevrilir ve birleşik bir string olarak döndürülür
    return ''.join(format(byte, '08b') for byte in byte_data)

# Ses dosyasına gizli.txt dosya verisini gömen fonksiyon
def embed_file(audio_path, output_path, file_path):
    samplerate, data = wavfile.read(audio_path)
    data = data.copy()
    
    # Gömülecek dosya ikilik hale getirilir ve bitlerin sonuna bitiş belirteci eklenir
    bits = file_to_bits(file_path) + '1111111111111110'  # End marker
    bit_idx = 0

    for i in range(len(data)):
        if bit_idx < len(bits):
            if isinstance(data[i], np.ndarray):  # Stereo (çok kanallı) veri kontrolü
                data[i][0] = (data[i][0] & ~1) | int(bits[bit_idx])
            else:
                # Mono veri ise doğrudan bit yazılır
                data[i] = (data[i] & ~1) | int(bits[bit_idx])
            bit_idx += 1
        else:
            break

    wavfile.write(output_path, samplerate, data)
    print(f"'{file_path}' başarıyla '{output_path}' dosyasına gömüldü.")

embed_file('original_ses_2.wav', 'output_ses_2.wav', 'gizli.txt')
