# 15. 3Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find all unique triplets that sum to zero

## 💡 APL Solution

```apl
ThreeSum ← {∪↓(⊂⍵)[⍸0=+⌿⍵∘.+⍵∘.+⍵]}
```

## 📝 Explanation

APL solution for 3Sum. Uses outer product (∘.) to create matrix of all pair combinations. Uses where (⍸) to find indices of true/non-zero elements. Uses unique (∪) to remove duplicate elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #15](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
