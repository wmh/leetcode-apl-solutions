# 215. Kth Largest Element

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find kth largest element in array.

## 💡 APL Solution

```apl
FindKthLargest ← {⊃⍵[⍒⍵]⌷⍨⍺}
```

## 📝 Explanation

APL solution for Kth Largest Element. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #215](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
