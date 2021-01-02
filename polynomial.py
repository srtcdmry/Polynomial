#p1 = w1_0*x^0 + w_23*x^23 + w_46*x^46 + w_1001*x^1001
#p2 = W2_0*x^0 + w_55*x^55 + w_1002*x^1002

p1katsayi   = [7,8,6,5,0] 
print("1.polinom katsayi: ",p1katsayi)
p1us =        [0,1,2,3,5]
print("1.polinom us: ",p1us)
p2katsayi =   [1,2,3,5,1]  
print("2.polinom katsayi:",p2katsayi)
p2us =        [0,1,2,4,5]  
print("2.polinom us:",p2us)

#  degısken katsayıları ve değiken us sayıları esleniyor tek listede 
def merge(list1, list2): 
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 
h1 = merge(p1katsayi,p1us)
print("1.Polınom ve usleri:",h1)                 
h2 = merge(p2katsayi,p2us)
print("2.polınom ve usleri ",h2)            



import collections

def addpoly(p, q):
    # r itere edilebilir bir nesne oluyor 
    r = collections.Counter()
    # p ile q toplanıyor ve yeni bir listeye ekleniyor
    for coeff, exp in (p + q):
        r[exp] += coeff
    #eklenen yeni ve son listede diğer fonksiyona gidiyor 
    return counter_to_poly(r)

def subpoly(p, q):
    # r itere edilebilir bir nesne oluyor 
    r = collections.Counter()
    # p ile q toplanıyor ve yeni bir listeye ekleniyor
    for coeff, exp in (p+q ):
        # counter sayıcına ekklıyoruz
        r[exp] += coeff
        #print(r)
        # eger deger sayıcı ıcınde varsa degeri yanı jatsayıyı cıkarıyoruz
        if coeff in r :       
            r[exp] -= 2*coeff
            #print(r)
    return counter_to_poly(r)

def counter_to_poly(c):
    p = [(coeff,exp) for exp, coeff in c.items() if coeff != 0]
    p.sort(key = lambda pair: pair[1], reverse = True)
    return p
   # print(r)
    #eklenen yeni ve son listede diğer fonksiyona gidiyor 
print("h1 + h1 = ", addpoly(h1,h2))
print("h1 - h1 = ", subpoly(h1,h2))  
