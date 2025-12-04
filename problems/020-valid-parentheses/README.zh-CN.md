# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給定一個只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判斷字符串是否有效。有效字符串需滿足：左括號必須用相同類型的右括號閉合。左括號必須以正確的順序閉合。每個右括號都有一個對應的相同類型的左括號。

## 💡 APL 解法

```apl
ValidParentheses ← {
    ⍝ Simple balance check for single type
    0=+/('('=⍵)-')'=⍵
}

⍝ For full validation with multiple types:
ValidParentheses2 ← {
    pairs←'()' '[]' '{}'
    stack←⍬
    valid←1
    {valid∧←ProcessChar ⍵}¨⍵
    valid∧0=≢stack
}

⍝ Example usage:
⍝ ValidParentheses '()'        → 1
⍝ ValidParentheses '()[]{}'    → 1
⍝ ValidParentheses '(]'        → 0
```

## 📝 解释

對於簡單情況（版本 1）：計算開括號 '(' 並減去閉括號 ')'。如果和為 0 則有效。對於完整驗證（版本 2）：需要基於堆棧的括號對匹配。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
