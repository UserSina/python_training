import json
import os


def startupCheck():
    if (os.path.exists('repertoire.json')):
        print('\nJson file exists!')
        return True
    else:
        print('\nNo json file!')
        return False


def showAll(myList):
    if (len(myList) == 0):
        print("Pas de contactes")
    # else:
        # for item in myList:


def main():
    myList = []
    if (startupCheck()):
        print('Reading data from json')
        with open('repertoire.json') as f:
            myList = json.load(f)
    else:
        print('Creating empty dictionary')

    print("/-----------------------Repertoire Telephone--------------------------/")
    print("1.Afficher tous les contactes.")
    print("2.Ajouter un contact.")
    print("3.Modifier un contact.")
    print("4.Effacer un contact.")
    print(myList)


if __name__ == "__main__":
    main()
