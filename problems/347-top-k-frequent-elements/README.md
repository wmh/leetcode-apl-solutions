# 347. Top K Frequent Elements

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Return the k most frequent elements.

## 💡 APL Solution

```apl
TopKFrequent ← {
    k ← ⍺
    freq ← {⍵,≢⍵}⌸⍵
    k↑freq[⍒freq[;2];1]
}
```

## 📝 Explanation

Groups elements by frequency and takes top k.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n*log(n))`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #347](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
