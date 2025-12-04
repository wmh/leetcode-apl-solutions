# 215. Kth Largest Element

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Find kth largest element in array.

## 💡 APL Solution

```apl
FindKthLargest ← {
    k←⍺
    sorted←⍵[⍒⍵]
    sorted[k-1]
}
```

## 📝 Explanation

Sorts in descending order and returns kth.

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
