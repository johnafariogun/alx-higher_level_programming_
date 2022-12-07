def search_replace(my_list, search, replace):
    new = my_list[:]
    new[:] = [replace if search == i else i for i in my_list]
    return new
