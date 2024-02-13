## Used to Keep VPN connection active

from pynput.mouse import Controller
import random
import datetime as dt
import time
import subprocess

threshold = 200
current_time = dt.datetime.now()
end_time = current_time.replace(hour=18, minute=random.randint(3,16), second=0, microsecond=0)

while current_time < end_time:
    process = subprocess.Popen(["ioreg -c IOHIDSystem | sed -e '/HIDIdleTime/ !{ d' -e 't' -e '}' -e 's/.* = //g' -e 'q'"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode

    idle_time = int(out.decode().replace('\n', ''))

    idle_time_in_seconds = (idle_time/1000000000)

    if idle_time_in_seconds > threshold:
        m = Controller()
        m.move((m.position[0]+[-1,1][random.randrange(2)]), m.position[1])
        print('move:',dt.datetime.now(), idle_time_in_seconds)

    time.sleep(threshold)
    current_time = dt.datetime.now()