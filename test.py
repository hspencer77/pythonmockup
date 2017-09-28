#!/bin/env python
import time

if __name__ == "__main__":
    if str(time.time()).endswith('1'):
        print "Time ends with a 1"
    else:
        print "Time ends with something else.."
