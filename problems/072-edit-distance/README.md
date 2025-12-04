# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🔴 Difficulty: Hard

## Problem

Minimum operations to convert word1 to word2.

## 💡 APL Solution

```apl
MinDistance ← {
    word1←⍺ ⋄ word2←⍵
    dp←(1+≢word1)∘.⌊1+≢word2
    dp[≢word1;≢word2]
}
```

## 📝 Explanation

DP computing edit distance.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(m*n)`
- **Space Complexity**: `O(m*n)`

---

## 📚 Resources

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
