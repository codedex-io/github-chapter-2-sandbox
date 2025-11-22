
# 🎯 Leçon Git - Les Branches

## 📚 Objectif du Jour
Apprendre le fonctionnement des **branches Git**, comprendre leur utilité et maîtriser la création de **pull requests**.



## 🌿 C'est quoi une branche ?

Une branche est une **ligne de développement indépendante** qui permet de :

- 🔧 Travailler sur de nouvelles fonctionnalités
- 🐛 Corriger des bugs
- 🧪 Expérimenter des idées
- 🚀 Développer sans affecter la version principale



## 💡 Pourquoi utiliser des branches ?

| Avantage | Description |
|----------|-------------|
| ✅ **Isolation** | Travail sans risque sur le code principal |
| ✅ **Collaboration** | Travail en parallèle avec l'équipe |
| ✅ **Organisation** | Historique propre et structuré |
| ✅ **Sécurité** | Branche principale toujours stable |

---
### Nous sommes le 22/11/2025

Ici commence mes modifications de ce fichier. La leçon continue et le but est de maîtriser **les merges **ainsi que les** Pull request (PR)**
## 🛠️ Commandes Essentielles

### 📋 Gestion des branches
```bash
# Créer une nouvelle branche
git branch feature/ma-nouvelle-fonctionnalite

# Se déplacer sur une branche
git checkout feature/ma-nouvelle-fonctionnalite

# Créer et se déplacer directement
git checkout -b feature/ma-nouvelle-fonctionnalite

# Lister toutes les branches
git branch

# Supprimer une branche
git branch -d feature/branche-terminee

### 🔄 Synchronisation

# Pousser une branche sur GitHub
git push origin feature/ma-nouvelle-fonctionnalite

# Récupérer les dernières modifications
git pull origin main
