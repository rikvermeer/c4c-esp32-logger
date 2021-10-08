import network
# Conenct to wifi, default to reconnect 5 times
do_connect()


import time
print('Hello world! I can count:')
i = 1

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    print(i)
    i += 1
    time.sleep(1.0)  # Delay for 1 second.
