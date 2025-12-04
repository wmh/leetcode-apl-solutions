# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Écrivez une fonction qui prend la représentation binaire d'un entier positif et renvoie le nombre de bits définis qu'il a (également connu sous le nom de poids de Hamming).

## 💡 Solution APL

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 Explication

Convertit le nombre en binaire 32 bits en utilisant l'encodage (⊤⍨32⍴2), puis somme les bits avec +/. L'opérateur d'encodage ⊤ convertit vers la base spécifiée.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(1)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
