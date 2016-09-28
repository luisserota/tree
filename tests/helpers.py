import os
import subprocess
import time

def tree_correct(path):
    with open("/tmp/output.txt", "wb") as out, open("/tmp/err.txt", "wb") as err:
        subprocess.Popen(["tree",path], stdout=out, stderr=err)
    time.sleep(1)
    with open('/tmp/output.txt') as result:
        output = result.read()
    return output

def pytree(path):
    with open("/tmp/pytree.txt", "wb") as out, open("/tmp/pyerr.txt", "wb") as err:
        subprocess.Popen(["./pytree.py",path], stdout=out, stderr=err)
    time.sleep(1)
    with open('/tmp/pytree.txt') as result:
        output = result.read()
    return output
