# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給定一個非空整數數組 nums，除了某個元素只出現一次以外，其餘每個元素均出現兩次。找出那個只出現了一次的元素。你必須實現線性時間複雜度的算法，並且只使用常數額外空間。

## 💡 APL 解法

```apl
SingleNumber ← {≠/⍵}

⍝ Example usage:
⍝ SingleNumber 4 1 2 1 2    → 4
⍝ SingleNumber 2 2 1        → 1
⍝ SingleNumber 1            → 1
```

## 📝 解释

使用 XOR 歸約（≠/）。XOR 具有 a⊕a=0 和 a⊕0=a 的性質，因此重複的數字會相互抵消，只剩下單獨的數字。≠ 操作符在 APL 中是 XOR，/ 是將 XOR 應用於所有元素的歸約操作符。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
