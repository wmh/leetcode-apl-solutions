# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné un tableau nums contenant n nombres distincts dans la plage [0, n], renvoyez le seul nombre de la plage qui manque dans le tableau.

## 💡 Solution APL

```apl
MissingNumber ← {(((≢⍵)×(≢⍵)+1)÷2)-+/⍵}

⍝ Example usage:
⍝ MissingNumber 3 0 1    → 2
⍝ MissingNumber 0 1      → 2
⍝ MissingNumber 9 6 4 2 3 5 7 0 1    → 8
```

## 📝 Explication

Utilise la formule pour la somme de 0 à n : n×(n+1)÷2. Calcule la somme attendue moins la somme réelle. Le résultat est le nombre manquant. (≢⍵) donne n, donc nous calculons n×(n+1)÷2 - (+/⍵) où +/⍵ est la somme des éléments.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
