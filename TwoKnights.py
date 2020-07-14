'''
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints
1≤n≤10000
Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848
'''

def sq(i):
	return i*i

def func():
	n=int(input())
	for i in range(1,n+1):
		res=((sq(i)*(sq(i)-1)//2)-(8*(i-2)*(i-1)//2))
		print(res)
		
func()
