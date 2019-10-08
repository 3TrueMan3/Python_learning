import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b([aA])+\b', 'argh', line, count=1, flags=re.IGNORECASE))
