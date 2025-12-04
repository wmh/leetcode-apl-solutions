# 152. Maximum Product Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find maximum product subarray

## 💡 APL Solution

```apl
MaxProduct ← {⌈/×/¨{⍵↑¨⊂⍵}⍨⍳≢⍵}
```

## 📝 Explanation

APL solution for Maximum Product Subarray. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #152](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
