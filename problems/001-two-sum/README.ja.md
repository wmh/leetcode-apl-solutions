# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

整数配列 nums と整数 target が与えられたとき、合計が target になる 2 つの数値のインデックスを返します。各入力には正確に 1 つの解があると仮定でき、同じ要素を 2 回使用することはできません。任意の順序で答えを返すことができます。

## 💡 APL 解法

```apl
TwoSum ← {target←⍺ ⋄ arr←⍵ ⋄ sums←arr∘.+arr ⋄ mask←(sums=target)∧(∘.≠⍨⍳≢arr) ⋄ 2↑⍸mask}

⍝ Example usage:
⍝ 9 TwoSum 2 7 11 15    → 0 1
⍝ 6 TwoSum 3 2 4        → 1 2
⍝ 6 TwoSum 3 3          → 0 1
```

## 📝 説明

配列と自身の外積 (∘.+) を作成して、すべての可能な合計を取得します。マスクを使用して同じインデックスのペアを除外します (∘.≠⍨⍳≢arr)。⍸ で合計が目標と等しい位置を見つけます。2↑ で最初の 2 つのインデックスを取得します。

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
