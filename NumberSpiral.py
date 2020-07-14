'''
A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints
1≤t≤105
1≤y,x≤109
Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15
'''

def func():
	t=int(input())
	
	l=[[int(i) for i in input().split()] for j in range(t)]
	
	
	for i in range(t):
		y,x=l[i][0],l[i][1]
		
		if x>y:
			if x%2==1:
				print(x*x-y+1)
			else:
				x-=1
				print(x*x+y)
		else:
			if y%2==0:
				print(y*y-x+1)
			else:
				y-=1
				print(y*y+x)
		
func()
