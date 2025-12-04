# 371. Sum of Two Integers

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目371] Add two integers without + or -....

## 💡 APL 解法

```apl
GetSum ← {
    ⍝ XOR for sum, AND for carry
    (⍺≠⍵)+2×⍺∧⍵
}
```

## 📝 解釋

Sum of Two Integers 的 APL 解決方案。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(1)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #371](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
