def compute(n):
    ctr,i=0,5
    while (n/i)>=1:
        ctr+=n//i;
        i*=5
    return ctr


def func():
    n=int(input())
    print(compute(n))

func()










