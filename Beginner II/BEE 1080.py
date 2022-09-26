li = []
for i in range(0, 100):
    li.append(int(input()))
print(f"""{max(li)}
{li.index(max(li))+1}""")
