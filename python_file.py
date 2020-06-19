ANTLR runtime and generated code versions disagree: 4.8!=4.7.2
ANTLR runtime and generated code versions disagree: 4.8!=4.7.2
num2 = 51 

tablica1 = ["a","b","c"] 

def fun1(i,s):
	nazwa = s
	print(nazwa)
	num2 = i + 1
	return num2

def fun2(a,b):
	if a < b:
		return "1"
	elif b == a:
		return "2"
	else:
		return "3"


def fun3():
	for i in range(0,5):
		print(i)


def fun4():
	x = 0
	while x < 10:
		print(x)
		x = x + 1


def main(): 
	num1 = 68
	nazwa1 = fun2(3,5)
	print(nazwa1)
	fun3()
	num1 += 1


if __name__ == '__main__':
	main()
