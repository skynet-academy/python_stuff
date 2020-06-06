import sys

filename = sys.argv[1]

with open(filename, 'r') as hugefile:
    chunksize = 10
    readable = ''
    while hugefile:
        # if we don't want to start not from 1st byte
        # we do a hugefile.seek(skipbytes) to skip
        # skipbytes of bytes from the file start


        start = hugefile.tell()
        print("Starting at:", start)
        file_block = '' # holds chunck_size of lines


        for _ in range(start, start + chunksize):
            line = hugefile.readline()
            file_block = file_block + line
            # print('file_block', type(file_block), file_block)
        readable = readable + file_block
        print(readable)
        # tell where are we in file

        stop = hugefile.tell()
        print('readable', type(readable), readable)
        print('read bytes total:', len(readable))
        print('reading bytes from %s to %s'%(start, stop))


        input()


