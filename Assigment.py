a = 6
a = 100
b = 10
h = 8
area = 1/2*(a+b)*h
print(area)





#Folade is a student that offers 10 courses, at the end of the semster are scores are below
#input scores  wrtie a program to calculate her standing in the class 70 above A,60-69 B, 50-59 C, 40-49 D, 30-39 E, 29-0 F

score_for_maths = int(input('Please input the score for maths'))
score_for_english = int('input(Please input the score for english'))
score_for_chemistry = int('input(Please input the score for chemistry'))
score_for_biology = int(input('Please input the score for biology'))
score_for_agric = int(input('Please input the score for agric'))
score_for_physics = int(input('Please input the score for physics'))
score_for_economics = int(input('Please input the score for economics'))
score_for_civic = int(input('Please input the score for civic'))
score_for_crk = int(input('Please input the score for crk'))
score_for_history = int(input('Please input the score for history'))
score_for_bookkeeping = int(input('Please input the score for bookkeeping'))

each_scores = (score_for_agric + score_for_biology + score_for_bookkeeping + score_for_chemistry + score_for_civic + score_for_crk + score_for_economics + score_for_english + score_for_history + score_for_maths + score_for_physics)/100

if each_scores > 100:
    print('the number is above the score range reqiured')
else each_scores <0:
    print('number too low')


#a super store makes sales of five goods television, freezers, phones, indomie, rice
cost_price

#phones, freezer, television, Air conditioner, batteries

cost_price_of_phone = 72000
cost_price_of_freezer = 150000
cost_price_of_television = 120000
cost_price_of_Air_conditioner = 500000
cost_price_of_battery = 200000

selling_price_of_phone = int(input('Cost price of phone = 72000 What is your selling price'))
selling_price_of_frezzer=int(input('Cost Cost price of freezer = 150000 What is your selling price '))
selling_price_of_television = int(input('Cost price of television = 120000 What is your selling price'))
selling_price_of_Air_conditioner = int(input('Cost price of Air conditioner = 500000 What is your selling price'))
selling_price_of_battery = int(input('Cost price of battery = 200000 What is your selling price'))


total_selling_price = [selling_price_of_phone + selling_price_of_frezzer + selling_price_of_television + selling_price_of_Air_conditioner + selling_price_of_battery ]

total_cost_price = [cost_price_of_phone + 
cost_price_of_freezer + cost_price_of_television + cost_price_of_Air_conditioner + 
cost_price_of_battery]







if total_selling_price > total_cost_price:
	print('You have made profit of ', total_selling_price - total_cost_price)
elif total_selling_price < total_cost_price:
	print('You have made a loss of ', total_cost_price - total_selling_price)






