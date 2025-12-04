# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

整数配列 nums が与えられたとき、配列内に少なくとも 2 回出現する値があれば true を返し、すべての要素が異なる場合は false を返します。

## 💡 APL 解法

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}
```

## 📝 説明

APL solution for Contains Duplicate. Uses unique (∪) to remove duplicate elements. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
