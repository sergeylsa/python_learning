#Задача: реализовать игру в загадки

#Требования:
#Программа выводить в консоль текст загадки и ждать ввода пользователя
#Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
#Загадок должно быть 10, тематика вопросов должна быть по первому занятию
#Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
#Программа должна не учитывать регистр ответа: "Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"

#1-st question
good_cnt = 0
bad_cnt = 0
q = input('Wich language we are learning?')
if q.lower() == 'python':
    print('Exellent, that is right')
    good_cnt += 1
else:
    print('Wrong, try again!!!')
    q = input('Second attempt, input answer:') 
    if q.lower() == 'python':
        print('That is right')
        good_cnt += 1
    else:
        print('That is wrong answer')
        bad_cnt += 1
print('----------------------------')
#2-st question
q = input('Python interpreted or compiled language?')
if q.lower() == 'interpreted':
    print('Exellent, that is right')
    good_cnt += 1 
else:
    print('Wrong, try again!!!')
    q = input('Second attempt, input answer:') 
    if q.lower() == 'interpreted':
        print('That is right')
        good_cnt += 1
    else:
        print('That is wrong answer')
        bad_cnt += 1  
print('----------------------------')
#3-st question
q = input('In python  is all object(yes/no)?')
if q.lower() == 'yes':
    print('Exellent, that is right')
    good_cnt += 1 
else:
    print('Wrong, try again!!!')
    q = input('Second attempt, input answer:') 
    if q.lower() == 'yes':
        print('That is right')
        good_cnt += 1
    else:
        print('That is wrong answer')
        bad_cnt += 1            
print('----------------------------')
print('')        
print('End test')
print('---------------------')
print('Total questions was 3!')
print('Result:')
print('Correct answer = {}'.format(good_cnt))
print('Wrong answer = {}'.format(bad_cnt)) 
print('---------------------')
