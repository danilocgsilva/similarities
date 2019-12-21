import sys
from Compare import Compare

compare = Compare()

try:
    value1 = sys.argv[1]
    value2 = sys.argv[2]
    valueReturned = compare.compare(value1, value2)
    print(str(valueReturned))
except IndexError as ie:
    print("Forgot terms to compare!")
