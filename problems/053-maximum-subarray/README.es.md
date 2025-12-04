# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

Dado un array de enteros nums, encuentra el subarray con la suma más grande y devuelve su suma.

## 💡 Solución APL

```apl
MaxSubArray ← {⌈/+\0⌈⍵}
```

## 📝 Explicación

Utiliza el algoritmo de Kadane. La versión 3 es la más simple: suma acumulativa con máximo en ejecución (⌈\), anteponiendo 0 para manejar arrays todos negativos. Toma el máximo de las sumas máximas en ejecución.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
