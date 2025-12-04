# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Vous montez un escalier. Il faut n marches pour atteindre le sommet. Chaque fois, vous pouvez monter 1 ou 2 marches. De combien de façons distinctes pouvez-vous atteindre le sommet ?

## 💡 Solution APL

```apl
ClimbStairs ← {⊃(+⌿⍣(⍵-1))1 1}
```

## 📝 Explication

C'est la suite de Fibonacci ! Itère n fois avec l'opérateur de puissance (⍣⍵), en commençant par 1 1. Chaque itération ajoute la somme des 2 derniers nombres ({⍵,+/¯2↑⍵}). Prend le premier élément (⊃) du résultat final.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
