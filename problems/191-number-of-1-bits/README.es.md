# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Escribe una función que tome la representación binaria de un entero positivo y devuelva el número de bits establecidos que tiene (también conocido como peso de Hamming).

## 💡 Solución APL

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 Explicación

Convierte el número a binario de 32 bits usando codificación (⊤⍨32⍴2), luego suma los bits con +/. El operador de codificación ⊤ convierte a la base especificada.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(1)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
