# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Se te da un entero grande representado como un array de enteros digits, donde cada digits[i] es el i-ésimo dígito del entero. Los dígitos están ordenados de más significativo a menos significativo en orden de izquierda a derecha. El entero grande no contiene ningún 0 inicial. Incrementa el entero grande en uno y devuelve el array resultante de dígitos.

## 💡 Solución APL

```apl
PlusOne ← {10⊥1+10⊥⍣¯1⊢⍵}
```

## 📝 Explicación

Convierte dígitos a número usando decodificación (10⊥⍵), suma 1, luego convierte de vuelta a dígitos usando codificación (10⊥⍣¯1). El operador ⊥ decodifica desde base 10, ⊥⍣¯1 codifica a dígitos de base 10.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
