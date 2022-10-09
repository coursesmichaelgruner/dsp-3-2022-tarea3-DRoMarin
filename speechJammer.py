import sounddevice as sd
import numpy as np
import queue

delay = 1000
q = queue.Queue()
fs = 8000
chunk = 8
for n in range(delay):
    q.put(np.zeros([chunk,1],dtype = "f"))

#def callback(indata,outdata,frames,time,status):
#    if status:
#        print(status)
#    print(len(indata))
#    outdata[:]=indata

mic = sd.Stream(samplerate=fs,blocksize=chunk, dtype='float32',channels=1)#,callback=callback)
with mic:
    while True:
        data,_ = mic.read(chunk)
        q.put(data)
        out = q.get()
        mic.write(out)

    
