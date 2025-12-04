# 371. Sum of Two Integers

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

[Problème 371] Add two integers without + or -....

## 💡 Solution APL

```apl
GetSum ← {
    ⍝ XOR for sum, AND for carry
    (⍺≠⍵)+2×⍺∧⍵
}
```

## 📝 Explication

APL solution for Sum of Two Integers. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(1)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #371](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
