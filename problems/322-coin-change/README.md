# 322. Coin Change

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Min coins for amount

## 💡 APL Solution

```apl
CoinChange ← {⌊⍵÷⌊/⍺}
```

## 📝 Explanation

APL solution for Coin Change. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(amount*n)`
- **Space Complexity**: `O(amount)`

---

## 📚 Resources

- [LeetCode Problem #322](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
