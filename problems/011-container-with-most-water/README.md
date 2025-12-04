# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

## 💡 APL Solution

```apl
MaxArea ← {⌈/,((⊃⌊/¨⍵∘.,⍵)×(⊃-/¨(⍳≢⍵)∘.,⍳≢⍵))}

⍝ Simplified:
MaxArea2 ← {n←≢⍵ ⋄ ⌈/,((⍵∘.⌊⍵)×(⍳n)∘.-⍳n)}

⍝ Example usage:
⍝ MaxArea2 1 8 6 2 5 4 8 3 7    → 49
⍝ MaxArea2 1 1                  → 1
```

## 📝 Explanation

Creates outer product of heights (∘.⌊) to get minimum heights for all pairs. Multiplies by distances ((⍳n)∘.-⍳n) to get areas. Takes maximum.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n²)`

---

## 📚 Resources

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
