# 347. Top K Frequent Elements

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 难度: Medium

## 题目

[题目347] Return the k most frequent elements....

## 💡 APL 解法

```apl
TopKFrequent ← {
    k ← ⍺
    freq ← {⍵,≢⍵}⌸⍵
    k↑freq[⍒freq[;2];1]
}
```

## 📝 解释

Groups elements by frequency and takes top k....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(n))`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #347](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
