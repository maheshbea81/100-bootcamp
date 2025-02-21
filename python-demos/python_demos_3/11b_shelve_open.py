import shelve

db = shelve.open('capitals')
print(db['UK'])
print(db['FR'])
db.close()
