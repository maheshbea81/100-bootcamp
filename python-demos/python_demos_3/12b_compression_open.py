import pickle
import gzip

f_input = gzip.open('capitals_compressed.pgz', 'rb')
caps = pickle.load(f_input)
f_input.close()

print(caps)