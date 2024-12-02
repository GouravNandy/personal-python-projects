import os
os.environ['SD_ENABLE_ASIO'] = '1'
import sounddevice as sd
import soundfile as sf
import wavio as wv
from scipy.io.wavfile import write


def voice_recorder(freq, duration):
    try:
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2, dtype='float32')
        sd.wait()
        write("recording0.wav", freq, recording)
        wv.write("recording1.wav", recording, freq, sampwidth=2)
    except:
        return False
    else:
        return True

def play():
    data, fs = sf.read('recording0.wav')
    sd.play(data, fs)
    sd.wait()
    pass



if __name__ == '__main__':
    freq, duration = map(int, input("Enter the frequency and duration with a space in between: ").split(' '))
    print("Voice is being recorded . Please speak something !!")
    result = voice_recorder(freq,duration)
    if result == True:
        print('Voice Recorded')
    else:
        print('Voice couldnt be recorded')

    play()

