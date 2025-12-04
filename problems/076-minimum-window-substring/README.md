# 76. Minimum Window Substring

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🔴 Difficulty: Hard

## Problem

Find minimum window in s which contains all characters of t.

## 💡 APL Solution

```apl
MinWindow ← {
    ⍝ Sliding window with character count
    windows ← {⍵↑⍨⊃⍸(∧/⍺∊⍵)⍵}
    ⊃⌊/≢¨windows
}
```

## 📝 Explanation

Maintains character counts in sliding window.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*m)`
- **Space Complexity**: `O(m)`

---

## 📚 Resources

- [LeetCode Problem #76](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
