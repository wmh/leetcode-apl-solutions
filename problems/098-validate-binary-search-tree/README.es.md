# 98. Validate Binary Search Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

[Problema 98] Determine if tree is valid BST....

## 💡 Solución APL

```apl
IsValidBST ← {
    sorted←⍵[⍋⍵]
    ∧/sorted=⍵
}
```

## 📝 Explicación

APL solution for Validate Binary Search Tree. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #98](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
