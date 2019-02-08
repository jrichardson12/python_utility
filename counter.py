#!/opt/local/bin/python3
# authon: John Richardson
#   desc: Counts the number of times a user uses the script.

import sys
import getpass
import datetime
import subprocess
sys.path.insert(0, r'path/to/utility')
import openFile


def scriptCounter(path, scriptName):
    user = getpass.getuser()
    timeStamp = datetime.datetime.now()
    usesLog = openFile.openFile(path +
                                scriptName + "/log/uses.log", 'a')
    count, ERR = subprocess.Popen(["wc -l " + path +
                                  scriptName + "/log/uses.log"],
                                  shell=True,
                                  stderr=subprocess.PIPE,
                                  stdout=subprocess.PIPE).communicate()
    usesLog.write(str(count) + ',' +
                  str(timeStamp) + ',' +
                  str(user) + '\n')
