# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## 💡 APL Solution

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}

⍝ Example usage:
⍝ ContainsDuplicate 1 2 3 1    → 1 (true)
⍝ ContainsDuplicate 1 2 3 4    → 0 (false)
⍝ ContainsDuplicate 1 1 1 3 3 4 3 2 4 2    → 1 (true)
```

## 📝 Explanation

Compares the length of the array (≢⍵) with the length of unique elements (≢∪⍵). If they differ, there must be duplicates. The ≢ operator gives the length, ∪ gives unique elements, and ≠ checks if they're not equal.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
