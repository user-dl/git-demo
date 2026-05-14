# def write1():
#     x = input("Напиши що робити в інфінітиві: ")
#     newlist = []
#     if x.lower() == "стоп" or x.lower() == "stop":
#         print("Програма завершена.")
#         return newlist
#     else:
#         newlist.append(x)
#         write1()
    #testcommit
# print(write1())
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

print(newlist)
