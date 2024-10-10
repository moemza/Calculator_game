import random
list_operator = ["/", "*", "+", "-"]
def operations(operator, num1, num2):
    
    if operator in list_operator:
        
        if operator == "/":
            return num1/num2
        elif operator == "*":
            return num1 * num2
        elif operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
    else:
        return None
    
def equations():
    score = 0
    for i in range(5):
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
        operator = random.choice(list_operator)
        solution = (operations(operator,num1,num2)) 
        print(f"{num1} {operator} {num2}")
        try:
            answer = float(input("Enter your answer:"))
        except:
            print("Wrong input, try next question")
            answer = (operations(operator,num2,num1))
        if answer == solution:
            score += 1
    return score
def gameplay():
    print("Welcome to calculator game")
    score = equations()
    print(f"Your score is : {score}")
    if score >= 4:
        return "Nice one!!"
    elif score >=2:
        return "Nice try!!"
    else:
        return "Try again!!"
    

print(gameplay())