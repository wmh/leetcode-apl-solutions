# 155. Min Stack

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Design a stack with push, pop, top, and getMin in O(1).

## 💡 APL Solution

```apl
MinStack ← {
    stack ← ⍬
    minStack ← ⍬
    {stack,←⍵ ⋄ minStack,←⌊/stack}¨⍵
}
```

## 📝 Explanation

Maintains auxiliary stack for minimums.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #155](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
