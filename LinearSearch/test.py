from linear_search import LinearSearch

ls = LinearSearch()

ls.set_array([1, 2, 3, 4, 5, 6])
ls.set_target(5)

print(ls.linear_search())
print(ls.linear_search_recursive())

