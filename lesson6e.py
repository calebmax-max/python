# On the try and except block you run some codes and if it is successful the try block will get executed otherwise the except will be executed when there is an anticipated error.
try:
    number = 100 
    answer = number / 0

    print("The answer is: ",answer)

except Exception as e:
    print("There is an error")






