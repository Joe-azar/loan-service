# Service Web Composite pour l'Évaluation de Demande de Prêt Immobilier

## Description
Ce projet implémente un **Service Web Composite** pour automatiser le processus d'évaluation des demandes de prêt immobilier. Le système utilise une architecture orientée services (SOA), où plusieurs services spécialisés (extraction d'informations, vérification de solvabilité, évaluation de la propriété et décision d'approbation) sont coordonnés par un **Service Composite**.

Le projet a été développé en Python en utilisant les bibliothèques **Spyne** pour exposer les services web via SOAP, **Tkinter** pour l'interface graphique, et **SQLite** pour la gestion des données.

## Fonctionnalités
- **Soumission des demandes de prêt** via une interface graphique ou un dépôt de fichier.
- **Extraction automatique des informations** de la demande (nom, adresse, montant, etc.).
- **Vérification de la solvabilité** du client en fonction de ses revenus et dépenses.
- **Évaluation de la valeur de la propriété** soumise dans la demande de prêt.
- **Prise de décision d'approbation ou de rejet** en fonction des résultats des étapes précédentes.
- **Orchestration des services** via un Service Composite.

## Structure du Projet
```bash
project_root/
├── data/                       # Dossier où les fichiers de demande de prêt sont déposés
├── services/                   # Contient les services indépendants
│   ├── information_extraction_service.py
│   ├── solvency_check_service.py
│   ├── property_evaluation_service.py
│   ├── approval_decision_service.py
├── main.py                     # Script principal qui lance les services et l'interface
├── watchdog_trigger.py          # Surveille les fichiers déposés dans 'data/'
├── web_composite_service.py     # Service composite orchestrant les autres services
└── README.md                   # Documentation du projet
```

## Services Exposés

### 1. **Service d'Extraction d'Informations**
- **Description** : Extrait les informations pertinentes de la demande (nom, adresse, montant du prêt, etc.).
- **Entrée** : Demande de prêt en texte brut (SOAP).
- **Sortie** : Dictionnaire contenant les informations extraites.

### 2. **Service de Vérification de Solvabilité**
- **Description** : Calcule le score de solvabilité du client en fonction de ses revenus, ses dépenses et son score de crédit.
- **Entrée** : Nom du client, revenus mensuels, dépenses mensuelles.
- **Sortie** : Score de solvabilité.

### 3. **Service d'Évaluation de la Propriété**
- **Description** : Évalue la valeur de la propriété soumise dans la demande et vérifie sa conformité légale.
- **Entrée** : Description de la propriété, adresse.
- **Sortie** : Valeur estimée de la propriété.

### 4. **Service de Décision d'Approbation**
- **Description** : Prend une décision d'approbation ou de rejet du prêt en fonction du score de solvabilité et de la valeur de la propriété.
- **Entrée** : Score de solvabilité, valeur de la propriété, montant du prêt.
- **Sortie** : Décision d'approbation ou de rejet.

### 5. **Service Composite**
- **Description** : Orchestrateur qui coordonne les autres services pour fournir une évaluation complète de la demande de prêt.

## Installation

### Prérequis
- **Python 3.7+**
- Bibliothèques Python requises :
  ```bash
  pip install spyne watchdog
  ```

### Étapes
1. Clonez ce dépôt dans votre répertoire local.
   ```bash
   git clone https://github.com/Joe-azar/loan-service.git
   cd loan-service
   ```

2. Installez les bibliothèques nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez le script principal `main.py` pour démarrer tous les services et l'interface graphique :
   ```bash
   python main.py
   ```

## Utilisation

### Interface Graphique
L'interface graphique permet de :
- Soumettre une nouvelle demande de prêt en remplissant un formulaire.
- Déposer directement un fichier contenant une demande de prêt dans le répertoire surveillé.

### Dépôt de Fichier
Placez un fichier texte contenant les informations de la demande dans le dossier `data/`. Le fichier doit avoir un format similaire à celui-ci :
```
Nom du Client: John Doe
Adresse: 123 Rue de Paris, 75001 Paris, France
Email: john.doe@email.com
Numéro de Téléphone: +33 123 456 789
Montant du Prêt Demandé: 200000 EUR
Durée du Prêt: 20 ans
Description de la Propriété: Maison à deux étages avec jardin
Revenu Mensuel: 5000 EUR
Dépenses Mensuelles: 3000 EUR
```

Le système détectera automatiquement le fichier et traitera la demande.

## Base de Données
Une base de données SQLite est utilisée pour stocker les informations relatives aux demandes de prêt et aux décisions prises.
- **Table `loan_requests`** : Contient les informations extraites des demandes.
- **Table `loan_performance`** : Stocke les performances des décisions d'approbation.

## Tests et Résultats
Le projet a été testé avec différents scénarios de demande de prêt. Les résultats des tests ont montré que le système peut :
- Extraire correctement les informations des demandes.
- Calculer un score de solvabilité précis.
- Évaluer la valeur d'une propriété fictive.
- Prendre une décision d'approbation ou de rejet de la demande de prêt.

## Améliorations Futures
- Intégration de véritables API de solvabilité et d'évaluation immobilière.
- Déploiement des services sur une plateforme cloud pour un accès à distance.
- Amélioration de l'interface graphique pour plus d'ergonomie.

## Auteurs
- **Joe Azar** - Développeur du projet.

## Encadré par
- **Monsieur Yehia Taher** - Professeur.
