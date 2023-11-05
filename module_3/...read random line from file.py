#

import random

def random_line(f_name):
    line = open(f_name).read().splitlines()
    return random.choice(line)

print(random_line('theory 2.txt'))