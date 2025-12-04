# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

## 💡 APL Solution

```apl
MissingNumber ← {(((≢⍵)×(≢⍵)+1)÷2)-+/⍵}

⍝ Example usage:
⍝ MissingNumber 3 0 1    → 2
⍝ MissingNumber 0 1      → 2
⍝ MissingNumber 9 6 4 2 3 5 7 0 1    → 8
```

## 📝 Explanation

Uses the formula for sum of 0 to n: n×(n+1)÷2. Calculates expected sum minus actual sum. The result is the missing number. (≢⍵) gives n, so we calculate n×(n+1)÷2 - (+/⍵) where +/⍵ is the sum of elements.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
