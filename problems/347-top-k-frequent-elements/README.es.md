# 347. Top K Frequent Elements

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

[Problema 347] Return the k most frequent elements....

## 💡 Solución APL

```apl
TopKFrequent ← {
    k ← ⍺
    freq ← {⍵,≢⍵}⌸⍵
    k↑freq[⍒freq[;2];1]
}
```

## 📝 Explicación

Groups elements by frequency and takes top k....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*log(n))`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #347](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
