# 155. Min Stack

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目155] Design a stack with push, pop, top, and getMin in ...

## 💡 APL 解法

```apl
MinStack ← {
    stack ← ⍬
    minStack ← ⍬
    {stack,←⍵ ⋄ minStack,←⌊/stack}¨⍵
}
```

## 📝 解釋

Maintains auxiliary stack for minimums....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(1)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #155](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
