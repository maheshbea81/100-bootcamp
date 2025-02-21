fh_out = open('spam.txt', 'wt')

try:
    fh_out.write('Spam, spam, spam!')
except FileNotFoundError as err:
    print('Blooming Vikings! ')
finally:
    # Always close file handle after use
    fh_out.close()
