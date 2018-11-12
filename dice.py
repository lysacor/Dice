import random

RAN_NUM = int(random.randint(1, 6))

RESPONSE = 'true'

while RESPONSE == 'true':
    print(RAN_NUM)
    RESPONSE = RESPONSE.tolower(input("""Roll the dice again? (true/false)"""))
    if RESPONSE not in ('true', 'false'):
        RESPONSE = RESPONSE.tolower(input("""Input incorrect try again?
        (true/false)"""))
