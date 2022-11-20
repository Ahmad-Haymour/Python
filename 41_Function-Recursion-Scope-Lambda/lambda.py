#------------------------------#
#   -- Function => Lambda --   #
#  -- Anonymous => Function -- #
#------------------------------#

#  [1]- It has on name
#  [2]- You can call it inline without defining it
#  [3]- You can use it in return Data from another function
#  [4]- Lambda used for siple functions and def handle the large Tasks
#  [5]- Lambda is one single Expression not Block of Code
#  [6]- Lambda Type is Function
#---------------------------------------------------------------------

def say_hello(name, age): return "Hello {}, you are {} Years Old".format(name, age) 

hello = lambda name : "Hello {}".format(name)

print(say_hello("Ahmad", 28))
print(hello('Sam'))
print('><'*40)

print(type(say_hello))          #   => Type Function
print(type(hello))
print(type(hello('Sam')))       #   => Type Function Return
print('><'*40)

print(say_hello.__name__)       #   => Name of Variable or Function
print(hello.__name__)