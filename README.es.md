# 🧠 Soluciones LeetCode en APL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> Resolviendo más de 100 problemas clásicos de LeetCode usando APL (A Programming Language) - uno de los lenguajes de programación más esotéricos y poderosos.

> **⚠️ Contenido Generado por IA**: Este proyecto fue creado con asistencia significativa de IA. Ver [AI_GENERATED.md](./AI_GENERATED.md) para detalles. El código APL no ha sido probado en un intérprete real. Se recomienda verificación antes de usar.

**🌍 Idiomas**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🎯 Sobre Este Proyecto

Este proyecto muestra soluciones a los problemas más populares de LeetCode implementados en **APL (A Programming Language)**, un lenguaje único conocido por:

- **Extrema Concisión**: Expresa algoritmos complejos en muy pocos caracteres
- **Orientado a Arrays**: Soporte nativo para operaciones poderosas de arrays
- **Notación Matemática**: Usa símbolos Unicode especiales (⍵, ⍺, ⌽, ⊥, ∇, etc.)
- **Alta Curva de Aprendizaje**: Considerado uno de los lenguajes más difíciles de dominar

### ¿Por qué APL?

APL desafía los paradigmas de programación convencionales y ofrece:
- Una forma completamente diferente de pensar sobre algoritmos
- Soluciones elegantes que a menudo revelan la esencia matemática de los problemas
- Un rico conjunto de operaciones primitivas para manipulación de arrays
- Significado histórico como uno de los primeros lenguajes de alto nivel

## 📊 Cobertura de Problemas

| Dificultad | Cantidad | Porcentaje |
|------------|----------|------------|
| 🟢 Fácil   | 40+      | ~35%       |
| 🟡 Medio   | 50+      | ~50%       |
| 🔴 Difícil | 15+      | ~15%       |
| **Total**  | **100+** | **100%**   |

## 📝 Lista de Problemas

### Problemas Destacados

#### #1 - Two Sum (Fácil)
**Problema**: Dado un array de enteros y un objetivo, devuelve los índices de dos números que suman el objetivo.

**Solución APL**:
```apl
TwoSum ← {
    ⍝ ⍺: suma objetivo, ⍵: array
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}
```

**Explicación**: Usa producto exterior `∘.` para generar todas las sumas de pares posibles, luego `⍸` para encontrar índices coincidentes.

**Complejidad**: Tiempo O(n²), Espacio O(n²)

[📄 Solución Completa](problems/001-two-sum.json)

---

#### #136 - Single Number (Fácil)
**Problema**: Encuentra el elemento que aparece solo una vez en un array donde todos los demás aparecen dos veces.

**Solución APL**:
```apl
SingleNumber ← {≠/⍵}
```

**Explicación**: Reducción XOR - ¡el one-liner más elegante! Aprovecha las propiedades XOR: a⊕a=0 y a⊕0=a.

**Complejidad**: Tiempo O(n), Espacio O(1)

[📄 Solución Completa](problems/136-single-number.json)

---

#### #206 - Reverse Linked List (Fácil)
**Problema**: Invierte una lista enlazada simple.

**Solución APL**:
```apl
ReverseList ← {⌽⍵}
```

**Explicación**: `⌽` es el operador de inversión de APL - ¡la solución más simple posible!

**Complejidad**: Tiempo O(n), Espacio O(1)

[📄 Solución Completa](problems/206-reverse-list.json)

---

### 📚 Todos los Problemas

Explora todas las soluciones en el directorio [`problems/`](problems/). Cada problema tiene su propio archivo JSON con:
- Descripción del problema (7 idiomas)
- Código de solución APL
- Explicación detallada (7 idiomas)
- Análisis de complejidad temporal y espacial

**Índice**: Ver [`problems/index.json`](problems/index.json) para la lista completa.

## 🚀 Características

- ✅ **100+ Problemas Clásicos**: Cobertura completa de los problemas más importantes de LeetCode
- ✅ **Soluciones APL**: Implementaciones únicas usando operaciones poderosas de arrays
- ✅ **Explicaciones Detalladas**: Cada solución incluye análisis de complejidad
- ✅ **7 Idiomas**: Documentación completa en inglés, chino, japonés, español, alemán, francés
- ✅ **Estructura Modular**: Cada problema en su propio archivo JSON
- ✅ **Enfoque Educativo**: Aprende programación de arrays a través de ejemplos prácticos
- ✅ **Código Abierto**: Licencia MIT, contribuciones bienvenidas

## 💻 Cómo Usar

### Navegar en GitHub

¡Simplemente navega este repositorio en GitHub! Todos los problemas están documentados en:
- **Archivos README**: Resumen y problemas destacados (7 idiomas)
- **Directorio problems/**: Archivos individuales de problemas con soluciones completas

### Clonar Localmente

```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# Ver un problema específico
cat problems/001-two-sum.json | jq '.'

# Listar todos los problemas
cat problems/index.json | jq '.'
```

### Probar las Soluciones

Para ejecutar realmente el código APL, necesitarás un intérprete APL:

1. **En línea**: Visita [TryAPL.org](https://tryapl.org/)
2. **Local**: Instala [Dyalog APL](https://www.dyalog.com/download-zone.htm)
3. **GNU APL**: Usa `apt install gnu-apl` (Linux) o `brew install gnu-apl` (macOS)

## 📂 Estructura del Proyecto

```
leetcode-apl-solutions/
├── README.md                  # Documentación en inglés
├── README.zh-TW.md           # Documentación en chino tradicional
├── README.zh-CN.md           # Documentación en chino simplificado
├── README.ja.md              # Documentación en japonés
├── README.es.md              # Documentación en español
├── README.de.md              # Documentación en alemán
├── README.fr.md              # Documentación en francés
├── problems/                  # Directorio de problemas
│   ├── index.json            # Índice de todos los problemas
│   ├── 001-two-sum.json      # Problema individual
│   ├── 136-single-number.json
│   ├── 206-reverse-list.json
│   └── ...                   # Más problemas
├── AI_GENERATED.md           # Descargo de responsabilidad de IA
├── LICENSE                   # Licencia MIT
└── .gitignore               # Configuración de Git

```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Puedes ayudar de las siguientes maneras:

1. **Agregar Más Problemas**: Implementa problemas adicionales de LeetCode en APL
2. **Mejorar Soluciones**: Optimiza las soluciones APL existentes
3. **Corregir Errores**: Reporta y corrige cualquier problema que encuentres
4. **Traducciones**: Ayuda a mejorar las traducciones de idiomas
5. **Documentación**: Mejora las explicaciones de problemas

## 📚 Recursos

### Aprender APL
- [APL Wiki](https://aplwiki.com/) - Documentación completa de APL
- [Tutorial Dyalog APL](https://tutorial.dyalog.com/) - Tutorial oficial de Dyalog
- [APL Cart](https://aplcart.info/) - Modismos APL buscables
- [Try APL](https://tryapl.org/) - Intérprete APL en línea

### LeetCode
- [Problemas LeetCode](https://leetcode.com/problemset/all/) - Lista oficial de problemas
- [Preguntas de Entrevista Top](https://leetcode.com/problem-list/top-interview-questions/)

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🙏 Agradecimientos

- **Kenneth E. Iverson** - Creador de APL
- **LeetCode** - Por proporcionar excelentes problemas algorítmicos
- **Dyalog Ltd** - Por mantener y desarrollar APL
- **Comunidad APL** - Por mantener vivo este hermoso lenguaje

## 📧 Contacto

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [Reportar problemas o sugerencias](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Historial de Estrellas

Si encuentras este proyecto útil, ¡por favor considera darle una estrella! ⭐

---

**Hecho con ❤️ y muchos ⍵, ⍺, ⌽, y ∇**

*"APL es un error, llevado a la perfección."* - Edsger W. Dijkstra

A pesar de las críticas, ¡APL sigue siendo uno de los lenguajes más elegantes y poderosos para manipulación de arrays! 🎯
