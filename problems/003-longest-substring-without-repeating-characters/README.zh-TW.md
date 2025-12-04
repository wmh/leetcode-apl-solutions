# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

給定一個字串 s，請你找出其中不含有重複字元的最長子串的長度。

## 💡 APL 解法

```apl
LengthOfLongestSubstring ← {⌈/≢¨∪¨{⍵↑¨⊂⍵}⍨⍳≢⍵}
```

## 📝 解釋

版本 2：生成所有子字串，檢查每個是否唯一 ((≢⍵)=≢∪⍵)，返回最大長度。使用嵌套的 drop/take 創建子字串。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n²)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
