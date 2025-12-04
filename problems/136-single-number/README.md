# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with linear runtime complexity and use only constant extra space.

## 💡 APL Solution

```apl
SingleNumber ← {≠/⍵}

⍝ Example usage:
⍝ SingleNumber 4 1 2 1 2    → 4
⍝ SingleNumber 2 2 1        → 1
⍝ SingleNumber 1            → 1
```

## 📝 Explanation

Uses XOR reduce (≠/). XOR has the property that a⊕a=0 and a⊕0=a, so duplicate numbers cancel out, leaving only the single number. The ≠ operator is XOR in APL, and / is the reduce operator that applies XOR between all elements.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
