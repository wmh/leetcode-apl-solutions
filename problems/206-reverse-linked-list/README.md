# 206. Reverse Linked List

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given the head of a singly linked list, reverse the list, and return the reversed list.

## 💡 APL Solution

```apl
ReverseList ← {⌽⍵}

⍝ Example usage:
⍝ ReverseList 1 2 3 4 5    → 5 4 3 2 1
⍝ ReverseList 1 2          → 2 1
⍝ ReverseList 1            → 1
```

## 📝 Explanation

Uses the reverse operator (⌽). In APL, ⌽ reverses the elements of a vector along its last axis. This is the simplest possible solution - just one symbol!

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #206](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
