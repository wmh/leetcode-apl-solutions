# 739. Daily Temperatures

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

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

For each day, finds next warmer day.

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
