import random
#Открытие текстового файла для записи оценок
user_ball = open('user_ball', 'w')

summa_balls = 0
while True:
    #Получение случайного номера задачи
    num_task= random.randrange(1,11)

    #Считывание текста задачи из текстового файла
    with open("tasks1.txt",  encoding="utf8") as file_task:
        for i in range(1, num_task*2+1):
            line = file_task.readline()
    print('№'+str(num_task))    
    print(line, end="")


    #Считывание текста ответа из текстового файла

    with open("answer.txt",  encoding="utf8") as file_answer:
        for i in range(1, num_task*2+1):
            answer_task = file_answer.readline()

            
    #Обработка ответа ученика
    print('Введите ваш ответ: ')
    user_answer = input()

    user_ball.write('task #' + str(num_task)+',  ball = ')
    if (float(answer_task) == float(user_answer)):
        ball = 1;
    else:
        ball = 0;
        
    summa_balls +=ball
    user_ball.write(str(ball)+ '\n')    

    user_ball.writelines('answer_task: '+ answer_task)
    user_ball.writelines('user_answer: '+ user_answer+ '\n\n')
    
    print('Продолжим решать задачи (Y/N): ')
    reply = input()
    if (reply == 'N'):
        break
    
user_ball.writelines('\nTotal balls: '+ str(summa_balls)+ '\n')   
 
file_task.close()   
file_answer.close()
user_ball.close()
