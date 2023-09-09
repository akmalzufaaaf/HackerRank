a = input().split()
b = input().split()
c = input().split()
d = input().split()
e = input().split()

atribut = ['nama', 'hari', 'bulan']

coll_a = dict(zip(atribut, a))
coll_b = dict(zip(atribut, b))
coll_c = dict(zip(atribut, c))
coll_d = dict(zip(atribut, d))
coll_e = dict(zip(atribut, e))

col = [coll_a] + [coll_b] + [coll_c] + [coll_d] + [coll_e]

def sortir(elem):
    bulan = int(elem['bulan'])
    return bulan

col.sort(key=sortir)
print(col[2]['nama'].lower())