def valeur_entrente():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


def Operation():
    operation_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez l'operation (+, -, *, /) : ")  
        if operation in operation_valides:
            return operation
        else:
            print("Erreur : Opération non valide. veuillez entrer une operation valide.")   


def calcule(nombre1, nombre2, operation):
        if operation == '+':
            return nombre1 + nombre2
        elif operation == '-':
            return nombre1 - nombre2
        elif operation == '*':
            return nombre1 * nombre2
        elif operation == '/':
              if nombre2 != 0:
                return nombre1 / nombre2
              else:
                print("Erreur : Division par zéro.")
                return None
                         
def calculatrice():
    nombre1 = valeur_entrente()
    nombre2 = valeur_entrente()
    operation = Operation()
     
    resultat = calcule(nombre1, nombre2, operation)

    if resultat is not None:
        print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}.")


calculatrice()