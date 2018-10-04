
def main():
	print("Enter the negative integer Dividend")
	dividend = int(input())
	print("Enter the Divisor")
	divisor = int(input())
	if(dividend >= 0):
		print("Lol, enter negative integer")
		main()
	else:
		negative_division(dividend, divisor)


def negative_division(dividend, divisor):
	dividend1 = abs(dividend)
	remainder = dividend1 % divisor
	quoient = int(dividend1 / divisor)
	if (remainder > 0):
		quoient = -1 - quoient
		remainder = divisor - remainder
	else:
		quoient = -quoient
		remainder = 0
	print("Quoient is ",quoient)
	print("Remainder is ",remainder)

if __name__ == '__main__':
	main()
