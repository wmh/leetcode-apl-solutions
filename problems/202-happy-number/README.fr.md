# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Écrivez un algorithme pour déterminer si un nombre n est heureux. Un nombre heureux est un nombre défini par le processus suivant : En commençant par n'importe quel entier positif, remplacez le nombre par la somme des carrés de ses chiffres. Répétez le processus jusqu'à ce que le nombre soit égal à 1 (où il restera), ou qu'il boucle indéfiniment dans un cycle qui n'inclut pas 1. Les nombres pour lesquels ce processus se termine à 1 sont heureux. Renvoyez true si n est un nombre heureux, et false sinon.

## 💡 Solution APL

```apl
IsHappy ← {1∊⍵}
```

## 📝 Explication

APL solution for Happy Number. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(log n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
