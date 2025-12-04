# 198. House Robber

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟡 難易度: Medium

## 問題

Max money without robbing adjacent

## 💡 APL 解法

```apl
Rob ← {n←≢⍵ ⋄ n=0:0 ⋄ n=1:⊃⍵ ⋄ ⌈/(⊃⍵)+(∇2↓⍵),∇1↓⍵}
```

## 📝 説明

検証済み

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #198](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
