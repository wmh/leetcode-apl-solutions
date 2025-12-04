# 235. Lowest Common Ancestor of BST

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find LCA in BST.

## 💡 APL Solution

```apl
LowestCommonAncestor ← {
    ⍝ Find split point
    ⊃⍸(⍺≤⍵)∧(⍵≤⍺)
}
```

## 📝 Explanation

APL solution for Lowest Common Ancestor of BST. Uses where (⍸) to find indices of true/non-zero elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #235](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
