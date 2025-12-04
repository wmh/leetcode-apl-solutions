# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

空でない整数配列 nums が与えられます。すべての要素は 2 回出現しますが、1 つだけ 1 回だけ出現します。その要素を見つけてください。線形時間計算量で、定数の追加スペースのみを使用するソリューションを実装する必要があります。

## 💡 APL 解法

```apl
SingleNumber ← {≠/⍵}

⍝ Example usage:
⍝ SingleNumber 4 1 2 1 2    → 4
⍝ SingleNumber 2 2 1        → 1
⍝ SingleNumber 1            → 1
```

## 📝 説明

XOR リダクション（≠/）を使用します。XOR には a⊕a=0 および a⊕0=a という性質があるため、重複する数値は相殺され、単一の数値のみが残ります。≠ 演算子は APL では XOR であり、/ はすべての要素間で XOR を適用するリダクション演算子です。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
