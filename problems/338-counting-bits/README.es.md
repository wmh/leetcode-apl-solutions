# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Dado un entero n, devuelve un array ans de longitud n + 1 tal que para cada i (0 <= i <= n), ans[i] es el número de 1 en la representación binaria de i.

## 💡 Solución APL

```apl
CountBits ← {+/¨2⊥⍣¯1¨⍳⍵+1}
```

## 📝 Explicación

APL solution for Counting Bits. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses iota (⍳) to generate index ranges or find element positions. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*log(n))`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
