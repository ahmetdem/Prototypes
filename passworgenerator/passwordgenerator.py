import random
import string

letters = string.punctuation + string.ascii_letters + string.digits

result = ""

for i in range(12):
    rNumber = random.randrange( len(letters) )
    result += letters[rNumber]
    
print(result)