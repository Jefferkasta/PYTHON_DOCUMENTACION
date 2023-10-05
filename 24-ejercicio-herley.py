'''
0+1=1
1+1=2
2+1=3
3+2=5
5+3=8
8+5=13
13+8=21
21+13=34
'''
def fibonari(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
    return b
for x in range(5):
    print(fibonari(x))


        
        