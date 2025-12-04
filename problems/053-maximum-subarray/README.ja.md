# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

整数配列 nums が与えられたとき、最大の合計を持つ部分配列を見つけて、その合計を返します。

## 💡 APL 解法

```apl
MaxSubArray ← {⌈/+\0⌈⍵}
```

## 📝 説明

Kadane のアルゴリズムを使用します。バージョン 3 が最もシンプル：累積和と実行中の最大値 (⌈\)、すべて負の配列を処理するために 0 を前に追加します。実行中の最大和の最大値を取ります。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
