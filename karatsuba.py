import math
def karatsuba(num1,num2):
	if(int(num1)<10 or int(num2)<10):
		print ("in recursive if if: numbers received are : ",num1,num2)
		
		print ("in  recursice if returnjing the pproduct: ",int(num1)*int(num2))
		return int(num1)*int(num2)

	num1 = str(num1)
	num2 = str(num2)

	print "in recursive call ------------------------------------"
	print "numbers received are ",
	print (num1,num2)

	print (max(len(num1),len(num2)))//2
	maxLength =math.ceil( max(len(num1),len(num2))/2)
	print maxLength
	maxLength = int(maxLength)
	print ("numbers to be split at :   ", maxLength)	
	high1,low1 = num1[:maxLength],num1[maxLength:]
	print (high1,low1)
        	
	high2,low2 = num2[:maxLength],num2[maxLength:]
	print (high2,low2)
	z2 = karatsuba(int(high1),int(high2))
	print (z2)
	z1 = karatsuba(int(high1)+int(low1),int(high2)+int(low2))
	print (z1)	
	z0 = karatsuba(int(low1),int(low2))
	print (z0)
	print (maxLength,)
	y = 0
	y = z2 * (10**(2*maxLength))
	print y
	y = y + z0
	print y
	y = y+ (z1-z0-z2)*(10**maxLength)
	print y
	print ("returning from recursive call : ",y)
	
	return y





if __name__ == "__main__":
	a = 100
	b = 10
	print karatsuba(a,b)
