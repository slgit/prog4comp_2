def ask_user(a, b):
    """get answer from user: a*b = ?"""
    question = '{:d} * {:d} = '.format(a, b)
    answer = int(input(question))    
    return answer
    
def points(a, b, answer_given):    
    """Check answer. Correct: 1 point, else 0"""
    true_answer = a*b        
    if answer_given == true_answer:
        print('Correct!')
        return 1
    else:
        print('Sorry! Correct answer was: {:d}'.format(true_answer))
        return 0
    
print('\n*** Welcome to the times tables test! ***\
       \n          (To stop: ctrl-c)')

# Ask user for a*b, ... a, b are in [1, N]
N = 2
score = 0    
for i in range(1, N+1, 1):
    for j in range(1, N+1, 1):
        user_answer = ask_user(i, j)  
        score = score + points(i, j, user_answer)
        print('Your score is now: {:d}'.format(score))
            
print('\nFinished! \nYour final score: {:d}   (max: {:d})'\
      .format(score, N*N))