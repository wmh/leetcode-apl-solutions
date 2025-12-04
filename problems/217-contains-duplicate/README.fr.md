# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné un tableau d'entiers nums, renvoyez true si une valeur apparaît au moins deux fois dans le tableau, et renvoyez false si chaque élément est distinct.

## 💡 Solution APL

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}

⍝ Example usage:
⍝ ContainsDuplicate 1 2 3 1    → 1 (true)
⍝ ContainsDuplicate 1 2 3 4    → 0 (false)
⍝ ContainsDuplicate 1 1 1 3 3 4 3 2 4 2    → 1 (true)
```

## 📝 Explication

Compare la longueur du tableau (≢⍵) avec la longueur des éléments uniques (≢∪⍵). S'ils diffèrent, il doit y avoir des doublons. L'opérateur ≢ donne la longueur, ∪ donne des éléments uniques et ≠ vérifie s'ils ne sont pas égaux.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
