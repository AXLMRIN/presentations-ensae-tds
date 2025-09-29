# presentations-ensae-tds

Here you'll find all the presentations for the "Python for data science" seminars held at ENSAE.

## Index

- [Session 1 (16th Sept 2025)](./presentations/seance_1-25_09_16.pdf)
  - [Rappel de la syntaxe de base](./corrections/seance_1-25-09-16-syntaxe.py)
  - [Correction des exercices Numpy](./corrections/seance_1-25-09-18-numpy.ipynb)
- [Session 2 (23rd Sept 2025)](./presentations/seance_2-25_09_23.pdf)
  - [Correction pandas intro](./corrections/seance_2-26-09-23-pandas-intro.ipynb)
  - [Correction pandas intro](./corrections/seance_2-26-09-23-pandas-suite.ipynb)

# Créer une session onyxia

Pour ouvrir une session onyxia :

- À partir du [site de Lino Galiana](https://pythonds.linogaliana.fr): trouver le notebooks de votre choix, appuyer sur la pillule "SSP Cloud | Lancer avec VSCode"
- À partir d'[Onyxia](https://datalab.sspcloud.fr), se connecter puis se rendre dans la section "Mes services", appuyer sur "Nouveau service", sélectionner "Vscode-python", cliquer sur "Lancer" puis "Lancer". Vous êtes redirigés vers la page "Mes services". Attendre que le service est déployé, puis clique sur "Ouvrir", "Cliquer pour copier le mot de pass..." et enfin "Ouvrir le service 🚀" et finalement, coller le mot de passe.

# Git et Github

## Git

Git est uniquement local (propre à la machine). Sert à versionner son code à l'aide des `commit`.

### Comment `commit`

2 étapes :

- Stage (En ligne de code : `git add filename`; sur VSCode: onglet Source control [^1], cliquer sur "+", [voir présentation slide 6](./presentations/seance_2-25_09_23.pdf))
- Commit (`git commit -m "MESSAGE"`; sur VSCode: onglet Source control [^2], ajouter un message et cliquer sur "✔ Commit", [voir présentation slide 6](./presentations/seance_2-25_09_23.pdf))

🎉 Votre fichier est versionné 🎉

### Ignorer des fichiers

Tout n'est pas bon à garder, vous pouvez ajouter un fichier `.gitignore` pour spécifier les fichiers à ignorer.

Ex :

```
fichier/specifique.py
dossier/
*.html # Tous les fichiers html
```

### Commandes additionnelles et astuces

- Voir vos derniers changements:
  - ligne de commange : `git log`, permet de voir l'identifiant du commit (SHA), l'auteur, la date et le message associé.
  - VSCode : dans l'onglet Source control, il y a un onglet "repositories"
- Annuler un comit
  - en gardant les modifications
    - en ligne de commande : `git reset --soft $SHA` (remplacer `$SHA` par l'identifiant du commit) ou bien `git reset --soft HEAD^` pour revenir un commit en arrière.
    - Dans VS code : dans la section Source control, dans l'onglet "repositories" puis "commits" il y a la liste de tous les commits. Il suffit d'appuyer sur le logo retour &#8634; [voir présentation slide 10](./presentations/seance_2-25_09_23.pdf)
  - sans garder les modifications (🚨DANGER🚨):
    - en ligne de commande : `git reset --hard $SHA` (remplacer `$SHA` par l'identifiant du commit) ou bien `git reset --hard HEAD^` pour revenir un commit en arrière.

## Github

Plateforme en ligne de partage de projets Git.

- Créer un dépot : [voir présentation slide 14](./presentations/seance_2-25_09_23.pdf)
- Cloner un dépot sur sa machine : [voir présentation slide 15](./presentations/seance_2-25_09_23.pdf)

Une fois qu'un dépot est copié sur votre machine :

- Pour téléverser (upload) ses modifications (celles qui ont été commit): `git push`
- Pour télécharger (download) les modifiications d'autres contributeur.ices : `git pull` (si message d'erreur : `git pull --rebase`).

### Comment travailler avec des branches?

Les branches permettent de travailler de manière indépendantes. Pour les utiliser il faut :

- Créer une branche : `git checkout -b user/nom-branche` ou `git branch user/nom-branche` puis `git checkout user/nom-branche`.
- Publier la branche sur Github : `git push --set-upstream origin user/nom-branche`
- Travailler dessus en enregistrant des commits
- Une fois le travail terminé, pour joindre les modifications au projet il faut :
  - Retourner sur la branche `main` : `git checkout main`
  - Récupérer les possibles modifications apportées entre temps : `git pull`
  - Si modifications il y a eu des modifications, la bonne pratique est de reporter ces modifications dans sa branche :
    - retourner dans sa branche : `git checkout user/nom-branche`
    - Joindre les modifications téléchargées : `git merge main`
    - Régler les possibles conflits
    - S'assurer que la branche est stable, nos fonctions font bien ce qu'on leur demande.
    - Une fois qu'on est satisfait, on peut retourner sur la branche `main` : `git checkout main`
  - Joindre les modifications de notre branche à la branche `main` : `git merge user/nom-branche`
  - _Aucun conflit ne devrai apparaître puisqu'ils ont du être réglés en amont_
  - Téléverser la branche `main` : `git push`

Autre méthode proposées depuis Github : [voir présentation slide 20](./presentations/seance_2-25_09_23.pdf)

[^1]: icone 3 points reliés sur la gauche
[^2]: icone 3 points reliés sur la gauche
