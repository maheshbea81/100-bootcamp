# The shelve module is used to store pickled objects by a string key in a database
# that looks like a dictionary

import shelve

db = shelve.open('capitals')
db['UK'] = 'London'
db['FR'] = 'Paris'
db.close()
