# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

Du erhältst ein Integer-Array height der Länge n. Es werden n vertikale Linien gezeichnet, sodass die zwei Endpunkte der i-ten Linie (i, 0) und (i, height[i]) sind. Finde zwei Linien, die zusammen mit der x-Achse einen Container bilden, sodass der Container das meiste Wasser enthält. Gib die maximale Wassermenge zurück, die ein Container speichern kann.

## 💡 APL-Lösung

```apl
MaxArea ← {⌈/,((⊃⌊/¨⍵∘.,⍵)×(⊃-/¨(⍳≢⍵)∘.,⍳≢⍵))}

⍝ Simplified:
MaxArea2 ← {n←≢⍵ ⋄ ⌈/,((⍵∘.⌊⍵)×(⍳n)∘.-⍳n)}

⍝ Example usage:
⍝ MaxArea2 1 8 6 2 5 4 8 3 7    → 49
⍝ MaxArea2 1 1                  → 1
```

## 📝 Erklärung

Erstellt äußeres Produkt von Höhen (∘.⌊), um minimale Höhen für alle Paare zu erhalten. Multipliziert mit Entfernungen ((⍳n)∘.-⍳n), um Flächen zu erhalten. Nimmt Maximum.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n²)`
- **Raumkomplexität**: `O(n²)`

---

## 📚 Ressourcen

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
