st = input().lower().split()
res = {i : st.count(i) for i in set(st) if st.count(i)>1}
print('zawiera' if len(res) != 0 else 'nie zawiera')
