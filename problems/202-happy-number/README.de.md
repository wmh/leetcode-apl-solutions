# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Schreibe einen Algorithmus, um zu bestimmen, ob eine Zahl n glücklich ist. Eine glückliche Zahl ist eine Zahl, die durch folgenden Prozess definiert ist: Beginnend mit einer beliebigen positiven Ganzzahl, ersetze die Zahl durch die Summe der Quadrate ihrer Ziffern. Wiederhole den Prozess, bis die Zahl 1 ist (wo sie bleiben wird), oder sie endlos in einem Zyklus schleift, der nicht 1 enthält. Zahlen, für die dieser Prozess bei 1 endet, sind glücklich. Gib true zurück, wenn n eine glückliche Zahl ist, und false, wenn nicht.

## 💡 APL-Lösung

```apl
IsHappy ← {n←⍵ ⋄ seen←⍬ ⋄ {n∊seen:0 ⋄ 1=n:1 ⋄ seen,←n ⋄ n←+/((10⊥⍣¯1⊢n)*2) ⋄ ∇⍬}⍬}

⍝ Simpler iterative check:
IsHappy2 ← {1∊20{+/(10⊥⍣¯1⊢⍵)*2}⍣⍺⊢⍵}

⍝ Example usage:
⍝ IsHappy2 19    → 1
⍝ IsHappy2 2     → 0
```

## 📝 Erklärung

Version 2: Iteriert 20 Mal und wendet die Zifferquadratsumme an. Wenn 1 in den Ergebnissen erscheint, ist es glücklich. Verwendet inverse Kodierung (10⊥⍣¯1), um Ziffern zu erhalten, quadriert sie und summiert.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(log n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
