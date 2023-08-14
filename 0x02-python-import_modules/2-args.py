#!/usr/bin/python3
import sys
if (len(sys.argv) <= 1):
    print("0 arguments")
elif (len(sys.argv) == 2):
    print("{} argument".format(len(sys.argv) - 1))
    print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
else:
    print("{} arguments".format(len(sys.argv) - 1))
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))
