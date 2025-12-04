# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Estás subiendo una escalera. Se necesitan n pasos para llegar a la cima. Cada vez puedes subir 1 o 2 escalones. ¿De cuántas formas distintas puedes subir a la cima?

## 💡 Solución APL

```apl
ClimbStairs ← {⊃{⍵,+/¯2↑⍵}⍣⍵⊢1 1}

⍝ Alternative using matrix power:
ClimbStairs2 ← {⊃⊃(2 2⍴1 1 1 0)+.×⍣⍵⊢2 2⍴1 0 0 1}

⍝ Example usage:
⍝ ClimbStairs 2    → 2
⍝ ClimbStairs 3    → 3
⍝ ClimbStairs 5    → 8
```

## 📝 Explicación

¡Esta es la secuencia de Fibonacci! Itera n veces con el operador de potencia (⍣⍵), comenzando con 1 1. Cada iteración agrega la suma de los últimos 2 números ({⍵,+/¯2↑⍵}). Toma el primer elemento (⊃) del resultado final.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
