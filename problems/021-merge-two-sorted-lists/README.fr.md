# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

On vous donne les têtes de deux listes chaînées triées list1 et list2. Fusionnez les deux listes en une seule liste triée. La liste doit être créée en épissant ensemble les nœuds des deux premières listes. Renvoyez la tête de la liste chaînée fusionnée.

## 💡 Solution APL

```apl
MergeTwoLists ← {⍺[⍋⍺,⍵],⍵[⍋⍺,⍵]}

⍝ Simpler version:
MergeTwoLists2 ← {(⍺,⍵)[⍋⍺,⍵]}

⍝ Example usage:
⍝ 1 2 4 MergeTwoLists2 1 3 4    → 1 1 2 3 4 4
⍝ ⍬ MergeTwoLists2 0            → 0
⍝ ⍬ MergeTwoLists2 ⍬            → ⍬
```

## 📝 Explication

Concatène les deux listes (⍺,⍵) puis trie par ordre croissant (⍋). L'ordre croissant renvoie les indices qui trieraient le tableau. La version 2 est plus propre : concaténer puis indexer par positions triées.

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
