# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Dada una cadena s que contiene solo los caracteres '(', ')', '{', '}', '[' y ']', determina si la cadena de entrada es válida. Una cadena de entrada es válida si: Los corchetes de apertura deben cerrarse con el mismo tipo de corchetes. Los corchetes de apertura deben cerrarse en el orden correcto. Cada corchete de cierre tiene un corchete de apertura correspondiente del mismo tipo.

## 💡 Solución APL

```apl
IsValid ← {0=+/(⍵='(')-⍵=')'}
```

## 📝 Explicación

APL solution for Valid Parentheses. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
