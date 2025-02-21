import pickle
import gzip

capitals = {'New Zealand': 'Wellington', 'Finland': 'Helsinki',
        'Sweden': 'Stockholm',  'Spain': 'Madrid'}

f_output = gzip.open('capitals_compressed.pgz', 'wb')
pickle.dump(capitals, f_output)
f_output.close()
