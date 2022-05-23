chemin = r"F:\ESGI\Python\Liste_de_Course\liste.txt"

print("\n###############\tBienvenue sur votre liste de courses en ligne.\t###############\n")

def menu():
  print("1. Ajouter un element dans votre liste.")
  print("2. Retirer une element de votre liste.")
  print("3. Afficher les elements de votre liste.")
  print("4. Vider le contenu de votre liste.")
  print("5. Quitter le programme.\n")

def choice1():
  if int(user_choice) == 1:
    with open(chemin, "r", encoding="utf-8") as f:
      lines = f.read().splitlines()
      print(f"Voici votre liste de course: {lines}")
      add = input("Que souhaitez vous ajouter à la liste ?: ")

    while add.lower() in lines:
      print("\nCette article est deja present dans votre liste")
      add = input("Que souhaitez vous ajouter à la liste ?: ")
    else:
      with open(chemin, "a", encoding="utf-8") as f:
        f.write(add.lower() + "\n")
        print(f"\nL'article '{add}' est bien ajouté à votre liste !")

def choice2():
  if int(user_choice) == 2:
    with open(chemin, "r", encoding="utf-8") as f:
      lines = f.read().splitlines()
      print(f"Voici votre liste de course: {lines}")
      rm = input("Que souhaitez vous retirer de votre liste ?: ")

    while rm.lower() not in lines:
      print("\nCette article n'est pas present dans votre liste")
      print(f"Voici votre liste de course: {lines}")
      rm = input("Que souhaitez vous retirer de votre liste ?: ")
    else:
      with open(chemin, "w", encoding="utf-8") as f:
        index = lines.index(rm.lower())
        lines.remove(lines[index])
        result = "\n".join(lines)
        f.write(result)
        print(f"\nL'article '{rm}' est bien retiré de votre liste !")

def choice3():
  if int(user_choice) == 3:
    with open(chemin, "r", encoding="utf-8") as f:
      lines = f.read().splitlines()
      print(lines)

def choice4():
  if int(user_choice) == 4:
    with open(chemin, "w", encoding="utf-8") as f:
      f.write("")

def choice5():
  if int(user_choice) == 5:
    print(exit())



while True:
  menu()

  user_choice = input("Que souhaitez vous faire ?: ")

  while user_choice.isdigit() == False or int(user_choice) <= 0 or int(user_choice) > 5:
    print("Veuillez rentrer une valeur valide !")
    user_choice = input("Que souhaitez vous faire ?: ")

  choice1()
  choice2()
  choice3()
  choice4()
  choice5()

  repeat = input("\nSouhaitez vous effectuer d'autres changements ?: \nOui: 0\nNon: 1\nVotre saisie: ")
  while repeat.isdigit() == False or int(repeat) != 0 and int(repeat) != 1:
    print("\nValeur non valide.")
    repeat = input("Souhaitez vous effectuer d'autres changements ?: \nOui: 0\nNon: 1\nVotre saisie: ")

  if int(repeat) == 0:
    continue
  else:
    print(exit())
