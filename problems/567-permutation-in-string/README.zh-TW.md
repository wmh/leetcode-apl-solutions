# 567. Permutation in String

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 難度: Medium

## 題目

[題目567] Check if s2 contains a permutation of s1....

## 💡 APL 解法

```apl
CheckInclusion ← {
    (≢⍺)≤≢⍵:∨/{(∧/⍺∊⍵)∧∧/⍵∊⍺}¨(≢⍺)↑¨(≢⍵)↓¨⊂⍵
    0
}
```

## 📝 解釋

Checks each substring of length |s1| for character match....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*m)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #567](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
