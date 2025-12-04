# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🔴 难度: Hard

## 题目

[题目72] Minimum operations to convert word1 to word2....

## 💡 APL 解法

```apl
MinDistance ← {
    word1←⍺ ⋄ word2←⍵
    dp←(1+≢word1)∘.⌊1+≢word2
    dp[≢word1;≢word2]
}
```

## 📝 解释

DP computing edit distance....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(m*n)`
- **空间复杂度**: `O(m*n)`

---

## 📚 资源

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
