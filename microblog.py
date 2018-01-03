#!/usr/bin/python3

import os
import sys
import time

now = time.strftime("%c")
outfolder = sys.argv[1]
outfile = "%s.md" % now

def save(buf):
    path = os.path.join(outfolder, outfile)
    with open(path, 'a') as log:
        for line in buf:
            log.write("> %s\n" % line)

cmd = ""
buffer = []
while cmd != "quit":
    cmd = input("$ ")
    if cmd == "save":
        save(buffer)
        buffer = []
    elif cmd == "quit":
        save(buffer)
    else:
        buffer.append(cmd)



    



