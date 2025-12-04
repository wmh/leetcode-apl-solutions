# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

長さ n の整数配列 height が与えられます。i 番目の線の 2 つの端点が (i, 0) と (i, height[i]) になるように n 本の垂直線が描かれています。x 軸と一緒にコンテナを形成する 2 本の線を見つけて、コンテナが最も多くの水を含むようにします。コンテナが格納できる最大水量を返します。

## 💡 APL 解法

```apl
MaxArea ← {⌈/,((⍵∘.⌊⍵)×(⍳≢⍵)∘.-⍳≢⍵)}
```

## 📝 説明

高さの外積 (∘.⌊) を作成して、すべてのペアの最小高さを取得します。距離 ((⍳n)∘.-⍳n) を掛けて面積を取得します。最大値を取ります。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n²)`
- **空間計算量**: `O(n²)`

---

## 📚 リソース

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
