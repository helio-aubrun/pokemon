import json
testlast = True
while testlast:

    #nom d'ataque
    atack = input ("donner le nom de l'atacke : \n")

    #puissance
    test1 = False
    while not test1 : 
        try :
            puissance = int (input ("donner la puissance d'atacke : \n"))
            test1 = True
        except:
            print ("donner un entier")

    #category
    test2 = False
    list1 = ["statu", "phisique", "special"]
    while not test2 :
        try :
            num = int (input ("donner la category d'atacke 1 = statu, 2 = phisique, 3 = special: \n"))
            while num not in [1,2,3] :
                num = int (input ("donner la category d'atacke 1 = statu, 2 = phisique, 3 = special: \n"))
            test2 = True
        except:
            print ("donner un entier")
    cat = list1[num - 1]

    #prescision
    test3 = False
    while not test3 : 
        try :
            precision = int (input ("donner la precision d'atacke : \n"))
            test3 = True
        except:
            print ("donner un entier")

    #pp
    test4 = False
    while not test4 : 
        try :
            pp = int (input ("donner les pp d'atacke : \n"))
            test4 = True
        except:
            print ("donner un entier")


    #type
    test5 = False
    list2 = ["eau", "feu", "plant", "normal", "spectre"]
    while not test5 : 
        try :
            num1 = int (input ("donner la category d'atacke 1 = eau, 2 = feu, 3 = plant, 4 = normal, 5 = spectre: \n"))
            while num1 not in [1,2,3,4,5] :
                num1 = int (input ("donner la category d'atacke 1 = eau, 2 = feu, 3 = plant, 4 = normal, 5 = spectre: \n"))
            test5 = True
        except:
            print ("donner un entier")
    type = list2[num1 - 1]

    #creation dun dectionaire pour l'atack
    dicti = {
        "nom": atack,
        "puissance": puissance,
        "category": cat,
        "precision": precision,
        "pp": pp,
        "type": type
    }


    #recuperer le dictionaire
    with open('atack_list.json', 'r') as f:
        atack_list = json.load(f)


    # obtention du nouvean id
    last_key = list(atack_list.keys())[-1]
    new_key = str(int(last_key) + 1)

    #ajout du nouveau dictionaire
    atack_list [new_key] = dicti

    with open('atack_list.json', 'w') as f:
        json.dump(atack_list, f)
        
