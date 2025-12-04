# 416. Partition Equal Subset Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Determine if array can be partitioned into two subsets with equal sum.

## 💡 APL Solution

```apl
CanPartition ← {
    target←(+/⍵)÷2
    2|+/⍵:0
    target∊+/¨subsets
}
```

## 📝 Explanation

Checks if subset sum equals half of total.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*sum)`
- **Space Complexity**: `O(sum)`

---

## 📚 Resources

- [LeetCode Problem #416](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
