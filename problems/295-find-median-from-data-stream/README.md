# 295. Find Median from Data Stream

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🔴 Difficulty: Hard

## Problem

Find median from data stream.

## 💡 APL Solution

```apl
FindMedian ← {
    sorted←⍵[⍋⍵]
    n←≢sorted
    2|n:sorted[⌊n÷2]
    +⌿sorted[(n÷2)+¯1 0]÷2
}
```

## 📝 Explanation

Maintains sorted order and computes median.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #295](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
