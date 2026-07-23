# Chapitre 4 — L'atelier du développeur

> *« Un artisan ne commence jamais par fabriquer son premier meuble. Il commence par préparer son atelier. Cette journée marqua le moment où IAssistant cessa d'être une idée pour devenir un véritable projet. »*

---

## Une nouvelle étape

Les trois premiers chapitres nous avaient permis de comprendre pourquoi IAssistant devait exister.

Nous avions défini sa vision, ses principes fondateurs, son architecture générale ainsi que les valeurs qui guideraient chacune de nos décisions.

Une évidence s'est alors imposée.

Avant d'écrire la moindre fonctionnalité, il fallait préparer l'environnement dans lequel toutes ces idées allaient prendre vie.

Cette décision pouvait sembler secondaire.

Elle allait pourtant influencer toute la vie du projet.

---

## Construire l'atelier avant le logiciel

La tentation aurait été grande de commencer immédiatement à écrire des classes Python.

Nous avons volontairement résisté à cette envie.

Un bon logiciel ne commence pas par son code.

Il commence par son environnement de travail.

Nous avons donc choisi de construire notre atelier avant de construire notre maison.

Le projet a été organisé autour d'un Workspace Visual Studio Code afin que l'ouverture d'IAssistant ne soit plus une succession de manipulations, mais un simple geste.

Petit à petit, chaque élément a trouvé sa place.

Le dépôt GitHub a été préparé.

Le projet Python a été structuré.

Les premiers fichiers de configuration ont été créés.

Les bases de notre futur environnement de développement étaient désormais posées.

---

## Le Workspace

Le Workspace est rapidement devenu bien plus qu'un simple fichier de configuration.

Il représente désormais la porte d'entrée du projet.

Ouvrir IAssistant ne signifie plus ouvrir un dossier contenant quelques fichiers Python.

Cela signifie entrer dans un environnement entièrement préparé pour développer l'application.

Cette idée nous a particulièrement marqués.

Le Workspace n'ouvre pas simplement un projet.

Il ouvre l'atelier dans lequel IAssistant va être construit.

---

## Le premier lancement

Une autre étape importante fut la création de la chaîne de démarrage de l'application.

Plutôt que de lancer directement un fichier Python, nous avons souhaité construire une architecture claire dès le premier jour.

Cette réflexion a donné naissance à plusieurs composants.

Le **launcher** devient l'unique point d'entrée du projet.

Le **bootstrap** prépare l'environnement avant le démarrage de l'application.

Enfin, la classe **IAssistant** représentera l'application elle-même.

Cette séparation paraît simple.

Elle permettra pourtant au projet de grandir sans jamais remettre en question son mode de démarrage.

---

## Le bootstrap

Le bootstrap est rapidement devenu le chef d'orchestre du lancement.

Son rôle n'est pas de faire le travail.

Son rôle est de préparer le terrain.

Aujourd'hui, il affiche simplement une bannière, prépare l'environnement puis transmet la main à l'application.

Demain, il pourra vérifier la configuration, préparer les différents services, initialiser les journaux ou encore contrôler que tout est prêt avant de poursuivre.

Sa responsabilité restera toujours la même.

Préparer IAssistant avant son démarrage.

---

## Une architecture qui grandit naturellement

Cette séance nous a également permis de confirmer une règle importante.

Nous ne créerons jamais un fichier simplement parce qu'il pourrait être utile un jour.

Chaque dossier, chaque module et chaque classe devront répondre à un besoin réel.

Lorsque ce besoin apparaîtra, l'architecture évoluera naturellement.

Cette manière de travailler nous semble beaucoup plus durable que de construire dès le départ une structure complexe dont une grande partie resterait vide pendant des mois.

L'architecture accompagnera la croissance du projet.

Elle ne la précédera jamais.

---

## Le premier démarrage officiel

L'un des moments les plus symboliques de cette séance fut le premier lancement réussi d'IAssistant.

Pour la première fois, le projet ne se limitait plus à une collection de fichiers.

Il était capable de démarrer selon une chaîne clairement définie.

```
Workspace
    ↓
Run and Debug / Run Task
    ↓
Launcher
    ↓
Bootstrap
    ↓
IAssistant
```

Ce lancement n'apportait encore aucune intelligence.

Aucune automatisation.

Aucun dialogue.

Pourtant, une étape essentielle venait d'être franchie.

IAssistant possédait désormais une véritable porte d'entrée.

---

## Ce que cette séance a réellement construit

À première vue, cette journée pourrait sembler très technique.

Pourtant, elle représente bien davantage.

Nous n'avons pas développé IAssistant.

Nous avons construit l'endroit dans lequel il allait être développé.

Les outils sont désormais prêts.

Le projet est organisé.

Le démarrage est maîtrisé.

L'atelier est enfin opérationnel.

---

## Et maintenant…

Une nouvelle question apparaît naturellement.

Elle sera probablement l'une des plus importantes de toute cette aventure.

> **Qu'est-ce qu'IAssistant ?**

Non pas techniquement.

Mais conceptuellement.

La réponse à cette question donnera naissance à la première véritable classe métier du projet.

À partir de ce moment, nous ne construirons plus seulement un environnement de développement.

Nous commencerons enfin à construire IAssistant lui-même.

---

*Ainsi s'achève le quatrième chapitre.*

*L'atelier est prêt.*

*Les outils sont rangés.*

*Il est temps de donner vie à IAssistant.*
