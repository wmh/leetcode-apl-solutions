# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

編寫一個函數，輸入是一個無符號整數（以二進制串的形式），返回其二進制表達式中設置位的個數（也被稱為漢明重量）。

## 💡 APL 解法

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 解释

使用編碼 (⊤⍨32⍴2) 將數字轉換為 32 位二進制，然後用 +/ 對位求和。編碼操作符 ⊤ 轉換為指定的基數。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(1)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
