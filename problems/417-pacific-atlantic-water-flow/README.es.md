# 417. Pacific Atlantic Water Flow

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

[Problema 417] Find cells from which water can flow to both ocean...

## 💡 Solución APL

```apl
PacificAtlantic ← {
    ⍝ DFS from both coasts
    pacific∩atlantic
}
```

## 📝 Explicación

DFS from both ocean borders....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(m*n)`
- **Complejidad Espacial**: `O(m*n)`

---

## 📚 Recursos

- [LeetCode Problem #417](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
