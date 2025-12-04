# 238. Product of Array Except Self

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目238] Return an array where each element is the product ...

## 💡 APL 解法

```apl
ProductExceptSelf ← {
    ⍝ Multiply all except current
    n ← ≢⍵
    result ← ×/¨⍵~¨⍵
    result
}
```

## 📝 解释

For each position, multiplies all other elements....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #238](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
