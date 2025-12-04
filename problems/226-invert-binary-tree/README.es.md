# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dada la raíz de un árbol binario, invierte el árbol y devuelve su raíz.

## 💡 Solución APL

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⍵[0],(∇⍵[2]),∇⍵[1]}

⍝ For nested representation:
⍝ Example usage:
⍝ InvertTree (4 (2 (1 ⍬ ⍬) (3 ⍬ ⍬)) (7 (6 ⍬ ⍬) (9 ⍬ ⍬)))
⍝ → (4 (7 (9 ⍬ ⍬) (6 ⍬ ⍬)) (2 (3 ⍬ ⍬) (1 ⍬ ⍬)))
```

## 📝 Explicación

Intercambia recursivamente los hijos izquierdo y derecho. Caso base: árbol vacío devuelve vacío. Caso recursivo: mantiene la raíz, intercambia los hijos recursando primero sobre el derecho y luego sobre el izquierdo.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(h)`

---

## 📚 Recursos

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
