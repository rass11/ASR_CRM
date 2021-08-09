from itertools import combinations_with_replacement as comb, product



l = ['2020-01', '2020-02', '2020-03', '2020-04','2020-05',
     '2020-06', '2020-07', '2020-08','2020-09', '2020-10', '2020-11', '2020-12']
#print((comb(l, 3)))
print(list(product(l, repeat=2)))