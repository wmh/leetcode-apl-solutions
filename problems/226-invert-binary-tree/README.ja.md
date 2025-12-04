# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

二分木のルート root が与えられたとき、ツリーを反転し、そのルートを返します。

## 💡 APL 解法

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⌽∇¨⍵}
```

## 📝 説明

APL solution for Invert Binary Tree. Uses reverse (⌽) to flip array elements. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(h)`

---

## 📚 リソース

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
