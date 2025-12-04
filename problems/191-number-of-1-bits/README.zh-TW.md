# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

編寫一個函數，輸入是一個無符號整數（以二進位串的形式），返回其二進位表達式中設置位的個數（也被稱為漢明重量）。

## 💡 APL 解法

```apl
HammingWeight ← {+/2⊥⍣¯1⊢⍵}
```

## 📝 解釋

Number of 1 Bits 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(1)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
