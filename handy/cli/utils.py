import humanize
import time
import os

msg_help_timer = "Written by junying, 2019-06-05 \
                 \nUsage: timer \
                 \nExample: timer "
def log(t):
    fullpath='/tmp/tictoc'
    output = []
    # read
    if os.path.exists(fullpath) and os.path.isfile(fullpath):
        with open(fullpath) as f: 
            for line in f: output.append(line)
    # overwrite
    with open(fullpath, 'w') as f:
        f.writelines([str(t)])
    return int(output[-1]) if len(output) > 0 else 0

def timer():
    import sys
    if any("-h" in argv for argv in sys.argv): return msg_help_timer
    toc = int(time.time())
    tic = log(toc)
    return humanize.naturaltime(toc-tic)