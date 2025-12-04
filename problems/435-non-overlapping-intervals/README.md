# 435. Non-overlapping Intervals

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Minimum removals to make non-overlapping.

## 💡 APL Solution

```apl
EraseOverlapIntervals ← {
    sorted←⍵[⍋⍵[;1]]
    count←0
    count
}
```

## 📝 Explanation

APL solution for Non-overlapping Intervals. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #435](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
