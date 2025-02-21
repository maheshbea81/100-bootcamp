# Pickling converts Python objects into a stream of bytes
# which can be written to a file or across a network

import pickle

caps = {'Australia': 'Canberra', 'Eire': 'Dublin',
        'UK': 'London', 'US': 'Washington'}

output = open('capitals.p', 'wb')
pickle.dump(caps, output)
output.close()

