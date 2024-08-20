import pyaudio
import wave

p = pyaudio.PyAudio()

CHUNK = 1024
FRT = pyaudio.paInt16
CHAN = 1
RT = 44100
REC_SEC = 5
max_tokens = 128

OUTPUT = "input.wav"
filename = "input.wav"


def listen():
    print("[Listening...]")
    stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK, input_device_index=1)
    frames = []
    for i in range(0, int(RT / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("[End]")
    stream.stop_stream()
    stream.close()

    w = wave.open(OUTPUT, 'wb')
    w.setnchannels(CHAN)
    w.setsampwidth(p.get_sample_size(FRT))
    w.setframerate(RT)
    w.writeframes(b''.join(frames))
    w.close()


def speak():
    f = wave.open("output.wav", "rb")
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)

    data = f.readframes(CHUNK)

    while data:
        stream.write(data)
        data = f.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
