import sys
import requests
from datetime import datetime

# need to get this from the webpage
SESSION = '53616c7465645f5f617ba5f45c890a48f31105b2baef2958f5476c4103ba9afc21a6aa3007878a56220a5938a5f2d6ed'
# defaults
day = datetime.now().day
year = datetime.now().year
if not(len(sys.argv) == 1):
    params = sys.argv[1:]
    if len(params) == 1:
        day = params[0]
    elif len(params) == 2:
        day = params[0]
        year = params[1]
    else:
        raise RuntimeError('Must run in form\npython get_input.py > file\nOR\n python get_input.py <day>\nOR\npython get_input.py <day> <year>')

#  print(day, year)
webpage = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session' : SESSION})
print(webpage.text)
#  with open(f'{day}.in', 'w') as f:
    #  f.write(webpage.text)

