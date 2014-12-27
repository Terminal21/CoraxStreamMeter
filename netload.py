import psutil
import time
from out import AOut

out = AOut(max=300000, limit=3940)

recv = psutil.network_io_counters(pernic=True)['eth0'].bytes_recv
while(True):
    new_recv = psutil.network_io_counters(pernic=True)['eth0'].bytes_recv
    delta = new_recv - recv
    out.set(delta)
    recv = new_recv
    time.sleep(0.3)
