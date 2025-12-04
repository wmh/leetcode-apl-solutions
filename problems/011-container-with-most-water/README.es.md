# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

Se te da un array de enteros height de longitud n. Se dibujan n líneas verticales de tal manera que los dos extremos de la i-ésima línea son (i, 0) y (i, height[i]). Encuentra dos líneas que junto con el eje x formen un contenedor, de tal manera que el contenedor contenga la mayor cantidad de agua. Devuelve la cantidad máxima de agua que puede almacenar un contenedor.

## 💡 Solución APL

```apl
MaxArea ← {⌈/,((⊃⌊/¨⍵∘.,⍵)×(⊃-/¨(⍳≢⍵)∘.,⍳≢⍵))}

⍝ Simplified:
MaxArea2 ← {n←≢⍵ ⋄ ⌈/,((⍵∘.⌊⍵)×(⍳n)∘.-⍳n)}

⍝ Example usage:
⍝ MaxArea2 1 8 6 2 5 4 8 3 7    → 49
⍝ MaxArea2 1 1                  → 1
```

## 📝 Explicación

Crea el producto exterior de alturas (∘.⌊) para obtener alturas mínimas para todos los pares. Multiplica por distancias ((⍳n)∘.-⍳n) para obtener áreas. Toma el máximo.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n²)`
- **Complejidad Espacial**: `O(n²)`

---

## 📚 Recursos

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
