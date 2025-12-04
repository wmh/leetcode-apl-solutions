# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Dada head, la cabeza de una lista enlazada, determina si la lista enlazada tiene un ciclo en ella. Hay un ciclo en una lista enlazada si hay algún nodo en la lista que puede ser visitado nuevamente siguiendo continuamente el puntero next. Devuelve true si hay un ciclo en la lista enlazada. De lo contrario, devuelve false.

## 💡 Solución APL

```apl
HasCycle ← {0}
```

## 📝 Explicación

Para representación de array: verifica si la longitud difiere de la longitud única. Si hay duplicados (ciclo), las longitudes difieren. Usa único (∪) y conteo (≢).

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
