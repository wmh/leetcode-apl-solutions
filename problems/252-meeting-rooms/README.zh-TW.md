# 252. Meeting Rooms

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

[題目252] Determine if person can attend all meetings....

## 💡 APL 解法

```apl
CanAttendMeetings ← {
    sorted←⍵[⍋⍵[;0]]
    ∧/sorted[1↓⍳≢sorted;0]≥sorted[¯1↓⍳≢sorted;1]
}
```

## 📝 解釋

Meeting Rooms 的 APL 解決方案。使用等級 (⍋/⍒) 排序 - 返回將對陣列排序的索引。使用 tally (≢) 計算陣列長度。使用 iota (⍳) 生成索引範圍或查找元素位置。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(n))`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #252](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
