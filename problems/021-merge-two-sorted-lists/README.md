# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## 💡 APL Solution

```apl
MergeTwoLists ← {⍺[⍋⍺,⍵],⍵[⍋⍺,⍵]}

⍝ Simpler version:
MergeTwoLists2 ← {(⍺,⍵)[⍋⍺,⍵]}

⍝ Example usage:
⍝ 1 2 4 MergeTwoLists2 1 3 4    → 1 1 2 3 4 4
⍝ ⍬ MergeTwoLists2 0            → 0
⍝ ⍬ MergeTwoLists2 ⍬            → ⍬
```

## 📝 Explanation

Concatenates both lists (⍺,⍵) then sorts by grade up (⍋). Grade up returns indices that would sort the array. Version 2 is cleaner: concatenate then index by sorted positions.

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
