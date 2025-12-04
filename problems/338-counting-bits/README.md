# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## 💡 APL Solution

```apl
CountBits ← {+/¨(⍳⍵+1)⊤⍨¨32⍴¨2}

⍝ Example usage:
⍝ CountBits 2    → 0 1 1
⍝ CountBits 5    → 0 1 1 2 1 2
```

## 📝 Explanation

For each number 0 to n (⍳⍵+1), converts to binary using base-2 encode (⊤⍨32⍴2), then sums the bits (+/). The ¨ operator applies operation to each number.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
