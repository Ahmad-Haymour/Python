# ------------------------
#      -- Numbers Converting --

#           1- int(number)
#           1- float(number)
#           1- complex(number)
#---------------------------------------------------------------#
#           a- You can Convert From Int to Float or Complex
#           b- You can Convert From Float to Int or Complex
#           c- You cannot Convert Complex to Any Type
# ------------------------

# Integer ( int )

print(100)
print(type(100))
print(type(-100))


# Float

print(2.15)
print(type(2.15))
print(type(-2.15))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))

print("#---------------------------------#")

print(int(20.1234))
print(type(int(20.1234)))

print(float(224))
print(type(float(224)))

print(complex(10.50))
print(type(complex(10.50)))

print(10+9j)
# print(int(10,9j))     # Error  => Cannot Convert Complex to any type

