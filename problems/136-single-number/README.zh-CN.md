# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個非空整數數組 nums，除了某個元素只出現一次以外，其餘每個元素均出現兩次。找出那個只出現了一次的元素。你必須實現線性時間複雜度的算法，並且只使用常數額外空間。

## 💡 APL 解法

```apl
SingleNumber ← {⊃⍸1=+⌿∘.=⍨⍵}
```

## 📝 解释

Single Number 的 APL 解决方案。使用 where (⍸) 查找真值/非零元素的索引。使用封闭 (⊂) 包装元素或展开 (⊃) 解包/提取。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
