from baresipy import BareSIP
from time import sleep
import signal
import sys

to = "7101"

gateway = "sipserver.local"
user = "7157"
auth_user = "testuser"
auth_pswd = "testpassword"
debug = False


while True:

    b = BareSIP(user, auth_user, auth_pswd, gateway, debug=debug)

    while b.running:

        b.call(to)

        sleep(5)
        if b.call_established:
            b.send_audio("/usr/share/baresip/message.mp3")
            if b.dtmf:
                print(b.dtmf_digit)
                if(b.dtmf_digit == 2):
                   b.send_audio("/usr/share/baresip/dtmf_two_message.mp3")
                if(b.dtmf_digit == 9):
                   b.send_audio("/usr/share/baresip/dtmf_nine_message.mp3")
            b.hang()
            b.quit()
            sys.exit(0)
    b.hang()
    b.quit()

    sleep(15)


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    b.quit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
