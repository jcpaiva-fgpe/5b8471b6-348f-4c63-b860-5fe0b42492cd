li = input().split() 
d = {x : li.count(x) for x in li}
print(max(d, key = d.get))
