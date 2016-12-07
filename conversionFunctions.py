import re

def sid_to_id( sid ):
    return (re.findall('\d+', sid )).pop()
print sid_to_id ('NEO4J:12345')