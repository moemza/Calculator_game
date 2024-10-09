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
def gameplay():
    operator = input("Please choose an operator: ")
      
    score = 0
    for i in range(5):
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10) 
        print(f"{num1} {operator} {num2}")
        answer = input("Enter your answer:")
        if answer == (operations(operator,num1,num2)):
            score += 1
    return score

print(gameplay())