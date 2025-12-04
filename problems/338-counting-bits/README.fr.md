# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné un entier n, renvoyez un tableau ans de longueur n + 1 tel que pour chaque i (0 <= i <= n), ans[i] est le nombre de 1 dans la représentation binaire de i.

## 💡 Solution APL

```apl
CountBits ← {+/¨(⍳⍵+1)⊤⍨¨32⍴¨2}

⍝ Example usage:
⍝ CountBits 2    → 0 1 1
⍝ CountBits 5    → 0 1 1 2 1 2
```

## 📝 Explication

Pour chaque nombre de 0 à n (⍳⍵+1), convertit en binaire en utilisant l'encodage base-2 (⊤⍨32⍴2), puis somme les bits (+/). L'opérateur ¨ applique l'opération à chaque nombre.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*log(n))`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
