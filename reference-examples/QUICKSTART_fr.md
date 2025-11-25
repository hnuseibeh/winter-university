# 🚀 Guide de Démarrage Rapide
# Winter School 2025 - Tableau de Bord des Crises Économiques et Sociales

## Installation et Exécution

### 1. Télécharger le Projet
```bash
# Cloner le dépôt depuis GitHub
git clone [YOUR_REPO_URL]

# Ou télécharger le fichier ZIP et le décompresser
# Puis naviguer vers le dossier
cd winter-school-econ-social-crises
```

### 2. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer le Tableau de Bord
```bash
streamlit run app.py
```

### 4. Ouvrir le Navigateur
Ouvrez votre navigateur sur: `http://localhost:8501`

---

## 📊 Qu'est-ce qui est Inclus?

### 8 Pages Interactives:

1. **📊 Indicateurs Macroéconomiques** - PIB, chômage, inflation (Palestine & Maroc)
2. **👥 Chômage des Jeunes** - Tendances du Maroc (2015-2024) [Bilingue]
3. **🎓 Inadéquation Éducation-Emploi** - Analyse Palestine par domaine d'études avec scénarios
4. **🌾 Stress Agricole** - Rendements Maroc, précipitations, prix alimentaires [Bilingue]
5. **🚧 Surveillance des Points de Contrôle** - Analyse temps d'attente à Jérusalem [Bilingue]
6. **🏪 Micro-Entreprises** - Vulnérabilité des entreprises à Jérusalem [Bilingue]
7. **💰 Budgets des Ménages** - Scénarios de chocs en Palestine (hausse prix carburant/nourriture)
8. **🔍 Explorateur de Données** - Outil générique de visualisation CSV

### 10 Ensembles de Données:

**Indicateurs Macro:**
- Indicateurs économiques (PIB, chômage, inflation)

**Maroc:**
- Chômage des jeunes (national/urbain/rural)
- Stress agricole (rendement, précipitations, prix)
- Indice des prix alimentaires (mensuel par région)

**Palestine:**
- Chômage par domaine d'études
- Données éducation-emploi des jeunes
- Scénarios de chocs budgétaires des ménages

**Jérusalem:**
- Temps d'attente aux points de contrôle
- Vulnérabilité des micro-entreprises
- Vulnérabilité des quartiers

---

## 🎯 Premiers Pas

### Pour les Débutants:

1. **Commencez par les Indicateurs Macro** 📊
   - Visualisez les tendances économiques générales
   - Comparez Palestine et Maroc

2. **Explorez le Chômage des Jeunes** 👥
   - Recherchez l'écart urbain-rural
   - Observez les tendances dans le temps

3. **Essayez les Scénarios Éducation-Emploi** 🎓
   - Ajustez les taux de croissance offre/demande
   - Voyez les projections futures

4. **Utilisez l'Explorateur de Données** 🔍
   - Examinez n'importe quel ensemble de données interactivement
   - Exportez les données pour analyse externe

---

## 💡 Pour les Étudiants

### Ce que Vous Pouvez Faire:

- ✅ Utiliser les filtres pour explorer les données
- ✅ Lire les questions de discussion sur chaque page
- ✅ Exporter les données pour analyse supplémentaire
- ✅ Partager les résultats avec vos camarades
- ✅ Développer des recommandations politiques
- ✅ Ajouter vos propres fichiers CSV dans l'explorateur de données

### Pages Bilingues:

Quatre pages supportent l'arabe et l'anglais:
- 👥 Chômage des Jeunes (Maroc)
- 🌾 Stress Agricole (Maroc)
- 🚧 Surveillance des Points de Contrôle (Jérusalem)
- 🏪 Micro-Entreprises (Jérusalem)

---

## ❓ Dépannage

### Problème: Erreur "Module not found"
**Solution:** Exécutez `pip install -r requirements.txt` à nouveau

### Problème: Erreur "Data file not found"
**Solution:** Assurez-vous d'exécuter `streamlit run app.py` depuis le dossier racine

### Problème: "Port already in use"
**Solution:** Utilisez un port différent:
```bash
streamlit run app.py --server.port 8502
```

### Problème: Version Python
**Solution:** Vous avez besoin de Python 3.8 ou supérieur
```bash
python --version  # Vérifier la version
```

---

## 📚 Ressources Supplémentaires

- **Documentation complète:** [README.md](README.md)
- **Licence:** [LICENSE](LICENSE)
- **Version multilingue:** [README_MULTILINGUAL.md](README_MULTILINGUAL.md)

---

## 🎓 Conseils d'Apprentissage

1. **Commencez Simple** - Explorez une page à la fois
2. **Comparez les Données** - Recherchez des modèles à travers différentes pages
3. **Posez des Questions** - Utilisez les questions de discussion comme point de départ
4. **Expérimentez** - Changez les filtres et voyez ce qui se passe
5. **Partagez** - Discutez des résultats avec vos camarades

---

## 🌟 Fonctionnalités Clés

### Visualisations Interactives
- Graphiques en lignes temporelles
- Graphiques à barres comparatifs
- Nuages de points
- Cartes thermiques
- Graphiques circulaires

### Outils d'Analyse
- Filtres par pays/région
- Sélection d'indicateurs
- Curseurs de scénarios
- Filtrage de texte
- Exportation CSV

### Contenu Éducatif
- Questions de discussion
- Prompts de recommandations politiques
- Informations clés
- Explications bilingues

---

**Prêt à explorer les données de crises économiques et sociales!** 🎓📊

Fait avec ❤️ pour l'éducation
