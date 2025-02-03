import sys

arguments = sys.argv

    
if not len(arguments) == 3 or int(arguments[2]) == 0 or int(arguments[1]) // int(arguments[2]) == 0:
    print("erreur.")

else:
    print(f"résultat : {int(arguments[1]) // int(arguments[2])}")
    print(f"reste: {int(arguments[1]) % int(arguments[2])}")

