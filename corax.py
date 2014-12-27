from icestreamdata import IceStreamListener
from out import VOut
import time

ice = IceStreamListener('http://streaming.fueralle.org:8000', 'Radio CORAX')
out = VOut(max=20, limit=3940)

while(True):
    try:
    	listener = ice.get_listener()
    except Exception:
        print('{}: unable to read streamdata'.format(time.ctime()))
        continue
    out.set(listener)
    time.sleep(15)
