# 94. Binary Tree Inorder Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given the root of a binary tree, return the inorder traversal of its nodes' values.

## 💡 APL Solution

```apl
Inorder ← {0=≢⍵:⍬ ⋄ (∇⍵[1]),⍵[0],∇⍵[2]}

⍝ Example: (1 ⍬ (2 (3 ⍬ ⍬) ⍬)) → 1 3 2
```

## 📝 Explanation

Recursive: traverse left, visit root, traverse right. Base case returns empty for null nodes.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)`

---

## 📚 Resources

- [LeetCode Problem #94](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
