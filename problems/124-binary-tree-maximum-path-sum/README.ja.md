# 124. Binary Tree Maximum Path Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🔴 難易度: Hard

## 問題

[問題124] Find maximum path sum....

## 💡 APL 解法

```apl
MaxPathSum ← {+/⍵}
```

## 📝 説明

APL solution for Binary Tree Maximum Path Sum. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #124](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
