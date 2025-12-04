# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be visited again by continuously following the next pointer. Return true if there is a cycle in the linked list. Otherwise, return false.

## 💡 APL Solution

```apl
HasCycle ← {(≢⍵)≠≢∪⍵}

⍝ For array representation: check for duplicates
⍝ Example usage:
⍝ HasCycle 3 2 0 ¯4    → 0 (no cycle)
⍝ HasCycle 1 2 1       → 1 (has cycle - 1 repeats)
```

## 📝 Explanation

For array representation: checks if length differs from unique length. If there are duplicates (cycle), lengths differ. Uses unique (∪) and tally (≢).

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
