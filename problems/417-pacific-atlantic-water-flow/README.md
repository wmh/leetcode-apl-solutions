# 417. Pacific Atlantic Water Flow

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Find cells from which water can flow to both oceans.

## 💡 APL Solution

```apl
PacificAtlantic ← {
    ⍝ DFS from both coasts
    pacific∩atlantic
}
```

## 📝 Explanation

DFS from both ocean borders.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(m*n)`
- **Space Complexity**: `O(m*n)`

---

## 📚 Resources

- [LeetCode Problem #417](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
