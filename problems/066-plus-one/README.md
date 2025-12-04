# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

## 💡 APL Solution

```apl
PlusOne ← {10⊥⍣¯1⊢1+10⊥⍵}

⍝ Example usage:
⍝ PlusOne 1 2 3    → 1 2 4
⍝ PlusOne 4 3 2 1  → 4 3 2 2
⍝ PlusOne 9        → 1 0
```

## 📝 Explanation

Converts digits to number using decode (10⊥⍵), adds 1, then converts back to digits using encode (10⊥⍣¯1). The ⊥ operator decodes from base 10, ⊥⍣¯1 encodes to base 10 digits.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
