import re

string1 = 'hello 234 python'

# print(string1.find('2'))
# print(string1.startswith('python'))

pa = re.compile(r'hello', re.IGNORECASE)
b = pa.match(string1)
# print(b)
ma = re.match(r'[A-Z][a-z]*\s[0-9]*\s\D*', 'Azdf 30 /root')
print(ma.group())
