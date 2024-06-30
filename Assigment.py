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
