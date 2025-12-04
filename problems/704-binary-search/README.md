# 704. Binary Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟢 Difficulty: Easy

## Problem

Search for target value in sorted array.

## 💡 APL Solution

```apl
BinarySearch ← {
    target←⍺
    (target∊⍵)×⊃⍸target=⍵
}
```

## 📝 Explanation

Standard binary search.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #704](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
