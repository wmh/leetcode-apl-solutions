# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

範囲 [0, n] の n 個の異なる数値を含む配列 nums が与えられたとき、配列から欠落している範囲内の唯一の数値を返します。

## 💡 APL 解法

```apl
MissingNumber ← {(((≢⍵)×(≢⍵)+1)÷2)-+/⍵}

⍝ Example usage:
⍝ MissingNumber 3 0 1    → 2
⍝ MissingNumber 0 1      → 2
⍝ MissingNumber 9 6 4 2 3 5 7 0 1    → 8
```

## 📝 説明

0 から n までの和の公式を使用します：n×(n+1)÷2。期待される合計から実際の合計を引きます。結果が欠落している数値です。(≢⍵) は n を与えるので、n×(n+1)÷2 - (+/⍵) を計算します。ここで +/⍵ は要素の合計です。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
