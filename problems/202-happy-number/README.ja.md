# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

数 n がハッピー数かどうかを判定するアルゴリズムを作成します。ハッピー数は次のプロセスで定義されます：任意の正の整数から始めて、その数をその各桁の 2 乗の合計で置き換えます。数が 1 になる（そこにとどまる）まで、または 1 を含まないサイクルで無限にループするまで、このプロセスを繰り返します。このプロセスが 1 で終わる数がハッピーです。n がハッピー数の場合は true を返し、そうでない場合は false を返します。

## 💡 APL 解法

```apl
IsHappy ← {n←⍵ ⋄ seen←⍬ ⋄ {n∊seen:0 ⋄ 1=n:1 ⋄ seen,←n ⋄ n←+/((10⊥⍣¯1⊢n)*2) ⋄ ∇⍬}⍬}

⍝ Simpler iterative check:
IsHappy2 ← {1∊20{+/(10⊥⍣¯1⊢⍵)*2}⍣⍺⊢⍵}

⍝ Example usage:
⍝ IsHappy2 19    → 1
⍝ IsHappy2 2     → 0
```

## 📝 説明

バージョン 2：桁の 2 乗和を 20 回適用して反復します。結果に 1 が現れる場合、それはハッピーです。エンコード逆 (10⊥⍣¯1) を使用して桁を取得し、それらを 2 乗して合計します。

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
