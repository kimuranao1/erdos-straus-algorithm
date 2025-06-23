from fractions import Fraction

#a = (1 / n) * 4
#b = (1 / x) + (1 / y) + (1 / z) 

d = 0
nn = 0
sol = 0
sol2 = []
solve = []
aa = []
solves = []
#nはnの値
#aは分母をどのくらい分解して考えるか？
for n in range(2,200):
    for a in range(1,200):
        d = n*a
        nn = 4*a
        sol3 = nn
        



        for i in range(1,sol3):
                ve = sol3 / i
                vv = sol3 - i
                ve = float(ve)
                vv = float(vv)

                if ve.is_integer() and vv.is_integer():
                    for k in range(1,(sol3-i)):
                        ve1 = sol3 / k
                        ve1 = float(ve1)
                        if ve1.is_integer():
                                ve2 = sol3 - i - k
                                ve2 = float(ve2)
                                if ve2.is_integer():
                                        solve.append(n)

                                        solve.append(ve)
                                        solve.append(ve1)
                                        solve.append(ve2)
                                        aa = solve.copy()
                                        solves.append(solve)
                                        solve = []



for i in solves:
    n = int(i[0])
    x = Fraction(1,int(i[1]))
    y = Fraction(1,int(i[2]))
    z = Fraction(1,int(i[3]))
    yoi1 = Fraction(4,n)
    a = yoi1
    b = x + y + z
    if a == b:
        print('n='+str(n)+', x='+str(x)+', y='+str(y)+', z='+str(z))
