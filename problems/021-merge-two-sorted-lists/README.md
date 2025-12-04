# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟢 Difficulty: Easy

## Problem

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## 💡 APL Solution

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 Explanation

APL solution for Merge Two Sorted Lists. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O((n+m)*log(n+m))`
- **Space Complexity**: `O(n+m)`

---

## 📚 Resources

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
