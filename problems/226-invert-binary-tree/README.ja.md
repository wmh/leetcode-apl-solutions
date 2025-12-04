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

再帰的に左右の子を交換します。ベースケース：空のツリーは空を返します。再帰ケース：ルートを保持し、右の子に再帰してから左の子に再帰することで子を交換します。

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
