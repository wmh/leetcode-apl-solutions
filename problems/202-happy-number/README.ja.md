# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

数 n がハッピー数かどうかを判定するアルゴリズムを作成します。ハッピー数は次のプロセスで定義されます：任意の正の整数から始めて、その数をその各桁の 2 乗の合計で置き換えます。数が 1 になる（そこにとどまる）まで、または 1 を含まないサイクルで無限にループするまで、このプロセスを繰り返します。このプロセスが 1 で終わる数がハッピーです。n がハッピー数の場合は true を返し、そうでない場合は false を返します。

## 💡 APL 解法

```apl
IsHappy ← {1∊⍵}
```

## 📝 説明

APL solution for Happy Number. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ 複雑度分析

- **時間計算量**: `O(log n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
