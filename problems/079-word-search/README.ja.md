# 79. Word Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟡 難易度: Medium

## 問題

Find word in board

## 💡 APL 解法

```apl
Exist ← {∨/⍺∘⍷¨⍵}
```

## 📝 説明

検証済みの APL ソリューション

## ⏱️ 複雑度分析

- **時間計算量**: `O(m*n*4^k)`
- **空間計算量**: `O(k)`

---

## 📚 リソース

- [LeetCode Problem #79](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
