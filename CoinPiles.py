def func(a,b):
    if a<b:
        b,a=a,b;
    if a>2*b:
        print("NO")
        return
    if (a+b)%3==0:
        print("YES")
    else:
        print("NO");

def f():
    t=int(input())

    l=[[int(i) for i in input().split()] for j in range(t)]
    for data in l:
        func(data[0],data[1])

f()