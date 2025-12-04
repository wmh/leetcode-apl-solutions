# 704. Binary Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

[Problema 704] Search for target value in sorted array....

## 💡 Solución APL

```apl
BinarySearch ← {
    target←⍺
    (target∊⍵)×⊃⍸target=⍵
}
```

## 📝 Explicación

Standard binary search....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(log n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #704](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
