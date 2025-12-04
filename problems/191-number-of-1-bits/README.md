# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

## 💡 APL Solution

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 Explanation

Converts number to 32-bit binary using encode (⊤⍨32⍴2), then sums the bits with +/. The encode operator ⊤ converts to specified base.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
