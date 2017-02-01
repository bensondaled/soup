import pyaudio, warnings
import numpy as np

def play(arr, rate=44100):
    """play a numpy array as sound

    rate : int
        samples per second
    dtype : np.dtype
    """
    type_dict = {   np.dtype('int16') : pyaudio.paInt16,
                    np.dtype('int32') : pyaudio.paInt32,
                    np.dtype('int8') : pyaudio.paInt8,
                    np.dtype('float32') : pyaudio.paFloat32,
            }

    if arr.dtype not in type_dict:
        warnings.warn('data type of arr not accepted, casting to float32')
        arr = arr.astype(np.float32)

    p = pyaudio.PyAudio()
    stream = p.open(format=type_dict[arr.dtype],
        channels=arr.shape[1] if len(arr.shape)==2 else 1,
        rate=rate,
        output=True,
        )
    data = arr.tostring()
    stream.write(data)
