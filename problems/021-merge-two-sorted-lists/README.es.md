# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Se te dan las cabezas de dos listas enlazadas ordenadas list1 y list2. Fusiona las dos listas en una lista ordenada. La lista debe hacerse empalmando juntos los nodos de las primeras dos listas. Devuelve la cabeza de la lista enlazada fusionada.

## 💡 Solución APL

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 Explicación

Concatena ambas listas (⍺,⍵) luego ordena por grado ascendente (⍋). El grado ascendente devuelve índices que ordenarían el array. La versión 2 es más limpia: concatenar luego indexar por posiciones ordenadas.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O((n+m)*log(n+m))`
- **Complejidad Espacial**: `O(n+m)`

---

## 📚 Recursos

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
