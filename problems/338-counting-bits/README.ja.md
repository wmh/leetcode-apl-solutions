# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

整数 n が与えられたとき、長さ n + 1 の配列 ans を返します。各 i (0 <= i <= n) について、ans[i] は i の 2 進数表現での 1 の数です。

## 💡 APL 解法

```apl
CountBits ← {+/¨2⊥⍣¯1¨⍳⍵+1}
```

## 📝 説明

0 から n までの各数値 (⍳⍵+1) について、基数 2 エンコードを使用して 2 進数に変換し (⊤⍨32⍴2)、ビットを合計します (+/)。¨ 演算子は各数値に操作を適用します。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n*log(n))`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
