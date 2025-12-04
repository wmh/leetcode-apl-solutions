# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## 💡 APL Solution

```apl
SameTree ← {⍺≡⍵}

⍝ For arrays representing trees:
⍝ Example usage:
⍝ (1 2 3) SameTree (1 2 3)    → 1
⍝ (1 2) SameTree (1 ⍬ 2)     → 0
⍝ (1 2 1) SameTree (1 1 2)   → 0
```

## 📝 Explanation

Uses match operator (≡) which returns 1 if arrays are identical in structure and values, 0 otherwise. This is the simplest possible solution - just one symbol!

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
