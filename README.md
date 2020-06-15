###### PRESENTATION ######

Ce projet vise à implémenter le programme FizzBuzz au moyen d'un réseau neuronal,séquentiel et à couches denses, construit à l'aide du framework Tensorflow.

-- Règles du jeu --
FizzBuzz prend en entrée un nombre entier et renvoie soit:
-"Fizz" si le nombre reçu est un multiple de 3
-"Buzz" si le nombre reçu est un multiple de 5
-"FizzBuzz" si le nombre reçu est à la fois un multiple de 3 et de 5
-Le nombre reçu en entrée est affiché s'il n'est un ni multiple de 3 ni multiple de 5

En somme, le but est de modéliser ces 4 règles simples au travers d'un réseau de neurones. Celui-ci aura donc en sortie 4 probabilités entre -1 et 1 pour l'appartenance à l'un des 4 cas. Il nous suffit alors de selectionner seulement la probabilité la plus haute des 4 et de la considérer comme prédiction.

Cette approche, dite "Classification multi-classes", vise à assigner à chaque entrée un unique label parmi une multitude (plus de deux). 

-- Remarque --
Il serait intéressant de comparer les résultats entre cette approche et la classification dite "multi-labels" où l'on peut prédire plusieurs classes pour une seule entrée. Nous aurions donc 3 neurones sur la couche de sortie et non 4 puisque la colonne "FizzBuzz" devient alors obsolète.


###### TRAINER ######

Le fichier 'trainer.py' situé dans le dossier /fb-trainer permet d'entraîner un réseau de neurones au fizzbuzz à partir de données générées aléatoirement. Ce modèle est ensuite sauvegardé dans le dossier "/fizzbuzz_models" afin que notre autre programme fb-predictor puisse le charger et l'interroger directement.

D'abord, NB_OF_SAMPLES échantillons (50 000 par défaut) sont créés ayant pour valeur entre 0 et (2 ** NB_OF_BITS) - 1. (NB_OF_BITS = 18 par défaut)

Ensuite, on créer leur table de vérité : la colonne 'FizzBuzz' est égale à 1 si le nombre est un multiple de 3 et de 5, la colonne 'Fizz' est égale à 1 si le nombre est un multiple de 3 (mais n'est pas un multiple de 5 dans le cas du multi-classe, cf: note ci-dessus), la colonne 'Buzz' = 1 si le nombre est un multiple de 5 (mais pas de 3). Si aucun de ces 3 cas n'est concerné, c'est alors la colonne 'Number' que l'on met à 1, signifiant qu'il faudra afficher le nombre reçu en entrée plutôt qu'une réponse FizzBuzz.

Notre objectif est de faire tendre notre perte (ou "loss") le plus proche possible de 0 sur le set de test et s'assurer ainsi que notre modèle généralise correctement la donnée reçue.

5 paramètres optionnels pour ce programme :
NB_OF_BITS (-b, --bits): nombre de bits sur lesquels sont encodés les nombres reçus
Valeur par défaut = 18, donc valeur maximale pour un nombre = 262143 ((2 ** NB_OF_BITS) - 1)

NB_OF_SAMPLES (-s, --samples): Nombre d'échantillons générés par le programme pour entraîner le réseau neuronal, un nombre plus grand implique un meilleur entraînement mais un besoin de ressources également accru.
Valeur par défaut = 50 000

NB_OF_ITERATIONS (-i, --iterations): Nombre d'itérations faites par le programme au cours de l'entraînement. Une augmentation des itérations peut déboucher sur une meilleure qualité d'entraînement mais pas systématiquement. Les ressources nécessaires, elles, sont systématiquement plus importantes.
Valeur par défaut = 200

TEST_DATA_SIZE (-t, --test_size): Proportion en pourcentage de la donnée mise de côté pour évaluer le modèle après l'entraînement afin de s'assurer que le modèle en question généralise correctement son apprentissage sur des cas jusqu'alors inconnus.
Valeur par défaut = 20

MODEL_NAME (-m, --model_name): Nom du sous-répertoire dans lequel le modèle entraîné sera sauvegardé
Valeur par défaut = Date et heure du lancement du programme


###### PREDICTOR ######

Le fichier 'predictor.py' situé dans le dossier "/fb-predictor" permet d'interroger un modèle préalablement entraîné et sauvegardé.

La classe CLI du programme se charge de l'interaction entre celui-ci et l'utilisateur, donc prompts, lectures d'input, envois de la donnée au modèle chargé, interprétations des prédictions et restitutions à l'utilisateur.

La classe Parser se charge de l'entrée de l'utilisateur envoyée par la CLI et de la gestion d'erreur. Il s'assure par exemple que l'entrée de l'utilisateur est inférieur au nombre maximum accepté (< 262144 par défaut)

La classe Model se charge du chargement du modèle et de prédire les nombres renseignés par l'utilisateur en CLI.


2 arguments optionnels (les 3 autres sont acceptés mais n'ont aucun effet):

-MODEL_NAME (-m, --model_name): nom du modèle à charger depuis le dossier "fizzbuzz_models" à la racine
Valeur par défaut: dernier modèle ayant été créé ou modifié

-NB_OF_BITS (-b, --bits): Doit être égal au NB_OF_BITS du modèle entraîné que l'on veut interroger.
Valeur par défaut: 18 (valeur max = 262143) 


###### SEEDS ######
Fixer la seed de numpy permet de générer les mêmes données aléatoires au fil des éxécutions

Fixer la seed de Tensorflow permet d'avoir les mêmes initialisations des neurones au fil des éxécutions

Fixer la seed de train_test_split du module scki-kit permet d'avoir les mêmes partitions de données au fil des éxécutions

--- Remarque ---
Une solution envisageable pour un modèle de production serait d'entraîner 10 versions du même modèle avec des seeds différentes
et de prendre le vote de la majorité dans un problème de classification ou la moyenne dans un cas de régression.

###### PREREQUIS ######
Allez dans le dossier racine fizzbuzz/
```
cd fizzbuzz
```

#Python version 3.5 - 3.8
!!! Tensorflow ne fonctionne qu'avec la version 64-bit de Python !!!
```
py --version
```
or download it at: https://www.python.org/downloads/


#Python's Virtual Environment

--- UBUNTU / DEBIAN ---
```
sudo apt-get install python3-venv && py -m venv fb-venv && source fb-venv/bin/activate
```

--- OTHER UNIX DISTRIBUTIONS ---
```
py -m venv fb-venv && source fb-venv/bin/activate
```

--- WINDOWS ---
```
py -m venv fb-venv && fb-venv\Scripts\activate.bat
```


#Pip (version >19.0)

--- UNIX ---
```
sudo apt-get install python3-pip ; pip install --upgrade pip
```

--- WINDOWS ---
Téléchargez ce fichier sur votre bureau: https://bootstrap.pypa.io/get-pip.py
puis lancez la commande
```
py %USERPROFILE%\Desktop\get-pip.py
```


Si la commande "pip --version" n'échoue pas, alors pip est probablement correctement installé !

Pour mettre pip à jour (20.1.1 actuellement):
```
py -m pip install --upgrade pip
```

###### INSTALLATION ######

Installer les dépendances du projet via pip
```
py -m pip install -r requirements.txt
```

--- WINDOWS ---
Sur Windows, tensorflow recquiert également les paquets C++ VS 2015, 2017 et 2019 accessible ici:
https://aka.ms/vs/16/release/vc_redist.x64.exe

###### UTILISATION ######

--- TRAINER ---

To train a new model:
```
py fb-trainer/trainer.py
```

To train a new model and save it under a custom name (here we call it my_model_name):
```
py fb-trainer/trainer.py -m my_model_name
```

To train a new model with a custom number of iterations (50 here):
```
py fb-trainer/trainer.py -i 50
```

To train a new model with a custom portion of testing data (40% here):
```
py fb-trainer/trainer.py -t 40
```

To train a new model with a custom number of samples (10 000 here):
```
py fb-trainer/trainer.py -s 10000
```

To train a new model with a custom number of bits (8 bits here, i.e 255 max. value):
```
py fb-trainer/trainer.py -b 8
```

--- PREDICTOR ---

To make predictions through the CLI:
```
py fb-predictor/predictor.py
```

To make predictions with a model with a custom number of bits (8 bits here, i.e 255 max. value):
```
py fb-predictor/predictor.py -b 8
```

To make predictions with a model with a specific name (here my_model_name):
```
py fb-predictor/predictor.py -m my_model_name
```

Une fois dans l'interpreteur de commande, rentrez un nombre inférieur au maximum pour avoir le retour du fizzbuzz neuronal ou bien tapez 'quit' pour quitter le programme.

--- EXAMPLE ---
py fb-trainer/trainer.py -s 20000 -b 10 -t 33 -i 80 -m test_model && py fb-predictor/predictor.py -b 10 -m test_model


###### MY FEEDBACK ######

-- Importance des features et de leur préparation --

Seul les nombres sont donnés au réseau neuronal, aucune autre feature n'est construite. Cependant, les nombres ne sont pas donnés sous base 10 (système décimal) au réseau de neurones mais sous base 2 (système binaire). Cet encodage binaire de la donnée transmise augmente grandement l'efficacité du modèle. 

En effet, même en créant des features supplémentaires comme la somme des chiffres d'un nombre et le dernier chiffre du nombre (astuces utilisées par les humains pour rapidement savoir si un nombre est respectivement un multiple de 3 et/ou de 5), le modèle n'est jamais passé en dessous de 25% de perte alors que j'ai facilement réussi à descendre sous les 0,1% sans les features supplémentaires en lui fournissant les données encodées en binaire.

-- Remarque --
Le fait de fournir le nombre chiffre par chiffre en base 10, en commençant par le début ou la fin, n'a eu aucun effet conséquent sur les prédictions :(
Je m'attendais à ce qu'un réseau de neurones puisse mieux (ou plus facilement) modéliser l'intelligence humaine telle que les petites astuces mathématiques.
Ce modèle nécessite énormément de temps (d'entraînement) et de ressources pour répondre à une question basique d'informatique telle qu'un fizzbuzz.

-- Remarque n°2 --
Les nombres négatifs sont traités en compléments de deux, c'est à dire que -1 <=> 111111111111111111 <=> 262143 et renvoie donc Fizz ! J'ai donc bloqué tout nombre négatifs en entrée du programme.