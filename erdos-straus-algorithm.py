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
#aは4/nをどのくらい倍数に分解して考えるか？
#ve,ve1,ve2はそれぞれx,y,zの数値となる。
#無作為にxyzの値を記録していく。
#生成された全ての組み合わせを、(1 / n) * 4 == (1 / x) + (1 / y) + (1 / z)の公式に合致するか検証する。 


for n in range(2,100):
    for a in range(1,50):
        for aa2 in range(1,50):
            for aaa in range(1,50):
                solve.append(n)

                solve.append(int(a))
                solve.append(int(aa2))
                solve.append(int(aaa))
                aa = solve.copy()
                solves.append(solve)
                solve = []



for i in solves:
    n = i[0]
    x = Fraction(1,i[1])
    y = Fraction(1,i[2])
    z = Fraction(1,i[3])
    yoi1 = Fraction(4,n)
    a = yoi1
    b = x + y + z
    if a == b:
        print('n='+str(n)+', x='+str(x)+', y='+str(y)+', z='+str(z))
