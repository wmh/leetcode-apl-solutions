# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 💡 APL Solution

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}

⍝ For nested arrays:
⍝ Example usage:
⍝ MaxDepth (3 (9 ⍬ ⍬) (20 (15 ⍬ ⍬) (7 ⍬ ⍬)))    → 3
⍝ MaxDepth (1 ⍬ (2 ⍬ ⍬))                          → 2
```

## 📝 Explanation

Recursively counts depth. Base case: empty tree has depth 0. Recursive case: 1 + maximum depth of children. Uses self-reference (∇) to recurse over each child, then takes maximum with ⌈/.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)`

---

## 📚 Resources

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
