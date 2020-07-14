
def f(n):
	return (n*(n+1))//2


def func():
	n=int(input())
	a=set()
	b=set()
	if f(n)%2!=0:
		print("NO")
	else:
		print("YES")
		asum,bsum=0,0
		for i in range(n,0,-1):
			if asum>bsum:
				b.add(i)
				bsum+=i
			else:
				a.add(i)
				asum+=i
		print(len(a),*a,len(b),*b)
		
func()

			
		
		



