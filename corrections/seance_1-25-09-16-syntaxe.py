"""
Introduction à python, la syntaxe et les concepts de base

Toutes les variables python sont des objets. Ça veut dire que toute variable 
possède des attributs (ie valeurs / objets) rattachés, ainsi que des méthodes 
(des fonctions rattachées).

Par exemple, on créé un objet 'int' (integers = nombre entier)
"""
a : int = 15 # Syntaxe : l'objet a de type int est égal à 15
print(a.real) # Attribut "valeur réelle de a"
# >>> 15
print(a.imag) # Attribut "valeur imaginaire de a"
# >>> 0
print(a.is_integer()) # Méthode qui vérifie que l'objet est un entier
# >>> True

"""
Chaque objet propose de nombreuses fonctions qui peuvent être très utiles. À vous
de trouver celles qui vous parlent le plus / que vous trouvez les plus utiles. 

Syntaxe de base : 
"""
# Créer un objet avec "="
a = 1 # On créé un objet a et on lui donne la valeur 1
a, b, c = 1, 2, 3 # On peut créer plusieurs objets en même temps, a = 1; b = 2; c = 3

# Les types les plus -----------------------------------------------------------
## Les nombres  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  
a : int = 1 # Les nombres entiers
a : int = 1 + 1j # Les imaginaires (sans virgules)
a : float = 1.5 # les réels
a : float = 1 + 1.5j # Les imaginaires (à virgule)

## Les chaînes de caractères  --  --  --  --  --  --  --  --  --  --  --  --  --
ch : str = "Hello"
ch : str = 'Hello'
ch : str = '''Hello'''
ch : str = """Hello"""
ch : str = f'a = {a}' # f-strings est une technique pour créer des chaînes de caractères à partir d'objets déjà créés
print(ch)
# >>> a = (1+1.5j)

## Les booléens --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  
bo : bool = True
bo : bool = False

## Les listes  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -
l : list = [1, 2, 3, 'Hello', ['Liste imbriquée', 23]]
l2 : list = [i for i in range(10)] # Création d'une liste par compréhension 
print(l2)
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## Les dictionnaires --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  
d : dict = {"clef" : 1, "key" : [1, 2, 3], "d_impriqué" : {'clef' : True}}
d2 : dict = {f"key_{i}" : i for i in range(10)} # Création d'une liste par compréhension
print(d2)
# >>> {'key_0': 0, 'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4, 'key_5': 5, 'key_6': 6, 'key_7': 7, 'key_8': 8, 'key_9': 9}

# Les opérations ---------------------------------------------------------------
## Entre nombres --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print(b + c) # Addition
# >>> 5
print(b - c) # Soustraction
# >>> -1 
print(b * c) # Multiplication
# >>> 6
print(b ** c) # Puissance
# >>> 8
print(b / c) # Division
# >>> 0.6666666666666666
print(b // c) # Partie entière de la division
# >>> 0
print(b % c) # Reste par division entière; modulo
# >>> 2
#Arithmétiquemetn parlant la division en nombre entiers
# b = n * c + r (avec r le reste de la division de b par c)
# se traduit par : 
# b = (b // c) * c + b % c

## Entre les booléens  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -
print(True & False) # opération ET
# >>> False
print(True | False) # opération OU
# >>> True

## Entre les chaînes de caractères  --  --  --  --  --  --  --  --  --  --  --  
print("Une chaîne" + " ajoutée à une autre") # Concaténer des chaînes de caractères
# >>> Une chaîne ajoutér à une autre
ch = "Hello"
print(ch[0]) # Séléctionner le premier élément de la chaîne ()
# >>> H
print(ch[1:4]) # Séléctionner les éléments 1, 2 et 3
# >>> ell
print(ch[1:]) # Séléctionner les éléments 1 jusqu'à la fin
# >>> ello
print(ch[:4]) # Séléctionner les éléments du début au 3è
# >>> Hell
print(len(ch)) # Calculer la taille de la chaîne
# >>> 5 

## Entre les listes  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -- 
print([1, 2, 3] + ["1"]) # Concaténer des listes
# >>> [1, 2, 3, '1']
l = [1, 2, 3, 'Hello', ['Liste imbriquée', 23]]
print(l[0]) # Séléctionner le premier élément de la chaîne ()
# >>> 1
print(l[1:4]) # Séléctionner les éléments 1, 2 et 3
# >>> [2, 3, 'Hello']
print(l[1:]) # Séléctionner les éléments 1 jusqu'à la fin
# >>> [2, 3, 'Hello', ['Liste imbriquée', 23]]
print(l[:4]) # Séléctionner les éléments du début au 3è
# >>> [1, 2, 3, 'Hello']
print(len(l)) # Calculer la taille de la chaîne
# >>> 5 

## Entre les dictionnaires  --  --  --  --  --  --  --  --  --  --  --  --  --  
# c'est plus compliqué... 
d : dict = {"clef" : 1, "key" : [1, 2, 3], "d_impriqué" : {'clef' : True}}
print(d["key"]) # séléctionner l'objet clef
# >>> [1, 2, 3]

# Conditions -------------------------------------------------------------------
# Le comportement dépend éminament de l'objet considéré
print(b == c) # Test si b est égal à c
# >>> False
print(b != c) # Test si b est différent de c
# >>> True
print(b < c) # b inférieur à c
# >>> True
print(b <= c) # b inférieur ou égal à c
# >>> True
print(b > c) # b supérieur à c
# >>> False
print(b >= c) # b supérieur ou égal à c
# >>> False

## Les conditions dans le script --  --  --  --  --  --  --  --  --  --  --  --  
if a == b : 
    print("a est égal à b")
elif b == c : 
    print("a n'est pas égal à b, mais b est égal à c")
else : 
    print("a n'est pas égal à b, b n'est pas non plus égal à c")
# >>> a n'est pas égal à b, b n'est pas non plus égal à c
    
# Les boucles ------------------------------------------------------------------
## boucle la plus courante  --  --  --  --  --  --  --  --  --  --  --  --  --  
for i in range(10): 
    print(i)
# >>> 0
# >>> 1
# >>> 2
# >>> 3
# >>> 4
# >>> 5
# >>> 6
# >>> 7
# >>> 8
# >>> 9

## boucle dans une liste  --  --  --  --  --  --  --  --  --  --  --  --  --  -- 
l = [1, 2, 3, 'Hello', ['Liste imbriquée', 23]]
for element in l : 
    print(element)
# >>> 1
# >>> 2
# >>> 3
# >>> Hello
# >>> ['Liste imbriquée', 23]
    
## boucle dans un dictionnaire  --  --  --  --  --  --  --  --  --  --  --  --  
d : dict = {"clef" : 1, "key" : [1, 2, 3], "d_impriqué" : {'clef' : True}}
for key in d : 
    print(key, " : ", d[key])
# >>> clef  :  1
# >>> key  :  [1, 2, 3]
# >>> d_impriqué  :  {'clef': True}