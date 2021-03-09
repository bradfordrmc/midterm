def solvepi(i):  #function to solve for pi with i as arguement recieved
    x =1.0 # setting a variable for the function
    pi = 0.0 #intializing vairable pi for the function as a float
    for n in range(i): #for loop using i as the number of iterations
        pi += 4/(n*2+1)*x # main math solving for our pi variable where n equals the number of the iteration
        x *= -1 #math using our x variable
    return pi #returns pi each loop

print("Enter value for N") #asks user for n value
print(solvepi(int(input())))#takes user input for use in function