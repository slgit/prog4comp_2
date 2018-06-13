def ask_user(a, b):                                 # preliminary
    """get answer from user: a*b = ?"""
    print('{:d}*{:d} = '.format(a, b))      
    return a*b                     

def points(a, b, answer_given):                     # preliminary
    """Check answer. Correct: 1 point, else 0"""
    print('{:d}*{:d} = {:d}'.format(a, b, a*b))      
    return 1
    
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

