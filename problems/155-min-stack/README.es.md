# 155. Min Stack

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

[Problema 155] Design a stack with push, pop, top, and getMin in ...

## 💡 Solución APL

```apl
MinStack ← {
    stack ← ⍬
    minStack ← ⍬
    {stack,←⍵ ⋄ minStack,←⌊/stack}¨⍵
}
```

## 📝 Explicación

Maintains auxiliary stack for minimums....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(1)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #155](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
