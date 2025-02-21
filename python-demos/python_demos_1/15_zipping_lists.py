# The zip function returns an iterator of tuples
farms = ['Home Farm', 'Muckworthy', 'Scales End', 'Brown Rigg']

squirrels = [42, 12, 2, 0]
rabbits = [395, 68, 57, 32]
moles = [12, 8, 0, 29]

for f, s, r, m in zip(farms, squirrels, rabbits, moles):
    print('Total for', f, ':', s + r + m)

#     Example 2
print("*" * 30)

keys = ['Australia', 'Eire', 'France', 'Finland', 'UK', 'US']
vals = ['Canberra', 'Dublin', 'Paris', 'Helsinki','London', 'Washington']
mydict = dict(zip(keys, vals))
print(mydict)

