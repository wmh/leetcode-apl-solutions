# 15. 3Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

Find all unique triplets that sum to zero

## 💡 Solución APL

```apl
ThreeSum ← {∪↓(⊂⍵)[⍸0=+⌿⍵∘.+⍵∘.+⍵]}
```

## 📝 Explicación

APL solution for 3Sum. Uses outer product (∘.) to create matrix of all pair combinations. Uses where (⍸) to find indices of true/non-zero elements. Uses unique (∪) to remove duplicate elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n²)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #15](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
