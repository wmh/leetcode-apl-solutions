# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Given an integer array nums, find the subarray with the largest sum, and return its sum.

## 💡 APL Solution

```apl
MaxSubArray ← {⌈/+\0⌈⍵-+\0,⍨⌊\+\⍵}

⍝ Simpler Kadane's algorithm:
MaxSubArray2 ← {⌈/{⌈/+\⍵}¨↓∘.,⍨⍳≢⍵}

⍝ Most readable:
MaxSubArray3 ← {⌈/⌈\0,+\⍵}

⍝ Example usage:
⍝ MaxSubArray3 ¯2 1 ¯3 4 ¯1 2 1 ¯5 4    → 6
⍝ MaxSubArray3 1                        → 1
⍝ MaxSubArray3 5 4 ¯1 7 8               → 23
```

## 📝 Explanation

Uses Kadane's algorithm. Version 3 is simplest: cumulative sum with running maximum (⌈\), prepending 0 to handle all-negative arrays. Takes max of running max sums.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
