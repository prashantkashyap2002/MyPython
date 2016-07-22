#!/usr/bin/python
def greet(name):
    """ This is greeting function"""
    print("Hello" + name + ". Good Morning!!!!")
    
print(greet(" PARTH "))

def sum_natural(num):
	if(num <=0):
		print("enter +ve num")
	else:
		i=0
		while(num>0):
			i+=num
			num = num-1
		return i

num = int(input("Input the number: "))
n = sum_natural(num)
print("sum of natural no " + str(num) + "=" + str(n))
