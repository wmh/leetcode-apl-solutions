# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

正の整数の 2 進数表現を受け取り、セットされているビット数（ハミング重みとも呼ばれます）を返す関数を作成します。

## 💡 APL 解法

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 説明

エンコード (⊤⍨32⍴2) を使用して数値を 32 ビットバイナリに変換し、+/ でビットを合計します。エンコード演算子 ⊤ は指定された基数に変換します。

## ⏱️ 複雑度分析

- **時間計算量**: `O(1)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
