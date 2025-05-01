from scipy.io import wavfile
import numpy as np

def bits_to_string(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def extract_data(audio_path):
    samplerate, data = wavfile.read(audio_path)
    bits = ""

    for sample in data:
        if isinstance(sample, np.ndarray):  
           sample = sample[0]  
        bits += str(sample & 1)   


        if bits[-16:] == '1111111111111110':  # End marker
            break

    hidden_message = bits_to_string(bits[:-16])  # Son işaretleyiciyi kaldırma işlemi
    print("Gizli mesaj:", hidden_message)

extract_data('output_ses.wav')
