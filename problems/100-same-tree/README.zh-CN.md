# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給你兩棵二叉樹的根節點 p 和 q，編寫一個函數來檢驗這兩棵樹是否相同。如果兩個樹在結構上相同，並且節點具有相同的值，則認為它們是相同的。

## 💡 APL 解法

```apl
SameTree ← {⍺≡⍵}

⍝ For arrays representing trees:
⍝ Example usage:
⍝ (1 2 3) SameTree (1 2 3)    → 1
⍝ (1 2) SameTree (1 ⍬ 2)     → 0
⍝ (1 2 1) SameTree (1 1 2)   → 0
```

## 📝 解释

使用匹配運算符 (≡)，如果數組在結構和值上相同則返回 1，否則返回 0。這是最簡單的解決方案 - 只需一個符號！

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
