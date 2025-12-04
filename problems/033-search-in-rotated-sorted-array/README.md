# 33. Search in Rotated Sorted Array

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Search for target in rotated sorted array.

## 💡 APL Solution

```apl
Search ← {
    pivot←⊃⍸⍵≠⌊/⍵
    target←⍺
    (target∊⍵)×⊃⍸target=⍵
}
```

## 📝 Explanation

Finds pivot point and searches in correct half.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #33](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
