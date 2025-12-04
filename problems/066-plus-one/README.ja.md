# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

整数の配列 digits として表される大きな整数が与えられます。各 digits[i] は整数の i 番目の桁です。桁は最上位から最下位まで左から右の順に並べられています。大きな整数には先頭の 0 は含まれません。大きな整数を 1 増やして、結果の桁の配列を返します。

## 💡 APL 解法

```apl
PlusOne ← {10⊥⍣¯1⊢1+10⊥⍵}

⍝ Example usage:
⍝ PlusOne 1 2 3    → 1 2 4
⍝ PlusOne 4 3 2 1  → 4 3 2 2
⍝ PlusOne 9        → 1 0
```

## 📝 説明

デコード（10⊥⍵）を使用して桁を数値に変換し、1 を加算してから、エンコード（10⊥⍣¯1）を使用して桁に戻します。⊥ 演算子は基数 10 からデコードし、⊥⍣¯1 は基数 10 の桁にエンコードします。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
