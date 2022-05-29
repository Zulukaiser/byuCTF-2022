#!/usr/bin/env python3

import string
import random
#import pyfiglet
from pathlib import Path
import os

s = 'abcdefg'
new_string = ''
for char in s:
	new_string += random.choice(string.ascii_lowercase + string.digits+"_")

print(new_string)