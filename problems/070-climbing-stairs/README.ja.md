# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

階段を登っています。頂上に到達するには n ステップかかります。毎回、1 段または 2 段登ることができます。頂上に登る方法は何通りありますか？

## 💡 APL 解法

```apl
ClimbStairs ← {⊃(+⌿⍣(⍵-1))1 1}
```

## 📝 説明

これはフィボナッチ数列です！冪演算子 (⍣⍵) を使用して n 回反復し、1 1 から始めます。各反復では最後の 2 つの数値の合計を追加します ({⍵,+/¯2↑⍵})。最終結果の最初の要素を取ります (⊃)。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
