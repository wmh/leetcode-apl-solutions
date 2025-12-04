# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

給你一個整數 n，對於 0 <= i <= n 中的每個 i，計算其二進位表示中 1 的個數，返回一個長度為 n+1 的陣列 ans 作為答案。

## 💡 APL 解法

```apl
CountBits ← {+/¨(⍳⍵+1)⊤⍨¨32⍴¨2}

⍝ Example usage:
⍝ CountBits 2    → 0 1 1
⍝ CountBits 5    → 0 1 1 2 1 2
```

## 📝 解釋

對於 0 到 n 的每個數字 (⍳⍵+1)，使用基數 2 編碼轉換為二進位 (⊤⍨32⍴2)，然後對位求和 (+/)。¨ 運算子將操作應用於每個數字。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(n))`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
