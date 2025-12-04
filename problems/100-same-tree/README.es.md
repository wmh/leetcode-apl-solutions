# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dadas las raíces de dos árboles binarios p y q, escribe una función para verificar si son iguales o no. Dos árboles binarios se consideran iguales si son estructuralmente idénticos y los nodos tienen el mismo valor.

## 💡 Solución APL

```apl
SameTree ← {⍺≡⍵}

⍝ For arrays representing trees:
⍝ Example usage:
⍝ (1 2 3) SameTree (1 2 3)    → 1
⍝ (1 2) SameTree (1 ⍬ 2)     → 0
⍝ (1 2 1) SameTree (1 1 2)   → 0
```

## 📝 Explicación

Utiliza el operador de coincidencia (≡) que devuelve 1 si los arrays son idénticos en estructura y valores, 0 en caso contrario. ¡Esta es la solución más simple posible: solo un símbolo!

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
