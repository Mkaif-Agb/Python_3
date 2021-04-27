from collections import Counter

l = {1,2,1,4,5,235,46,4,6,45,3256,2,5,1,2,1,1,21,5,5,5,6}
print(Counter(l))


m =  "asdsdgfdfhfgdhfgjfghsfdgsddfasweryterhdffb"
print(Counter(m))

n = "How many times does the word word show up using counter from collections"
word = n.split()
print(Counter(word))

c = Counter(word)
print(c.most_common(2))

print(c.values())
print(sum(c.values()))


