from time import sleep 

y  = []


def Counter():
	Counter = 0
	while True:
		print(Counter)
		Counter += 1
		yield


def Printer():
	Counter = 0
	while True:
		if Counter % 3 == 0:
			print('Yes')
		Counter += 1
		yield
		 

def main():
	while True:
		x = y.pop(0)
		next(x)
		y.append(x)
		sleep(1)

if __name__ == '__main__':
	x1 = Counter()
	y.append(x1)
	x2 = Printer()
	y.append(x2)
	main()