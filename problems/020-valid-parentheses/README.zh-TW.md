# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給定一個只包括 '('，')'，'{'，'}'，'['，']' 的字串 s，判斷字串是否有效。有效字串需滿足：左括號必須用相同類型的右括號閉合。左括號必須以正確的順序閉合。每個右括號都有一個對應的相同類型的左括號。

## 💡 APL 解法

```apl
IsValid ← {0=+/(⍵='(')-⍵=')'}
```

## 📝 解釋

Valid Parentheses 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
