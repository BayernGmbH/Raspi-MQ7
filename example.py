from mq import *
import sys, time

print("Press CTRL+C to abort.")

mq = MQ();
while True:
    perc = mq.MQPercentage()
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write("%g," % perc["CO"])
    sys.stdout.flush()
    time.sleep(0.1)