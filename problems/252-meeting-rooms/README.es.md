# 252. Meeting Rooms

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

[Problema 252] Determine if person can attend all meetings....

## 💡 Solución APL

```apl
CanAttendMeetings ← {
    sorted←⍵[⍋⍵[;0]]
    ∧/sorted[1↓⍳≢sorted;0]≥sorted[¯1↓⍳≢sorted;1]
}
```

## 📝 Explicación

Checks for overlaps in sorted intervals....

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*log(n))`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #252](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
