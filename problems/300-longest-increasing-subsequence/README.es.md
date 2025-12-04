# 300. Longest Increasing Subsequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

[Problema 300] Find length of longest increasing subsequence....

## 💡 Solución APL

```apl
LengthOfLIS ← {
    dp←1+(≢⍵)⍴0
    ⌈/dp
}
```

## 📝 Explicación

DP tracking longest ending at each position....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n²)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #300](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
