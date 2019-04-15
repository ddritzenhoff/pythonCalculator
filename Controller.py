# Dominik Ritzenoff
# 4/14/19
""" This is a calculator program that I made to improve my python skills a bit and to see how I should organize my code.
I have commented out the print function that would actually print out the correct number."""

class Calculator:

	# This function is called when an object of the Calculator class is created.
	def __init__(self):
		# Declaring the three variables in this program.
		self.firstNumber = None
		self.secondNumber = None
		self.finalNumber = None

	# Main method. This is simply responsible for assigning the variables values.
	def main(self):
		print("\n\nWelcome to Dominik's Calculator!")
		print("\nFirst, I need your first input number:")
		self.firstNumber = self.intChecker()
		print("Next, I need your second input number")
		self.secondNumber = self.intChecker()
		print("Please enter an operator. This could be '*', '+', '-', or '/'")
		self.finalNumber = self.operationChecker(self.firstNumber, self.secondNumber)
		print(self.finalNumber)

	# This is almost like a super class for the operation method. Until a valid input argument is given, it loops.
	def operationChecker(self, num1, num2):
		# Calling the operation method.
		finalNum = self.operation(num1, num2)
		# Checking to see if the type is integer or not. If not, the while loop is entered. Keep going until a valid
		# input argument is given.
		while type(finalNum) is not int:
			print("God damn, trying to break my game again. Enter something legitimate")
			finalNum = self.operation(num1, num2)
		return finalNum

	# I used the closest thing to a switch case in Python because, well, I like switch cases.
	def operation(self, num1, num2):

		print("Enter the operator that you desire.")
		# Taking an input.
		operator = input()
		# Checking to see if the input is one of the four cases as mentioned below.
		operationChecker = {
			'*': num1 * num2,
			'+': num1 + num2,
			'-': num1 - num2,
			'/': num1 / num2
		}
		return operationChecker.get(operator, "error")

	# This method is much like the operationChecker method. Loops if the wrong input is given.
	def intChecker(self):
		numberInput = input()
		isInt = self.isValidNumber(numberInput)
		while not isInt:
			isInt, numberInput = self.forceInteger()

		# Now there is a very small chance that this can crash.
		return int(numberInput)

	# This method is responsible for forcing the user to input an integer.
	def forceInteger(self):
		print("Please stop trying to break the game and enter an int")
		newInt = input()
		newInt_isInt = self.isValidNumber(newInt)
		if newInt_isInt:
			return True, newInt
		return False, -1

	# This method is responsible for checking if the number input is valid.
	def isValidNumber(self, maybeNumber):
		isValid = None
		try:
			testNumber = int(maybeNumber)
			if type(testNumber) is int:
				isValid = True
		except ValueError:
			isValid = False
		return isValid


# If this python file is called, create an object of the calculator class and call the main method.
if __name__ == "__main__":
	operation = Calculator()
	operation.main()

