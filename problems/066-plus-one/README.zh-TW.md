# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

給你一個由整數組成的非空陣列，表示一個非負整數，請你把這個整數加一。最高位數字存放在陣列的首位，陣列中每個元素只存儲單個數字。你可以假設除了整數 0 之外，這個整數不會以零開頭。

## 💡 APL 解法

```apl
PlusOne ← {10⊥⍣¯1⊢1+10⊥⍵}

⍝ Example usage:
⍝ PlusOne 1 2 3    → 1 2 4
⍝ PlusOne 4 3 2 1  → 4 3 2 2
⍝ PlusOne 9        → 1 0
```

## 📝 解釋

使用解碼（10⊥⍵）將數字轉換為數字，加 1，然後使用編碼（10⊥⍣¯1）轉換回數字。⊥ 運算子從基數 10 解碼，⊥⍣¯1 編碼為基數 10 數字。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
