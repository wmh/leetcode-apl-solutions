# 739. Daily Temperatures

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find how many days until warmer temperature.

## 💡 APL Solution

```apl
DailyTemperatures ← {
    n←≢⍵
    result←n⍴0
    {result[⍵]←⊃⍸⍵<⍵↓⍵}¨⍳n
    result
}
```

## 📝 Explanation

APL solution for Daily Temperatures. Uses where (⍸) to find indices of true/non-zero elements. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #739](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
