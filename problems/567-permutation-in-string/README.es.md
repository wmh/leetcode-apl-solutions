# 567. Permutation in String

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

[Problema 567] Check if s2 contains a permutation of s1....

## 💡 Solución APL

```apl
CheckInclusion ← {
    (≢⍺)≤≢⍵:∨/{(∧/⍺∊⍵)∧∧/⍵∊⍺}¨(≢⍺)↑¨(≢⍵)↓¨⊂⍵
    0
}
```

## 📝 Explicación

Checks each substring of length |s1| for character match....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*m)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #567](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
