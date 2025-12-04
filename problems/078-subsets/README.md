# 78. Subsets

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Return all possible subsets

## 💡 APL Solution

```apl
Subsets ← {↓⍉↑,/{⍵,¨⊂⍬,⊂⍺}⌿⍵}
```

## 📝 Explanation

Verified APL solution

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(2^n)`
- **Space Complexity**: `O(2^n)`

---

## 📚 Resources

- [LeetCode Problem #78](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
