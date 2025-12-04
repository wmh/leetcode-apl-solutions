# 78. Subsets

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

Return all possible subsets

## 💡 APL 解法

```apl
Subsets ← {↓⍉(≢⍵)⊤⍳2*≢⍵}
```

## 📝 説明

APL solution for Subsets. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses transpose (⍉) to swap matrix rows and columns. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(2^n)`
- **空間計算量**: `O(2^n)`

---

## 📚 リソース

- [LeetCode Problem #78](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
