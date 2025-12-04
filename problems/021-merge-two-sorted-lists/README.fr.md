# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

On vous donne les têtes de deux listes chaînées triées list1 et list2. Fusionnez les deux listes en une seule liste triée. La liste doit être créée en épissant ensemble les nœuds des deux premières listes. Renvoyez la tête de la liste chaînée fusionnée.

## 💡 Solution APL

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 Explication

APL solution for Merge Two Sorted Lists. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O((n+m)*log(n+m))`
- **Complexité Spatiale**: `O(n+m)`

---

## 📚 Ressources

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
