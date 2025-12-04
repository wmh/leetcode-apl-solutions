# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

2 つのソート済みリンクリスト list1 と list2 の先頭が与えられます。2 つのリストを 1 つのソート済みリストにマージします。リストは、最初の 2 つのリストのノードをつなぎ合わせて作成する必要があります。マージされたリンクリストの先頭を返します。

## 💡 APL 解法

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 説明

APL solution for Merge Two Sorted Lists. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O((n+m)*log(n+m))`
- **空間計算量**: `O(n+m)`

---

## 📚 リソース

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
