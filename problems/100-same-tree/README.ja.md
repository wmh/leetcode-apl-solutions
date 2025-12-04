# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

2 つの二分木のルート p と q が与えられたとき、それらが同じかどうかを確認する関数を作成します。2 つの二分木は、構造的に同一であり、ノードが同じ値を持つ場合、同じと見なされます。

## 💡 APL 解法

```apl
SameTree ← {⍺≡⍵}

⍝ For arrays representing trees:
⍝ Example usage:
⍝ (1 2 3) SameTree (1 2 3)    → 1
⍝ (1 2) SameTree (1 ⍬ 2)     → 0
⍝ (1 2 1) SameTree (1 1 2)   → 0
```

## 📝 説明

マッチ演算子 (≡) を使用します。配列が構造と値において同一である場合は 1 を返し、そうでない場合は 0 を返します。これは最も簡単な解決策です - たった 1 つの記号！

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
