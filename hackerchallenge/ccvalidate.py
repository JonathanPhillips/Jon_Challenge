import re

pattern = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}$').match
repeated = re.compile(r'(\d)\1{3,}').search
validated = re.compile(r'^([4-6]\d{15})').match

for _ in range(int(input())):
    cards = input()
    if pattern(cards):
        cards = cards.replace('-','')
    if validated(cards) and not repeated(cards): 
        print("Valid")
    else:
        print("Invalid")
