#!/usr/bin/python
def greet(name):
    """ This is greeting function"""
    print("Hello" + name + ". Good Morning!!!!")
    

def sum_natural(num):
	if(num <=0):
		print("enter +ve num")
	else:
		i=0
		while(num>0):
			i+=num
			num = num-1
		return i
def var_arg_func(arg1, *vartuple):
	print arg1
	for var in vartuple:
		print var
	return
def default_func(name, age = 30):
	print ("name = " + name + ", age = " + str(age))

print(greet(" PARTH "))
num = int(input("Input the number: "))
n = sum_natural(num)
print("sum of natural no " + str(num) + "=" + str(n))
var_arg_func(n)
var_arg_func(n,num)
default_func("Novita")
default_func("Soniyo", 20)

