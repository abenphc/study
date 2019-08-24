import wave
from pyaudio import PyAudio, paInt16

channels = 1
sampwidth = 2
framerate = 8000
NUM_SAMPLES = 1024
TIME = 2


def save_wave_file(filename, data):
    '''save the data to the wav file'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    my_buf = []
    stream = pa.open(format=paInt16, channels=1,
                     rate=framerate, input=True,
                     input_device_index = -1,
                     frames_per_buffer=NUM_SAMPLES)
    count = 0
    while count < TIME * 20:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print(".")
    stream.stop_stream()
    stream.close()
    pa.terminate()
    save_wave_file('01.wav', my_buf)
    print('over')


if __name__ == "__main":
    my_record()
    print("over")
