# Need a copy of country.txt for this demo

fh_in = open('country.txt', 'rb')

index={}

while True:
    line = fh_in.readline()
    if not line:
        break
    fields = line.decode().split(',')
    index[fields[0]] = fh_in.tell() - len(line)

key = input('Enter a country:')
fh_in.seek(index[key])
print(fh_in.readline().decode(), end="")
