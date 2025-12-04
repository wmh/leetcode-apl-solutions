# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Se te da un array prices donde prices[i] es el precio de una acción dada en el i-ésimo día. Quieres maximizar tu beneficio eligiendo un solo día para comprar una acción y eligiendo un día diferente en el futuro para vender esa acción. Devuelve el beneficio máximo que puedes lograr de esta transacción. Si no puedes lograr ningún beneficio, devuelve 0.

## 💡 Solución APL

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}
```

## 📝 Explicación

Rastrea el mínimo en ejecución con escaneo (⌊\⍵). Resta el mínimo de cada precio (⍵-⌊\⍵) para obtener el beneficio en cada punto. Toma el máximo con ⌈/ y compara con 0 para manejar el caso sin beneficio.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
