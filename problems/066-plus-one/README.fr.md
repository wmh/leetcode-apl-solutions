# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

On vous donne un grand entier représenté sous forme de tableau d'entiers digits, où chaque digits[i] est le i-ème chiffre de l'entier. Les chiffres sont ordonnés du plus significatif au moins significatif dans l'ordre de gauche à droite. Le grand entier ne contient aucun 0 en tête. Incrémentez le grand entier d'un et renvoyez le tableau de chiffres résultant.

## 💡 Solution APL

```apl
PlusOne ← {10⊥⍣¯1⊢1+10⊥⍵}

⍝ Example usage:
⍝ PlusOne 1 2 3    → 1 2 4
⍝ PlusOne 4 3 2 1  → 4 3 2 2
⍝ PlusOne 9        → 1 0
```

## 📝 Explication

Convertit les chiffres en nombre en utilisant le décodage (10⊥⍵), ajoute 1, puis reconvertit en chiffres en utilisant l'encodage (10⊥⍣¯1). L'opérateur ⊥ décode depuis la base 10, ⊥⍣¯1 encode en chiffres de base 10.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
