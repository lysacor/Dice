import random

RESPONSE = 'true'

while RESPONSE == 'true':
    print(int(random.randint(1, 6)))
    RESPONSE = input("""Roll the dice again? (true/false)""")
    RESPONSE = RESPONSE.lower()
    FAILCHECK = 0
    if RESPONSE not in ('true', 'false'):
        while RESPONSE not in ('true', 'false'):
            RESPONSE = input("""Input incorrect try again? (true/false)""")
            RESPONSE = RESPONSE.lower()
