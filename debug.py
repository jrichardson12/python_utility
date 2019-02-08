#!/opt/local/bin/python3
# authon: John Richardson
#   desc: Debug commands

import sys


# debug info----------------------------------------------|
def sysExe():
        print(sys.exc_info())


def typeOf(obj):
        print(type(obj))


def printAll(*args):
        for count, thing in enumerate(args):
                print('{0}. {1}'.format(count, thing))
# -------------------------------------------------------|
