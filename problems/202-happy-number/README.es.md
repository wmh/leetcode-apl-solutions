# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Escribe un algoritmo para determinar si un número n es feliz. Un número feliz es un número definido por el siguiente proceso: Comenzando con cualquier entero positivo, reemplaza el número por la suma de los cuadrados de sus dígitos. Repite el proceso hasta que el número sea igual a 1 (donde permanecerá), o haga un bucle infinito en un ciclo que no incluya 1. Aquellos números para los cuales este proceso termina en 1 son felices. Devuelve true si n es un número feliz, y false si no.

## 💡 Solución APL

```apl
IsHappy ← {n←⍵ ⋄ seen←⍬ ⋄ {n∊seen:0 ⋄ 1=n:1 ⋄ seen,←n ⋄ n←+/((10⊥⍣¯1⊢n)*2) ⋄ ∇⍬}⍬}

⍝ Simpler iterative check:
IsHappy2 ← {1∊20{+/(10⊥⍣¯1⊢⍵)*2}⍣⍺⊢⍵}

⍝ Example usage:
⍝ IsHappy2 19    → 1
⍝ IsHappy2 2     → 0
```

## 📝 Explicación

Versión 2: Itera 20 veces aplicando la suma de cuadrados de dígitos. Si 1 aparece en los resultados, es feliz. Usa codificación inversa (10⊥⍣¯1) para obtener dígitos, los eleva al cuadrado y suma.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(log n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
