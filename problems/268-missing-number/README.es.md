# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dado un array nums que contiene n números distintos en el rango [0, n], devuelve el único número en el rango que falta en el array.

## 💡 Solución APL

```apl
MissingNumber ← {(((≢⍵)×(≢⍵)+1)÷2)-+/⍵}

⍝ Example usage:
⍝ MissingNumber 3 0 1    → 2
⍝ MissingNumber 0 1      → 2
⍝ MissingNumber 9 6 4 2 3 5 7 0 1    → 8
```

## 📝 Explicación

Utiliza la fórmula para la suma de 0 a n: n×(n+1)÷2. Calcula la suma esperada menos la suma real. El resultado es el número que falta. (≢⍵) da n, así que calculamos n×(n+1)÷2 - (+/⍵) donde +/⍵ es la suma de elementos.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
