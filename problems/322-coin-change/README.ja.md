# 322. Coin Change

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

Min coins for amount

## 💡 APL 解法

```apl
CoinChange ← {⌊⍵÷⌊/⍺}
```

## 📝 説明

APL solution for Coin Change. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(amount*n)`
- **空間計算量**: `O(amount)`

---

## 📚 リソース

- [LeetCode Problem #322](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
