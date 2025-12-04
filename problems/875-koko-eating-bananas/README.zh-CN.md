# 875. Koko Eating Bananas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 难度: Medium

## 题目

[题目875] Find minimum eating speed to finish all bananas in...

## 💡 APL 解法

```apl
MinEatingSpeed ← {
    h←⍺
    speeds←1+⍳⌈/⍵
    ⊃speeds/⍨h≥+/⌈⍵÷⍤1⊢speeds
}
```

## 📝 解释

Binary search on eating speed....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(max))`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #875](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
