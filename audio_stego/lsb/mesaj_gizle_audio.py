import numpy as np
from scipy.io import wavfile

def string_to_bits(s):
    return ''.join(format(ord(char), '08b') for char in s)

def embed_data(audio_path, output_path, message):
    samplerate, data = wavfile.read(audio_path)
    data = data.copy()
    
    bits = string_to_bits(message) + '1111111111111110'  # End marker
    bit_idx = 0

    for i in range(len(data)):
        if bit_idx < len(bits):
            if isinstance(data[i], np.ndarray):
                data[i][0] = (data[i][0] & ~1) | int(bits[bit_idx]) 
            else:
                data[i] = (data[i] & ~1) | int(bits[bit_idx])
            bit_idx += 1
        else:
            break

    wavfile.write(output_path, samplerate, data)
    print("Veri başarıyla gömüldü ve kaydedildi:", output_path)

embed_data('original_ses.wav', 'output_ses.wav', 'MESAAJ GIZLI')
