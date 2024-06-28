print("Fashina Marvellous")
print("Sarah")
print("Kenny")
print("Timi")
print("oba")


length = 5
breath = 4
length = 90

area = length + breath
print(area)



a = 6
b = 10
h = 8
area = 1/2*(a+b)*h
print(area)

b = 5
h = 90
area = 1/2 * (b*h)
print(area)


a = 6
a = 100
b = 10
h = 8
area = 1/2*(a+b)*h
print(area)





#note for friday 28 of june 2024
#formula for compound interest 
#    A = P(1+r/100)t

#where A = final amount P = initaial principal balance r = interest n = number of times interest applied per time period t = number of times elapsed


principal = int(input("principal_amount"))
inputed_rate = int(input("interest rate"))
rate = float(inputed_rate/100)
time = float(input("time"))

amount = principal * (1 + rate)**time


print(amount)

sentence = "The dog is here"
name = sentence[4:7]
name = sentence[-11:-8]
print("and the " + name + " is bingo")

first_sentence = "I think i would love to be like Elon"
second_sentence = "not the elon at mushin, the main one, Musk"

first_name = first_sentence[32:36]
second_name = second_sentence[38:43]
print(f'the founder of tesla is {first_name} {second_name}')



sentence = 'the flash power is speed'
hero = sentence[4:9]
power = sentence[-6:]
print(f'the power of the {hero} are more than his {power}, it is his family and friends')



value_given =input('write a number') 
float = float(value_given)
str_convert_value = str(value_given)
integer_convert_value = int(str_convert_value)

print(float ,str_convert_value , integer_convert_value)

value_given =input('write a number') 
float = float(value_given)
str_convert_value = str(value_given)
integer_convert_value = int(str_convert_value)

print(float ,str_convert_value , integer_convert_value)


number = 23
print(number == 23)
print(number != 23)


number = 'jumping'
print(number)


student_score = 60 

print(student_score )

print(True and True)
print(False and False)
print(True and False)

print(True or False)
print(True or True)

print(True or False and True and False or True and True or False)




student_score = 60 

print(student_score >= 60 )


usernumber = int(input('enter a lucky number'))

if usernumber == 10:
    print('weldone you have been picked for the scholarship')
elif usernumber == 7:
    print('you cant use this number')
elif usernumber == 9:
    print('almost there')
    
else:
    print('eyah sorry for you oh ')
    





year_given = int(input('put your year of birth '))
age_required = 2024-year_given

if age_required >= 27:
    print('you are too old for this')
elif age_required >= 18:
    print('reistration is succsessful')
else:
    print('your age is too low for this registration, minimum of 18 years required')


