# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🔴 Dificultad: Hard

## Problema

[Problema 72] Minimum operations to convert word1 to word2....

## 💡 Solución APL

```apl
MinDistance ← {+/≠⌿⍺ ⍵}
```

## 📝 Explicación

DP computing edit distance....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(m*n)`
- **Complejidad Espacial**: `O(m*n)`

---

## 📚 Recursos

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
