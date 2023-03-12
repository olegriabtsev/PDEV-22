this_list = ["apple1", "banana", "cherry", "orange", "kiwi", "mango"]
for i in range(len(this_list)):
    print(this_list[i])
print('---')
this_list = ["apple2", "banana", "cherry", "orange", "kiwi", "mango"]
for j in this_list:
    print(j)
print('---')
this_list = ["apple3", "banana", "cherry", "orange", "kiwi", "mango"]
i = 0
while i < len(this_list):
    print(this_list[i])
    i += 1  # i = i +1
print('---')
this_list = ["apple4", "banana", "cherry", "orange", "kiwi", "mango"]
[print(x) for x in this_list]
