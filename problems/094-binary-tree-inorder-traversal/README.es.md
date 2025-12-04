# 94. Binary Tree Inorder Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dada la raíz de un árbol binario, devuelve el recorrido inorden de los valores de sus nodos.

## 💡 Solución APL

```apl
Inorder ← {0=≢⍵:⍬ ⋄ (∇⍵[1]),⍵[0],∇⍵[2]}

⍝ Example: (1 ⍬ (2 (3 ⍬ ⍬) ⍬)) → 1 3 2
```

## 📝 Explicación

Recursivo: recorre izquierda, visita raíz, recorre derecha. El caso base devuelve vacío para nodos nulos.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(h)`

---

## 📚 Recursos

- [LeetCode Problem #94](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
