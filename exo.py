import sys

arguments = sys.argv

if len(arguments) == 3 and int(arguments[2]) != 0 and int(arguments[1]) // int(arguments[2]) != 0:
        print(f"résultat : {int(arguments[1]) // int(arguments[2])}")
        print(f"reste: {int(arguments[1]) % int(arguments[2])}")
        exit()

print("erreur.")
        

