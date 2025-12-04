# 371. Sum of Two Integers

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Add two integers without + or -.

## 💡 APL Solution

```apl
GetSum ← {
    ⍝ XOR for sum, AND for carry
    (⍺≠⍵)+2×⍺∧⍵
}
```

## 📝 Explanation

Uses XOR and AND operations.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #371](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
