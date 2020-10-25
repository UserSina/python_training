import json
import os


def startupCheck():
    if (os.path.exists('repertoire.json')):
        print('\nJson file exists!')
        return True
    else:
        print('\nNo json file!')
        return False


def saveToFile(data):
    print("Writing data to 'repertoire.json'")
    with open('repertoire.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def menu():
    print("/-------------------------Repertoire Telephone----------------------------/")
    print("0.Re-afficher ce menu.")
    print("1.Afficher tous les contactes.")
    print("2.Ajouter un contact.")
    print("3.Modifier un contact.")
    print("4.Effacer un contact.")
    print("5.Quitter!\n")


def showAll(myList):
    print("/-----------------1.Liste des contactes:----------------/")
    if (len(myList) == 0):
        print("Pas de contactes")
        return
    for item in myList:
        print(item['name'], item['phone'], sep=': ')


def addContact(myList):
    print("/-----------------2.Ajout contacte:----------------/")
    name = input("Name: ")
    phone = input("Phone: ")
    item = {'name': name, 'phone': phone}
    myList.append(item)
    print('Added.')


def editContact(myList):
    print("/-----------------3.Modifier contacte:----------------/")
    choice = input("1.By name | 2.By phone: ")
    if (choice == '1'):
        name = input('Nom: ')
        for item in myList:
            if(item['name'] == name):
                item['phone'] = input('New phone: ')
                print('Updated.')
                return
        print('Not found')
    elif (choice == '2'):
        phone = input('Phone: ')
        for item in myList:
            if(item['phone'] == phone):
                item['name'] = input('New name: ')
                print('Updated.')
                return
        print('Not found')
    else:
        print('Modification annulé')


def deleteContact(myList):
    print("/-----------------3.Effacer contacte:----------------/")
    choice = input("1.By name | 2.By phone: ")
    if (choice == '1'):
        name = input('Nom: ')
        for item in myList:
            if(item['name'] == name):
                myList.remove(item)
                print('Deleted.')
                return
        print('Not found')
    elif (choice == '2'):
        phone = input('Phone: ')
        for item in myList:
            if(item['phone'] == phone):
                myList.remove(item)
                print('Deleted.')
                return
        print('Not found')
    else:
        print('Suppression annulé')


def main():
    showMenu = True
    myList = [{}]
    if (startupCheck()):
        print('Reading data from json')
        with open('repertoire.json') as f:
            myList = json.load(f)
    else:
        print('Creating empty dictionary')
        with open('repertoire.json', 'w') as f:
            json.dump(myList, f)

    menu()
    choice = input('\nChoix: ')
    while True:
        if choice == '0':
            menu()
            choice = input('\nChoix: ')
        elif choice == '1':
            showAll(myList)
            choice = input('\nChoix: ')
        elif choice == '2':
            addContact(myList)
            choice = input('\nChoix: ')
        elif choice == '3':
            editContact(myList)
            choice = input('\nChoix: ')
        elif choice == '4':
            deleteContact(myList)
            choice = input('\nChoix: ')
        elif choice == '5':
            saveToFile(myList)
            break
        else:
            print('Invalid! Show menu: 0')
            choice = input('\nChoix: ')


if __name__ == "__main__":
    main()
