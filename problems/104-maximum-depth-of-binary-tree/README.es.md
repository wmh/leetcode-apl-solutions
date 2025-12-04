# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dada la raíz de un árbol binario, devuelve su profundidad máxima. La profundidad máxima de un árbol binario es el número de nodos a lo largo del camino más largo desde el nodo raíz hasta el nodo hoja más lejano.

## 💡 Solución APL

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}

⍝ For nested arrays:
⍝ Example usage:
⍝ MaxDepth (3 (9 ⍬ ⍬) (20 (15 ⍬ ⍬) (7 ⍬ ⍬)))    → 3
⍝ MaxDepth (1 ⍬ (2 ⍬ ⍬))                          → 2
```

## 📝 Explicación

Cuenta recursivamente la profundidad. Caso base: árbol vacío tiene profundidad 0. Caso recursivo: 1 + profundidad máxima de los hijos. Usa autorreferencia (∇) para recurrir sobre cada hijo, luego toma el máximo con ⌈/.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(h)`

---

## 📚 Recursos

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
