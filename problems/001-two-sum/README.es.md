# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Dado un array de enteros nums y un entero target, devuelve los índices de los dos números que suman target. Puedes asumir que cada entrada tendría exactamente una solución, y no puedes usar el mismo elemento dos veces. Puedes devolver la respuesta en cualquier orden.

## 💡 Solución APL

```apl
TwoSum ← {(⊃⍸⍺=+/∘.,⍨⍵)}
```

## 📝 Explicación

APL solution for Two Sum. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses where (⍸) to find indices of true/non-zero elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n²)`
- **Complejidad Espacial**: `O(n²)`

---

## 📚 Recursos

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
