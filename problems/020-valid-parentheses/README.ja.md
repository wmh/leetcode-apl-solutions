# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

'('、')'、'{'、'}'、'['、']' の文字だけを含む文字列 s が与えられたとき、入力文字列が有効かどうかを判定します。入力文字列が有効であるのは：開き括弧は同じタイプの閉じ括弧で閉じられなければなりません。開き括弧は正しい順序で閉じられなければなりません。すべての閉じ括弧には、対応する同じタイプの開き括弧があります。

## 💡 APL 解法

```apl
IsValid ← {0=+/(⍵='(')-⍵=')'}
```

## 📝 説明

単純なケース（バージョン 1）：開き括弧 '(' をカウントし、閉じ括弧 ')' を減算します。合計が 0 であれば有効です。完全な検証（バージョン 2）：括弧ペアのスタックベースのマッチングが必要です。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
