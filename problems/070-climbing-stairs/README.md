# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 💡 APL Solution

```apl
ClimbStairs ← {⊃{⍵,+/¯2↑⍵}⍣⍵⊢1 1}

⍝ Alternative using matrix power:
ClimbStairs2 ← {⊃⊃(2 2⍴1 1 1 0)+.×⍣⍵⊢2 2⍴1 0 0 1}

⍝ Example usage:
⍝ ClimbStairs 2    → 2
⍝ ClimbStairs 3    → 3
⍝ ClimbStairs 5    → 8
```

## 📝 Explanation

This is Fibonacci sequence! Iterates n times with power operator (⍣⍵), starting with 1 1. Each iteration appends sum of last 2 numbers ({⍵,+/¯2↑⍵}). Takes first element (⊃) of final result.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
