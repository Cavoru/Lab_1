# TODO Найдите количество книг, которое можно разместить на дискете

V_DISK = 1.44
N_LETTERS = 100
N_STR = 50
N_SIM = 25
V_ONE_BITS = 4

v_book_bits = N_SIM * N_STR * N_LETTERS * V_ONE_BITS
v_book_kb = v_book_bits / 1024
v_book_mb = v_book_kb / 1024

count = int(V_DISK // v_book_mb)

print("Количество книг, помещающихся на дискету:", count)
