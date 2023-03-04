shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_before)
print(list_id_after)
print(list_id_before == list_id_after)

print('---')
tuple_ = [1, 2, 3, 4, 5, 6]
print(tuple_[:-1])
