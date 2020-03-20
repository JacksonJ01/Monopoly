lists = [[], [], [], [], []]

this = 0
for list in lists:
    list.insert([this][0], this)
    this += 1

print(lists)

this = 0
that = 1
for list in lists:
    lists[this].append(that)
    this += 1
    that += 1

print(lists)


lists.remove()
print(lists)


lists[3].remove(5)
print(lists)
