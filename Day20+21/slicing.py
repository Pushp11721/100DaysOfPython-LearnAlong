piano_keys=['a','b','c','d','e','f','g']

for key in piano_keys[2:5]:
    print(key)#will print c,d,e

#reversing a string using slicing
reverse_keys=[]
for key in piano_keys[::-1]:
    reverse_keys.append(key)
print(reverse_keys)
