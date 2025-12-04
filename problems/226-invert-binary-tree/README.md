# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given the root of a binary tree, invert the tree, and return its root.

## 💡 APL Solution

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⍵[0],(∇⍵[2]),∇⍵[1]}

⍝ For nested representation:
⍝ Example usage:
⍝ InvertTree (4 (2 (1 ⍬ ⍬) (3 ⍬ ⍬)) (7 (6 ⍬ ⍬) (9 ⍬ ⍬)))
⍝ → (4 (7 (9 ⍬ ⍬) (6 ⍬ ⍬)) (2 (3 ⍬ ⍬) (1 ⍬ ⍬)))
```

## 📝 Explanation

Recursively swaps left and right children. Base case: empty tree returns empty. Recursive case: keep root, swap children by recursing on right then left.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)`

---

## 📚 Resources

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
