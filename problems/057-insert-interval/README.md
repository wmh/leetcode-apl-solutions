# 57. Insert Interval

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Insert new interval and merge if necessary.

## 💡 APL Solution

```apl
Insert ← {
    newInterval←⍺
    result←merge newInterval,⍵
    result
}
```

## 📝 Explanation

APL solution for Insert Interval. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #57](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
