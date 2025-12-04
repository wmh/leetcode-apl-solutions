# 853. Car Fleet

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

[Problema 853] Count number of car fleets that will arrive at des...

## 💡 Solución APL

```apl
CarFleet ← {
    sorted←⍵[⍒⍵[;1]]
    times←(⍺-sorted[;1])÷sorted[;2]
    1+≢⍸times>⌈\times
}
```

## 📝 Explicación

Sorts by position and calculates arrival times....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*log(n))`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #853](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
