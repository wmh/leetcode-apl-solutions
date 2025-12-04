# 102. Binary Tree Level Order Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

[Problema 102] Return level order traversal....

## 💡 Solución APL

```apl
LevelOrder ← {
    ⍝ BFS approach
    levels←{⍵⊂⍨⍳≢⍵}⍵
    levels
}
```

## 📝 Explicación

Groups nodes by level....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #102](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
