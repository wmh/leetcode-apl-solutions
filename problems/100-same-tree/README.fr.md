# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Étant donné les racines de deux arbres binaires p et q, écrivez une fonction pour vérifier s'ils sont identiques ou non. Deux arbres binaires sont considérés comme identiques s'ils sont structurellement identiques et que les nœuds ont la même valeur.

## 💡 Solution APL

```apl
IsSameTree ← {⍺≡⍵}
```

## 📝 Explication

Utilise l'opérateur de correspondance (≡) qui renvoie 1 si les tableaux sont identiques en structure et en valeurs, 0 sinon. C'est la solution la plus simple possible - juste un symbole !

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
