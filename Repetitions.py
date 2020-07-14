'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
'''

def func():
	s=input()
	res,curr=0,1
	for i in range(1,len(s)):
		if(s[i]==s[i-1]):
			curr+=1
		else:
			res=max(res,curr)
			curr=1
	res=max(res,curr)
	print(res)
		
		
func()
