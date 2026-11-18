def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def multiply(a, b):
	return a*b

def divide(a, b):
	return a/b

def circleArea(r):
        if r >= 0:
                return 3.14 * r * r
        else:
                return "Error"

def main():
	result = 0.0
	while True:
		a = float(input("first number: "))
		b = float(input("second number: "))
		op = input("operator (choose between + - * /):")
		if op == "+":
			result = add(a, b)
			print("Result: ", result)
		elif op == "-":
			result = subtract(a, b)
			print("Result: ", result)
		elif op == "*":
			result = multiply(a, b)
			print("Result: ", result)
		elif op == "/":
			result = divide(a, b)
			print("Result: ", result)
		else:
			print("Unknown operator: ", op)
if __name__ == "__main__":
	main()
