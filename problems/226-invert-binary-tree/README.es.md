# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Dada la raíz de un árbol binario, invierte el árbol y devuelve su raíz.

## 💡 Solución APL

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⌽∇¨⍵}
```

## 📝 Explicación

APL solution for Invert Binary Tree. Uses reverse (⌽) to flip array elements. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(h)`

---

## 📚 Recursos

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
