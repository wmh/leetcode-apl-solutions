# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

整数配列 nums が与えられたとき、配列内に少なくとも 2 回出現する値があれば true を返し、すべての要素が異なる場合は false を返します。

## 💡 APL 解法

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}

⍝ Example usage:
⍝ ContainsDuplicate 1 2 3 1    → 1 (true)
⍝ ContainsDuplicate 1 2 3 4    → 0 (false)
⍝ ContainsDuplicate 1 1 1 3 3 4 3 2 4 2    → 1 (true)
```

## 📝 説明

配列の長さ（≢⍵）と一意の要素の長さ（≢∪⍵）を比較します。それらが異なる場合、重複がある必要があります。≢ 演算子は長さを与え、∪ は一意の要素を与え、≠ はそれらが等しくないかどうかをチェックします。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
