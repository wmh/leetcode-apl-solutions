# 875. Koko Eating Bananas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

## 🟡 Difficulty: Medium

## Problem

Find minimum eating speed to finish all bananas in h hours.

## 💡 APL Solution

```apl
MinEatingSpeed ← {
    h←⍺
    speeds←1+⍳⌈/⍵
    ⊃speeds/⍨h≥+/⌈⍵÷⍤1⊢speeds
}
```

## 📝 Explanation

APL solution for Koko Eating Bananas. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses iota (⍳) to generate index ranges or find element positions. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(max))`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #875](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
