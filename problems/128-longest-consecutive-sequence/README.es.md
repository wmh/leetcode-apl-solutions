# 128. Longest Consecutive Sequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

[Problema 128] Find the length of the longest consecutive element...

## 💡 Solución APL

```apl
LongestConsecutive ← {
    ⍝ Find longest run
    sorted ← ∪⍵[⍋⍵]
    max ← ⌈/1,+/¨2=/¨1↓¨⊆sorted
    max
}
```

## 📝 Explicación

APL solution for Longest Consecutive Sequence. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses unique (∪) to remove duplicate elements. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*log(n))`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #128](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
