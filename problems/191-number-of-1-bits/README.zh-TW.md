# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

編寫一個函數，輸入是一個無符號整數（以二進位串的形式），返回其二進位表達式中設置位的個數（也被稱為漢明重量）。

## 💡 APL 解法

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 解釋

使用編碼 (⊤⍨32⍴2) 將數字轉換為 32 位元二進位，然後用 +/ 對位元求和。編碼運算子 ⊤ 轉換為指定的基數。

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
