# 853. Car Fleet

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Count number of car fleets that will arrive at destination.

## 💡 APL Solution

```apl
CarFleet ← {
    sorted←⍵[⍒⍵[;1]]
    times←(⍺-sorted[;1])÷sorted[;2]
    1+≢⍸times>⌈\times
}
```

## 📝 Explanation

APL solution for Car Fleet. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Uses scan (\) to compute running operations: +\ is running sum, ×\ is running product, ⌈\ is running max, ⌊\ is running min. Uses where (⍸) to find indices of true/non-zero elements. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #853](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
