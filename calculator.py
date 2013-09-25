from arithmetic import *

def main():
    #Get a command from the user - DONE
    #tokenize the command - DONE
    #check for a quit
    #if no quit, check for operation
    #check numbers

    while True:
        input = raw_input("> ")
        tokens = input.split(" ")
        
        if tokens[0] == "q":
            break
        else:
            if tokens[0] == "+":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print add(tokens[1], tokens[2])

            elif tokens[0] == "-":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print subtract(tokens[1], tokens[2])

            elif tokens[0] == "*":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print multiply(tokens[1], tokens[2])

            elif tokens[0] == "/":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print divide(tokens[1], tokens[2])

            elif tokens[0] == "square":
                tokens[1] = int(tokens[1])
                print square(tokens[1])

            elif tokens[0] == "cube":
                tokens[1] = int(tokens[1])
                print cube(tokens[1])

            elif tokens[0] == "pow":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print power(tokens[1], tokens[2])

            elif tokens[0] == "mod":
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                print mod(tokens[1], tokens[2])
                
            else:
                print "Invalid calculator command."

main()
