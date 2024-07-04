#arithmetic operators, modulus, boolean, bodmass=pedmass

x = 8
y = 5
if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')
    
    
# operator precedence  bodmass=pedmass
x, y, t = 3, 4, 5,
print (x, y, t)

x= ((6 + 3) - (19 * 3))
print(x)

x= ((9 ** 3) - (3 * 3))
print(x)

x= (9 ** 3)
print(x)

x= ((2 + 3)**3/3)
print(x)

x=(6 + 3 - 6 - 3)
print(x)

x=((6 + 3) - (6 - 3))
print(x)



#identity operators e.g is
x = ('Tola')
y = ('bola')

if x is not y:
    print('x is not y')
else:
    print('x is y')


#bitwise ,
#membership operators in, no in

x = ("dog", "cat", "rat", "bat")  
print("dog" in x)


x = ("dog", "cat", "rat", "bat")  
print("goat" in x)
    
    
x = ("dog", "cat", "rat", "bat")  
print("goat" not in x)

x = ("dog", "cat", "rat", "bat")  
print("Rat" in x)

#assignment operators = +
# = , +,  +=, -=

x = 5
x += 3

print(x)

y = 5
y -= 3

print(y)
 
 
#sting concatunaton
some, another = "idowu", "alaba"
print(some + another)

# + is not to add but to join
instrument = "guitar"
begin_value, b_value, e_value  = instrument[:3], "b", instrument[-2:]
#guibar
print(begin_value)
print(b_value)
print(e_value)

new_instrument = begin_value + b_value + e_value
print(new_instrument)

#clss work
Misspelt_word = "Kristain"
correct, correct2 =  "Ch", "ia"
Correct_word = (correct + Misspelt_word[1:5] + correct2 + Misspelt_word[6:])
print(Correct_word)


#functions
para = "riuiyvgcjvhzskkkkkksssssssssssssssssss"
print(len(para))

#mehtods
r = "dfgvhbjnkjdjjjjjjjjdjdjjdjjddtp"
print(r.index('t'))

name = "Khristain"
name.replace("K", "C")
new_name = name.replace("K", "C")
print(new_name.replace("ai", "ia"))

#you can even replace with spoacve


happening = "They are playing songs outside"
print(len(happening.split()))


Essay = "hhhhhhhhhhhhhhhhhh hhhhhhhhhh u              u u  u u uu u  u "
amount_words = Essay.split()
Essay_count = (len(amount_words))
print("You have total number of ",Essay_count, "words" )

word = "They are playing songs outside "
total_words = word.split()
word_count = len(total_words)
print(f"In the essay the amount of words written are {word_count} in total")
print(word.replace(' ', ''))


# .capitalize only the first letter     .lower =converts all the letter to low .upper all converts to capital letter
kk = "kenny"
print(kk.capitalize())




"""trying to make a diamond"""



the_sign = "*"

for i in range(1, 21, 2):
    print((i * the_sign).center(42))
for i in range(21, 0, -2):
    print((i * the_sign).center(42))
    
    
    
the_sign = "*"

for i in range(4, 30, 6):
    print((i * the_sign).center(42))
for i in range(3, 0, -30):
    print((i * the_sign).center(42))
    
