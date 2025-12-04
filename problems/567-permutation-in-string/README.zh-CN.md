# 567. Permutation in String

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目567] Check if s2 contains a permutation of s1....

## 💡 APL 解法

```apl
CheckInclusion ← {
    (≢⍺)≤≢⍵:∨/{(∧/⍺∊⍵)∧∧/⍵∊⍺}¨(≢⍺)↑¨(≢⍵)↓¨⊂⍵
    0
}
```

## 📝 解释

Checks each substring of length |s1| for character match....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*m)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #567](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
