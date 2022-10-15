#arthematic operators

print(10*20) #multipication
print(20/10) #division
print(20%10) #modulus
print(15//2)#floor division (7.5 but still rounds the nearest whole number)
print(15//4)

#assignment operators

a = 20
a += 5 # it is same as a = a + 5
print(a)

a -= 5 #same as a = a-5
print(a)
a *= 6 #same as a = a*6
print(a)
a /= 5 #same as a = a/5
print(a)

print(3**2) #3*3*3
print(3**4) #3*3*3*3*3

a %= 5 # same as a =a%5 remainder)
print(a)
a //=3 #same as a = a//3
print(a)
print(3==5)#== for equal = is for assigning

print(3!=4)# not equal
print(3>4)
print(3<4)
print(3>=4)#greater than equal
print(3<=4)#less than equal


#logical operators

x = 2

print(x < 5 and x < 8) #return true of both statements are true

print(x<5 or x>8) #return true if anyone of the condition is met

print(x > 3 or x > 10)

print(not(x<5 and x<8)) #it reverses the result for example if the result is true it will return false and vice versa


#identity operators

a =[10,20]
b =[10,20]
c=a
c=b# here last given string is considered
a.remove(20)
print(a)
print(a is c) #return true if both the variables are same object pointing to the same memory location
print(b is c)#it 