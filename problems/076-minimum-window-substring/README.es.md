# 76. Minimum Window Substring

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🔴 Dificultad: Hard

## Problema

[Problema 76] Find minimum window in s which contains all charac...

## 💡 Solución APL

```apl
MinWindow ← {
    ⍝ Sliding window with character count
    windows ← {⍵↑⍨⊃⍸(∧/⍺∊⍵)⍵}
    ⊃⌊/≢¨windows
}
```

## 📝 Explicación

Maintains character counts in sliding window....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*m)`
- **Complejidad Espacial**: `O(m)`

---

## 📚 Recursos

- [LeetCode Problem #76](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
