import random
newlist = []
def validation(text):
    if text.lower() == "стоп" or text.lower() == "stop":
        print("Програма завершена.")
        return False
    return True


while True:
    text = input("Напиши що робити в інфінітиві: ")
    if not validation(text):
        break
    newlist.append(text)

print(f"СЬогодні ти будеш:  {random.choice(newlist)}")
if input() == "пака":
    print("пака")
#--------------------------------------------------------
#conflict solving 
# fr0wofjeiorjejfroierjoreji master branch 
