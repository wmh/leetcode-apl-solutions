# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dado un array de enteros nums y un entero target, devuelve los índices de los dos números que suman target. Puedes asumir que cada entrada tendría exactamente una solución, y no puedes usar el mismo elemento dos veces. Puedes devolver la respuesta en cualquier orden.

## 💡 Solución APL

```apl
TwoSum ← {target←⍺ ⋄ arr←⍵ ⋄ sums←arr∘.+arr ⋄ mask←(sums=target)∧(∘.≠⍨⍳≢arr) ⋄ 2↑⍸mask}

⍝ Example usage:
⍝ 9 TwoSum 2 7 11 15    → 0 1
⍝ 6 TwoSum 3 2 4        → 1 2
⍝ 6 TwoSum 3 3          → 0 1
```

## 📝 Explicación

Crea el producto exterior (∘.+) del array consigo mismo para obtener todas las sumas posibles. Usa una máscara para excluir pares del mismo índice (∘.≠⍨⍳≢arr). Encuentra posiciones donde la suma es igual al objetivo con ⍸. Toma los primeros 2 índices con 2↑.

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
