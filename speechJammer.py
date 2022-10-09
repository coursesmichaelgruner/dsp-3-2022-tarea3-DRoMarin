import sounddevice as sd
import numpy as np
import queue
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('delay', type = int)
args = parser.parse_args()

delay = args.delay
q = queue.Queue()
fs = 8000
chunk = 8
for n in range(delay):
    q.put(np.zeros([chunk,1],dtype = "f"))

mic = sd.Stream(samplerate=fs,blocksize=chunk, dtype='float32',channels=1)#,callback=callback)
with mic:
    while True:
        data,_ = mic.read(chunk)
        q.put(data)
        out = q.get()
        mic.write(out)

    
