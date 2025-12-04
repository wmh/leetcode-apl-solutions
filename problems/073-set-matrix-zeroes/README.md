# 73. Set Matrix Zeroes

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Set zeros

## 💡 APL Solution

```apl
SetZeroes ← {⍵×⍨∘.∧⍨~0∊¨↓⍵}
```

## 📝 Explanation

Set row/col to 0

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(m*n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #73](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
