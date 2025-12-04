# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

二分木のルート root が与えられたとき、その最大深度を返します。二分木の最大深度は、ルート ノードから最も遠い葉ノードまでの最長パスに沿ったノード数です。

## 💡 APL 解法

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}

⍝ For nested arrays:
⍝ Example usage:
⍝ MaxDepth (3 (9 ⍬ ⍬) (20 (15 ⍬ ⍬) (7 ⍬ ⍬)))    → 3
⍝ MaxDepth (1 ⍬ (2 ⍬ ⍬))                          → 2
```

## 📝 説明

再帰的に深さをカウントします。ベースケース：空のツリーは深さ 0。再帰ケース：1 + 子の最大深さ。自己参照 (∇) を使用して各子を再帰し、⌈/ で最大値を取ります。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(h)`

---

## 📚 リソース

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
