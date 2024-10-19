# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44*1024*1024
pages = 100
strings = 50
symbols = 25
book_weight = (symbols*strings*pages)*4
print("Количество книг, помещающихся на дискету:", int(v/book_weight))
