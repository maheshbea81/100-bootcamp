import time

fh_out = open('log.txt', 'rt')

while True:
    line = fh_out.readline()

    if not line:
        time.sleep(1)
        # tell returns the current position of the file object
        # seek changes the current file opsition
        # together these are used to move the file handle from -1 (end of file)
        # to the last position for further reading
        fh_out.seek(fh_out.tell())
    else:
        print(line, end="")
