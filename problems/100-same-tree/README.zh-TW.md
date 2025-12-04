# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給你兩棵二元樹的根節點 p 和 q，編寫一個函數來檢驗這兩棵樹是否相同。如果兩個樹在結構上相同，並且節點具有相同的值，則認為它們是相同的。

## 💡 APL 解法

```apl
IsSameTree ← {⍺≡⍵}
```

## 📝 解釋

使用匹配運算子 (≡)，如果陣列在結構和值上相同則返回 1，否則返回 0。這是最簡單的解決方案 - 只需一個符號！

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
