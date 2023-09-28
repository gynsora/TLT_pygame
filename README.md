# TLT - pygame #
--- ---
Description : Dans le cadre d'une validation de formation de développeur PYTHON COT, j'ai crée ce mini-jeu à l'aide de pygame.
TLT est un jeu au tour par tour inspiré par dofus, othello et wavens.

# Pré-requis #
--- ---
Ce projet à été crée avec:
- Python version 3.11.3
- le module pygame version 2.5.0 
- le module pygame-ce version 2.3.1 
- le module pygame-gui version 0.6.9
- le module os (inclus dans python3)
- le module sys (inclus dans python3)

# Gameplay #
--- ---
TLT est un jeux au tour par tour, le but du jeu est de battre son adversaire en utilisant les sorts à sa disposition.
Un tour de jeux est composer de 4 phases différentes.
Le but du jeu est de réduire les points de vie de l'adversaire à 0. tout en évitant de perdre tout ces point de vie.

## La phase de movement ##
--- ---
La première phase durant un tour de jeu est la phase de mouvement.
La phase de mouvement permet au joueur de choisir un sort de déplacement si il souhaite s'approché ou s'éloigné de son adversaire.
### Déroulement de la phase de mouvement ###
- Le joueur doit cliquer sur un sort de déplacement , le sort est en surbrillance pendant la phase de mouvement (voir le sort sous la flèche verte de l'image ci-dessous)
- Lorsque le joueur à cliquer (sélectionner) un sort le board du jeu affichera des cases en jaune, cela représente la portée du sort
- Puis un fois que le joueur à cliquer sur une case jaune, le joueur se déplace vers la case selectionnée, puis la phase prend fin
- Si le joueur ne souhaite pas se déplacer, il peut directement passé à la phase suivante en appuyant sur le bouton "fin de tour" (voir le sort sous la flèche bleu de l'image ci-dessous)
[image phase de mouvement](Assets/img/readMe/mouvementPhase.png)

## La phase d'attaque ##
--- ---
La deuxième phase durant un tour de jeu est la phase d'attaque .
La phase d'attaque permet au joueur de choisir un sort d'attaque si il souhaite attaquer son adversaire.
### Déroulement de la phase d'attaque ###
Le déroulement de la phase d'attaque est identique à celui de la phase de mouvement, seulement les sorts en surbrillance (sélectionnable) sont des sorts offensifs.

## La phase de défense ##
--- ---
La troisième phase durant un tour de jeu est la phase de défense .
La phase de défense permet au joueur de choisir un sort de défense si il souhaite attaquer son adversaire.
Cette phase est reservé à celui qui à besoin de contrer une attaque pendant un tour.
Si le joueur à attaquer précédement durant le tour à la phase de défense sera effectuer par l'ennemi.
### Déroulement de la phase de défense ###
Le déroulement de la phase de défense est identique à celui de la phase de mouvement, seulement les sorts en surbrillance (selectionnable) sont des sort défensif.


## La phase de combat ##
--- ---
La dernière phase durant un tour de jeu est la phase de combat.
C'est durant cette phase que les animations des sort d'attaque et défense se font.
### Déroulement de la phase de combat ###
- L'animation du sort du personnage qui défend est faite
- Puis les calculs des bonus et des déplacement lié au sort sont fait
- Ensuite l'animation du sort du personnage qui attaque est faite, le board change de couleur en fonction de l'élement du sort attaquant.
- Puis le jeu regarde si l'attaque touche le personnage défendeur, si oui le calcul des dégâts est fait.

## Fin de tour ##
- Si le défendeur à ses points de vie réduit à zéro il perd.
- Sinon le tour d'après il devient l'attaquant.