# 153. Find Minimum in Rotated Sorted Array

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

[問題153] Find minimum element in rotated sorted array....

## 💡 APL 解法

```apl
FindMin ← {⌊/⍵}
```

## 📝 説明

APL solution for Find Minimum in Rotated Sorted Array. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(log n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #153](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
