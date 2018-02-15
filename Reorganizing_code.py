"""
def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= [None, None, None, None, None]
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[1]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
"""
# Part 1 (Myself)

def check_answers_reduced(my_answers,option):
  return (my_answers == option)
def check_answers(my_answers,option):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= [None, None, None, None, None]
    a = range(0,5)
    for i in a:
        results[i] = check_answers_reduced(my_answers[i],option[i])
        #print (results[i])
    count_correct = 0
    count_incorrect = 5
    for result in results:
        if result == True:
            count_correct += 1
    count_incorrect -= count_correct
    #print(count_correct/5>0.7)
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored {} out of 5.".format(count_correct)
    else:
        return "Unfortunately, you did not pass. You scored {} out of 5.".format(count_correct)
my_answers = [1,1,1,0,0]
option = [0,0,0,0,0]
print(check_answers(my_answers,option))

# Part 2 (reviewed code)
def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    # Checks the five answers provided to a multiple choice quiz
    # and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    score_string = "You scored " + str(count_correct) + " out of 5."
    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test! " + score_string
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass. " + score_string
