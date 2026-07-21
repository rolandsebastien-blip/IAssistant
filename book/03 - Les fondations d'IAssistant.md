# Chapitre 3 — Les fondations d'IAssistant

> *« Avant d'écrire une ligne de code, il faut comprendre ce que l'on souhaite réellement construire. »*

---

## Introduction

Au début de cette troisième séance, notre objectif semblait clair : poursuivre le développement d'IAssistant.

Pourtant, au fil des échanges, une évidence s'est imposée. Nous étions sur le point de construire une architecture sans avoir complètement défini ce qui faisait l'identité du projet.

Nous avons donc volontairement ralenti.

Au lieu d'ajouter du code, nous avons pris le temps de nous poser une question essentielle :

**Pourquoi IAssistant doit-il exister ?**

Cette simple question a profondément transformé notre manière de concevoir le projet.

---

## Une interview fondatrice

Plutôt que de discuter immédiatement de Python, de Home Assistant ou de structure logicielle, nous avons entrepris une véritable interview fondatrice.

Chaque réponse a permis de préciser un peu plus la mission d'IAssistant.

Nous avons compris que son objectif n'était pas de produire davantage d'automatisations, ni de devenir une couche supplémentaire au-dessus de Home Assistant.

Son rôle est plus fondamental.

IAssistant doit comprendre les personnes qui vivent dans une maison avant de chercher à comprendre la maison elle-même.

Cette idée deviendra la première décision d'architecture du projet.

---

## Changer de perspective

Au début du projet, nous imaginions naturellement une architecture organisée autour des intégrations, des objets connectés et des automatisations.

L'interview a progressivement inversé cette logique.

Les objets ne sont pas le point de départ.

Ils deviennent simplement des moyens mis au service des habitants.

Le véritable cœur d'IAssistant est désormais l'utilisateur.

Cette évolution modifiera durablement la manière dont le logiciel sera conçu.

---

## Une nouvelle architecture

Cette réflexion nous a conduits à revoir entièrement l'organisation du projet.

L'architecture ne reflète plus des choix techniques mais les grandes responsabilités d'IAssistant.

```text
src/
└── iassistant/
    ├── core/
    ├── domain/
    ├── integrations/
    ├── interaction/
    ├── knowledge/
    └── utils/
```

Chaque dossier représente désormais un concept clairement identifié plutôt qu'un simple regroupement de fichiers.

---

## Les premières décisions

Cette séance marque également une étape importante dans la gouvernance du projet.

Nous avons décidé d'introduire les **Architecture Decision Records (ADR)**.

Chaque décision importante sera désormais documentée afin d'expliquer non seulement ce qui a été choisi, mais surtout pourquoi ce choix a été fait.

Le premier ADR du projet établit un principe fondateur :

**User First.**

Toutes les futures décisions devront respecter ce principe.

La technologie n'est plus le centre du projet.

L'utilisateur le devient.

---

## Une nouvelle manière de développer

Cette séance nous a également conduits à définir notre méthode de travail.

Chaque séance devra désormais produire trois éléments complémentaires :

- une avancée de la documentation ;
- une décision d'architecture clairement formalisée ;
- une évolution concrète du code.

Cette approche garantit une progression équilibrée du projet et permet de conserver une trace de toutes les décisions importantes.

---

## Conclusion

À la fin de cette troisième séance, très peu de code a été écrit.

Pourtant, IAssistant n'a jamais autant progressé.

Son identité est désormais plus claire.

Sa philosophie est définie.

Ses premières décisions d'architecture sont formalisées.

Le projet possède désormais des fondations suffisamment solides pour commencer son véritable développement.

La prochaine séance marquera une nouvelle étape.

Pour la première fois, nous commencerons à donner vie à ces idées à travers les premières classes du projet.