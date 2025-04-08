import os
try:
    import numpy as np
    import sounddevice as sd
except:
    os.system('pip install numpy sounddevice')
    import numpy as np
    import sounddevice as sd


sample_rate = 44100  # Hz

def generate_sine_wave(frequency, duration, volume=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t) * volume
    return wave.astype(np.float32)

# تعریف نت‌های نمونه برای ملودی "Für Elise"
notes = [
    (659.25, 0.4),  # E5
    (622.25, 0.4),  # D#5
    (659.25, 0.4),  # E5
    (622.25, 0.4),  # D#5
    (659.25, 0.4),  # E5
    (494.00, 0.4),  # B4
    (587.33, 0.4),  # D5
    (523.25, 0.8),  # C5

    (440.00, 0.4),  # A4
    (261.63, 0.4),  # C4
    (329.63, 0.4),  # E4
    (440.00, 0.8),  # A4

    (493.88, 0.4),  # B4
    (440.00, 0.4),  # A4
    (392.00, 0.4),  # G4
    (329.63, 0.4),  # E4
    (349.23, 0.4),  # F4
    (294.66, 0.4),  # D4
    (329.63, 0.4),  # E4
    (220.00, 0.8),  # A3

    (659.25, 0.4),  # E5
    (622.25, 0.4),  # D#5
    (659.25, 0.4),  # E5
    (622.25, 0.4),  # D#5
    (659.25, 0.4),  # E5
    (494.00, 0.4),  # B4
    (587.33, 0.4),  # D5
    (523.25, 0.8),  # C5

    (440.00, 0.4),  # A4
    (261.63, 0.4),  # C4
    (329.63, 0.4),  # E4
    (440.00, 0.8),  # A4

    (493.88, 0.4),  # B4
    (440.00, 0.4),  # A4
    (392.00, 0.4),  # G4
    (329.63, 0.4),  # E4
    (349.23, 0.4),  # F4
    (294.66, 0.4),  # D4
    (329.63, 0.4),  # E4
    (220.00, 0.8)   # A3
]




song = np.array([], dtype=np.float32)
for freq, duration in notes:
    note_wave = generate_sine_wave(freq, duration)
    song = np.concatenate((song, note_wave))


sd.play(song, sample_rate)
sd.wait()  
