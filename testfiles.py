import numpy as np
import sys
import time

print("Press CTRL+C to terminate the program")

try:
	while True:
		f = open("test.txt","ab")
		a=np.random.rand(1,5)
		np.savetxt(f,a)
		f.close()
		time.sleep(1)


		
except KeyboardInterrupt:
	print("OK, done")
	sys.exit(0)
    
    

