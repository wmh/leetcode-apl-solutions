# 155. Min Stack

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 155] Design a stack with push, pop, top, and getMin in ...

## 💡 APL-Lösung

```apl
MinStack ← {
    stack ← ⍬
    minStack ← ⍬
    {stack,←⍵ ⋄ minStack,←⌊/stack}¨⍵
}
```

## 📝 Erklärung

APL solution for Min Stack. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(1)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #155](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
