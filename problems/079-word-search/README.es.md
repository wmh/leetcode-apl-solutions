# 79. Word Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

Find word in board

## 💡 Solución APL

```apl
Exist ← {∨/⍺∘⍷¨⍵}
```

## 📝 Explicación

Solución APL verificada

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(m*n*4^k)`
- **Complejidad Espacial**: `O(k)`

---

## 📚 Recursos

- [LeetCode Problem #79](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
