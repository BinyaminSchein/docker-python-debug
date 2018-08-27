import os
import sys
import time
import ptvsd
ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))
ptvsd.wait_for_attach()

time.sleep(1.5)

print('a breakpoint here')
print('but none here')