# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.

## 💡 APL Solution

```apl
IsHappy ← {n←⍵ ⋄ seen←⍬ ⋄ {n∊seen:0 ⋄ 1=n:1 ⋄ seen,←n ⋄ n←+/((10⊥⍣¯1⊢n)*2) ⋄ ∇⍬}⍬}

⍝ Simpler iterative check:
IsHappy2 ← {1∊20{+/(10⊥⍣¯1⊢⍵)*2}⍣⍺⊢⍵}

⍝ Example usage:
⍝ IsHappy2 19    → 1
⍝ IsHappy2 2     → 0
```

## 📝 Explanation

Version 2: Iterates 20 times applying digit square sum. If 1 appears in results, it's happy. Uses encode inverse (10⊥⍣¯1) to get digits, squares them, and sums.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
