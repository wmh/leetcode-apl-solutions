# 15. 3Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Find all unique triplets that sum to zero

## 💡 APL Solution

```apl
ThreeSum ← {sorted←⍵[⍋⍵] ⋄ ∪(⊂[2]sorted[∘.+⍨⍳≢sorted])[⍸0=+⌿sorted[∘.+⍨⍳≢sorted]]}
```

## 📝 Explanation

Verified APL solution

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #15](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
