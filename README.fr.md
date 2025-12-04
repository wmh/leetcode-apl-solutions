# 🧠 Solutions LeetCode en APL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> Résolution de plus de 100 problèmes classiques de LeetCode en utilisant APL (A Programming Language) - l'un des langages de programmation de tableaux les plus ésotériques et puissants.

> **⚠️ Contenu Généré par IA**: Ce projet a été créé avec une assistance IA significative. Voir [AI_GENERATED.md](./AI_GENERATED.md) pour les détails. Le code APL n'a pas été testé dans un interpréteur réel. Vérification recommandée avant utilisation.

**🌍 Langues**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🎯 À Propos de Ce Projet

Ce projet présente des solutions aux problèmes les plus populaires de LeetCode implémentées en **APL (A Programming Language)**, un langage unique connu pour:

- **Extrême Concision**: Exprime des algorithmes complexes en très peu de caractères
- **Orienté Tableaux**: Support natif pour des opérations puissantes sur les tableaux
- **Notation Mathématique**: Utilise des symboles Unicode spéciaux (⍵, ⍺, ⌽, ⊥, ∇, etc.)
- **Courbe d'Apprentissage Élevée**: Considéré comme l'un des langages les plus difficiles à maîtriser

### Pourquoi APL?

APL défie les paradigmes de programmation conventionnels et offre:
- Une façon complètement différente de penser aux algorithmes
- Des solutions élégantes qui révèlent souvent l'essence mathématique des problèmes
- Un ensemble riche d'opérations primitives pour la manipulation de tableaux
- Une signification historique en tant que l'un des premiers langages de haut niveau

## 📊 Couverture des Problèmes

| Difficulté | Nombre | Pourcentage |
|------------|--------|-------------|
| 🟢 Facile  | 40+    | ~35%        |
| 🟡 Moyen   | 50+    | ~50%        |
| 🔴 Difficile | 15+  | ~15%        |
| **Total**  | **100+** | **100%**  |

## 📝 Liste des Problèmes

### Problèmes en Vedette

#### #1 - Two Sum (Facile)
**Problème**: Étant donné un tableau d'entiers et une cible, renvoie les indices de deux nombres qui totalisent la cible.

**Solution APL**:
```apl
TwoSum ← {
    ⍝ ⍺: somme cible, ⍵: tableau
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}
```

**Explication**: Utilise le produit extérieur `∘.` pour générer toutes les sommes de paires possibles, puis `⍸` pour trouver les indices correspondants.

**Complexité**: Temps O(n²), Espace O(n²)

[📄 Solution Complète](problems/001-two-sum.json)

---

#### #136 - Single Number (Facile)
**Problème**: Trouve l'élément qui n'apparaît qu'une fois dans un tableau où tous les autres éléments apparaissent deux fois.

**Solution APL**:
```apl
SingleNumber ← {≠/⍵}
```

**Explication**: Réduction XOR - le one-liner le plus élégant! Exploite les propriétés XOR: a⊕a=0 et a⊕0=a.

**Complexité**: Temps O(n), Espace O(1)

[📄 Solution Complète](problems/136-single-number.json)

---

#### #206 - Reverse Linked List (Facile)
**Problème**: Inverse une liste chaînée simple.

**Solution APL**:
```apl
ReverseList ← {⌽⍵}
```

**Explication**: `⌽` est l'opérateur d'inversion d'APL - la solution la plus simple possible!

**Complexité**: Temps O(n), Espace O(1)

[📄 Solution Complète](problems/206-reverse-list.json)

---

### 📚 Tous les Problèmes

Parcourez toutes les solutions de problèmes dans le répertoire [`problems/`](problems/). Chaque problème a son propre fichier JSON avec:
- Description du problème (7 langues)
- Code de solution APL
- Explication détaillée (7 langues)
- Analyse de complexité temporelle et spatiale

**Index**: Voir [`problems/index.json`](problems/index.json) pour la liste complète.

## 🚀 Fonctionnalités

- ✅ **100+ Problèmes Classiques**: Couverture complète des problèmes les plus importants de LeetCode
- ✅ **Solutions APL**: Implémentations uniques utilisant des opérations puissantes sur les tableaux
- ✅ **Explications Détaillées**: Chaque solution inclut une analyse de complexité
- ✅ **7 Langues**: Documentation complète en anglais, chinois, japonais, espagnol, allemand, français
- ✅ **Structure Modulaire**: Chaque problème dans son propre fichier JSON
- ✅ **Orientation Éducative**: Apprenez la programmation de tableaux à travers des exemples pratiques
- ✅ **Open Source**: Licence MIT, contributions bienvenues

## 💻 Comment Utiliser

### Parcourir sur GitHub

Parcourez simplement ce dépôt sur GitHub! Tous les problèmes sont documentés dans:
- **Fichiers README**: Aperçu et problèmes en vedette (7 langues)
- **Répertoire problems/**: Fichiers de problèmes individuels avec solutions complètes

### Cloner Localement

```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# Voir un problème spécifique
cat problems/001-two-sum.json | jq '.'

# Lister tous les problèmes
cat problems/index.json | jq '.'
```

### Essayer les Solutions

Pour exécuter réellement le code APL, vous aurez besoin d'un interpréteur APL:

1. **En ligne**: Visitez [TryAPL.org](https://tryapl.org/)
2. **Local**: Installez [Dyalog APL](https://www.dyalog.com/download-zone.htm)
3. **GNU APL**: Utilisez `apt install gnu-apl` (Linux) ou `brew install gnu-apl` (macOS)

## 📂 Structure du Projet

```
leetcode-apl-solutions/
├── README.md                  # Documentation en anglais
├── README.zh-TW.md           # Chinois traditionnel
├── README.zh-CN.md           # Chinois simplifié
├── README.ja.md              # Documentation en japonais
├── README.es.md              # Documentation en espagnol
├── README.de.md              # Documentation en allemand
├── README.fr.md              # Documentation en français
├── problems/                  # Répertoire des problèmes
│   ├── index.json            # Index de tous les problèmes
│   ├── 001-two-sum.json      # Problème individuel
│   ├── 136-single-number.json
│   ├── 206-reverse-list.json
│   └── ...                   # Plus de problèmes
├── AI_GENERATED.md           # Avertissement IA
├── LICENSE                   # Licence MIT
└── .gitignore               # Configuration Git
```

## 🤝 Contribuer

Les contributions sont bienvenues! Vous pouvez aider de la manière suivante:

1. **Ajouter Plus de Problèmes**: Implémentez des problèmes LeetCode supplémentaires en APL
2. **Améliorer les Solutions**: Optimisez les solutions APL existantes
3. **Corriger les Bugs**: Signalez et corrigez tout problème trouvé
4. **Traductions**: Aidez à améliorer les traductions linguistiques
5. **Documentation**: Améliorez les explications des problèmes

## 📚 Ressources

### Apprendre APL
- [APL Wiki](https://aplwiki.com/) - Documentation complète d'APL
- [Tutoriel Dyalog APL](https://tutorial.dyalog.com/) - Tutoriel officiel Dyalog
- [APL Cart](https://aplcart.info/) - Idiomes APL consultables
- [Try APL](https://tryapl.org/) - Interpréteur APL en ligne

### LeetCode
- [Problèmes LeetCode](https://leetcode.com/problemset/all/) - Liste officielle des problèmes
- [Questions d'Entretien Top](https://leetcode.com/problem-list/top-interview-questions/)

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour les détails.

## 🙏 Remerciements

- **Kenneth E. Iverson** - Créateur d'APL
- **LeetCode** - Pour fournir d'excellents problèmes algorithmiques
- **Dyalog Ltd** - Pour la maintenance et le développement d'APL
- **Communauté APL** - Pour maintenir ce beau langage vivant

## 📧 Contact

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [Signaler des problèmes ou des suggestions](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Historique des Étoiles

Si vous trouvez ce projet utile, veuillez considérer lui donner une étoile! ⭐

---

**Fait avec ❤️ et beaucoup de ⍵, ⍺, ⌽, et ∇**

*"APL est une erreur, menée à la perfection."* - Edsger W. Dijkstra

Malgré les critiques, APL reste l'un des langages les plus élégants et puissants pour la manipulation de tableaux! 🎯
