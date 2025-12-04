# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

整数配列 nums と整数 target が与えられたとき、合計が target になる 2 つの数値のインデックスを返します。各入力には正確に 1 つの解があると仮定でき、同じ要素を 2 回使用することはできません。任意の順序で答えを返すことができます。

## 💡 APL 解法

```apl
TwoSum ← {(⊃⍸⍺=+/∘.,⍨⍵)}
```

## 📝 説明

APL solution for Two Sum. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses where (⍸) to find indices of true/non-zero elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(n²)`
- **空間計算量**: `O(n²)`

---

## 📚 リソース

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
