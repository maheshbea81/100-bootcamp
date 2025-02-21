import sys

fh_out = open('spam.txt', 'at')
print("Hello", file=fh_out)
print("Hello again", file=fh_out)
print("Oops, we had an error", file=sys.stderr)
