import sys
from baresipy import BareSIP
from time import sleep
import signal

to = "7157"

gateway = "sip.gateway"
user = "7150"
auth_user = "testuser"
auth_pswd = "testpassword"
debug = False


b = BareSIP(user, auth_user, auth_pswd, gateway, debug=debug)

while b.running:

    b.call(to)
    
    if b.call_established:
        b.send_audio("/usr/share/baresip/dot.mp3")
        #b.send_dtmf("123")
        if b.dtmf:
            print(b.dtmf_digit)
            if(b.dtmf_digit == 2):
                b.send_audio("/usr/share/baresip/ack.mp3")
            if(b.dtmf_digit == 9):
                b.send_audio("/usr/share/baresip/review.mp3")

        b.hang()
        b.quit()
    sleep(5)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    b.quit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
