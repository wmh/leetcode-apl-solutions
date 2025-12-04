# 167. Two Sum II

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

[Problema 167] Find two numbers in sorted array that add up to ta...

## 💡 Solución APL

```apl
TwoSumII ← {
    ⍝ Two pointer approach
    indices ← ⍸⍺=⍵+⌽⍵
    2↑indices
}
```

## 📝 Explicación

Uses two pointers from both ends....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #167](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
