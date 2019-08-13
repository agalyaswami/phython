from collections import OrderedDict

ans = {}

words = int(input("Enter a sentence: ")).split()
unique_words = set(words)

for item in unique_words:
    ans[item] = words.count(item)

od = OrderedDict(sorted(ans.items(), key=lambda e:e[0]))

for item in od.items():
    print ("%s:%d" % (item[0],item[1]))
