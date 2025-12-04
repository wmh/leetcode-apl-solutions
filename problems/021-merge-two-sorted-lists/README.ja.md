# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

2 つのソート済みリンクリスト list1 と list2 の先頭が与えられます。2 つのリストを 1 つのソート済みリストにマージします。リストは、最初の 2 つのリストのノードをつなぎ合わせて作成する必要があります。マージされたリンクリストの先頭を返します。

## 💡 APL 解法

```apl
MergeTwoLists ← {⍺[⍋⍺,⍵],⍵[⍋⍺,⍵]}

⍝ Simpler version:
MergeTwoLists2 ← {(⍺,⍵)[⍋⍺,⍵]}

⍝ Example usage:
⍝ 1 2 4 MergeTwoLists2 1 3 4    → 1 1 2 3 4 4
⍝ ⍬ MergeTwoLists2 0            → 0
⍝ ⍬ MergeTwoLists2 ⍬            → ⍬
```

## 📝 説明

両方のリストを連結 (⍺,⍵) してから、昇順でソート (⍋)。昇順は配列をソートするインデックスを返します。バージョン 2 はよりクリーン：連結してからソートされた位置でインデックス。

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
