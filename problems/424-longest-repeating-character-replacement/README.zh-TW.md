# 424. Longest Repeating Character Replacement

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 難度: Medium

## 題目

[題目424] Find length of longest substring with same letter ...

## 💡 APL 解法

```apl
CharacterReplacement ← {
    k←⍺ ⋄ maxLen←0
    {maxLen⌈←≢⍵}¨⊆⍵
    maxLen
}
```

## 📝 解釋

Slides window and counts character frequencies....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #424](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
