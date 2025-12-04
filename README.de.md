# 🧠 LeetCode APL Lösungen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> Lösung von über 100 klassischen LeetCode-Problemen mit APL (A Programming Language) - einer der esoterischsten und mächtigsten Array-Programmiersprachen.

> **⚠️ KI-Generierter Inhalt**: Dieses Projekt wurde mit erheblicher KI-Unterstützung erstellt. Siehe [AI_GENERATED.md](./AI_GENERATED.md) für Details. APL-Code wurde nicht in einem tatsächlichen Interpreter getestet. Überprüfung vor Verwendung empfohlen.

**🌍 Sprachen**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🎯 Über Dieses Projekt

Dieses Projekt präsentiert Lösungen zu den beliebtesten LeetCode-Problemen, implementiert in **APL (A Programming Language)**, einer einzigartigen Sprache, die bekannt ist für:

- **Extreme Prägnanz**: Drückt komplexe Algorithmen in sehr wenigen Zeichen aus
- **Array-Orientiert**: Native Unterstützung für leistungsstarke Array-Operationen
- **Mathematische Notation**: Verwendet spezielle Unicode-Symbole (⍵, ⍺, ⌽, ⊥, ∇, usw.)
- **Hohe Lernkurve**: Gilt als eine der am schwierigsten zu erlernenden Sprachen

### Warum APL?

APL fordert konventionelle Programmierparadigmen heraus und bietet:
- Eine völlig andere Art, über Algorithmen nachzudenken
- Elegante Lösungen, die oft die mathematische Essenz von Problemen offenbaren
- Einen reichhaltigen Satz von primitiven Operationen für Array-Manipulation
- Historische Bedeutung als eine der frühesten Hochsprachen

## 📊 Problemabdeckung

| Schwierigkeit | Anzahl | Prozentsatz |
|---------------|--------|-------------|
| 🟢 Einfach    | 40+    | ~35%        |
| 🟡 Mittel     | 50+    | ~50%        |
| 🔴 Schwer     | 15+    | ~15%        |
| **Gesamt**    | **100+** | **100%**  |

## 📝 Problemliste

### Hervorgehobene Probleme

#### #1 - Two Sum (Einfach)
**Problem**: Gegeben ein Array von Ganzzahlen und ein Ziel, gib die Indizes von zwei Zahlen zurück, die sich zum Ziel addieren.

**APL-Lösung**:
```apl
TwoSum ← {
    ⍝ ⍺: Zielsumme, ⍵: Array
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}
```

**Erklärung**: Verwendet äußeres Produkt `∘.` um alle möglichen Paarsummen zu generieren, dann `⍸` um übereinstimmende Indizes zu finden.

**Komplexität**: Zeit O(n²), Raum O(n²)

[📄 Vollständige Lösung](problems/001-two-sum.json)

---

#### #136 - Single Number (Einfach)
**Problem**: Finde das Element, das nur einmal erscheint, in einem Array, wo jedes andere Element zweimal erscheint.

**APL-Lösung**:
```apl
SingleNumber ← {≠/⍵}
```

**Erklärung**: XOR-Reduktion - der eleganteste Einzeiler! Nutzt XOR-Eigenschaften: a⊕a=0 und a⊕0=a.

**Komplexität**: Zeit O(n), Raum O(1)

[📄 Vollständige Lösung](problems/136-single-number.json)

---

#### #206 - Reverse Linked List (Einfach)
**Problem**: Kehre eine einfach verkettete Liste um.

**APL-Lösung**:
```apl
ReverseList ← {⌽⍵}
```

**Erklärung**: `⌽` ist APLs Umkehroperator - die einfachste mögliche Lösung!

**Komplexität**: Zeit O(n), Raum O(1)

[📄 Vollständige Lösung](problems/206-reverse-list.json)

---

### 📚 Alle Probleme

Durchsuche alle Problemlösungen im [`problems/`](problems/) Verzeichnis. Jedes Problem hat seine eigene JSON-Datei mit:
- Problembeschreibung (7 Sprachen)
- APL-Lösungscode
- Detaillierte Erklärung (7 Sprachen)
- Zeit- und Raumkomplexitätsanalyse

**Index**: Siehe [`problems/index.json`](problems/index.json) für die vollständige Liste.

## 🚀 Funktionen

- ✅ **100+ Klassische Probleme**: Umfassende Abdeckung der wichtigsten LeetCode-Probleme
- ✅ **APL-Lösungen**: Einzigartige Implementierungen mit leistungsstarken Array-Operationen
- ✅ **Detaillierte Erklärungen**: Jede Lösung enthält Komplexitätsanalyse
- ✅ **7 Sprachen**: Vollständige Dokumentation in Englisch, Chinesisch, Japanisch, Spanisch, Deutsch, Französisch
- ✅ **Modulare Struktur**: Jedes Problem in seiner eigenen JSON-Datei
- ✅ **Bildungsfokus**: Lerne Array-Programmierung durch praktische Beispiele
- ✅ **Open Source**: MIT-Lizenz, Beiträge willkommen

## 💻 Verwendung

### Auf GitHub Durchsuchen

Durchsuche einfach dieses Repository auf GitHub! Alle Probleme sind dokumentiert in:
- **README-Dateien**: Übersicht und hervorgehobene Probleme (7 Sprachen)
- **problems/ Verzeichnis**: Einzelne Problemdateien mit vollständigen Lösungen

### Lokal Klonen

```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# Ein bestimmtes Problem anzeigen
cat problems/001-two-sum.json | jq '.'

# Alle Probleme auflisten
cat problems/index.json | jq '.'
```

### Lösungen Ausprobieren

Um den APL-Code tatsächlich auszuführen, benötigen Sie einen APL-Interpreter:

1. **Online**: Besuchen Sie [TryAPL.org](https://tryapl.org/)
2. **Lokal**: Installieren Sie [Dyalog APL](https://www.dyalog.com/download-zone.htm)
3. **GNU APL**: Verwenden Sie `apt install gnu-apl` (Linux) oder `brew install gnu-apl` (macOS)

## 📂 Projektstruktur

```
leetcode-apl-solutions/
├── README.md                  # Englische Dokumentation
├── README.zh-TW.md           # Traditionelles Chinesisch
├── README.zh-CN.md           # Vereinfachtes Chinesisch
├── README.ja.md              # Japanische Dokumentation
├── README.es.md              # Spanische Dokumentation
├── README.de.md              # Deutsche Dokumentation
├── README.fr.md              # Französische Dokumentation
├── problems/                  # Problemverzeichnis
│   ├── index.json            # Index aller Probleme
│   ├── 001-two-sum.json      # Einzelnes Problem
│   ├── 136-single-number.json
│   ├── 206-reverse-list.json
│   └── ...                   # Weitere Probleme
├── AI_GENERATED.md           # KI-Haftungsausschluss
├── LICENSE                   # MIT-Lizenz
└── .gitignore               # Git-Konfiguration
```

## 🤝 Beitragen

Beiträge sind willkommen! Sie können auf folgende Weise helfen:

1. **Mehr Probleme Hinzufügen**: Implementieren Sie zusätzliche LeetCode-Probleme in APL
2. **Lösungen Verbessern**: Optimieren Sie bestehende APL-Lösungen
3. **Fehler Beheben**: Melden und beheben Sie gefundene Probleme
4. **Übersetzungen**: Helfen Sie bei der Verbesserung von Sprachübersetzungen
5. **Dokumentation**: Verbessern Sie Problemerklärungen

## 📚 Ressourcen

### APL Lernen
- [APL Wiki](https://aplwiki.com/) - Umfassende APL-Dokumentation
- [Dyalog APL Tutorial](https://tutorial.dyalog.com/) - Offizielles Dyalog-Tutorial
- [APL Cart](https://aplcart.info/) - Durchsuchbare APL-Idiome
- [Try APL](https://tryapl.org/) - Online APL-Interpreter

### LeetCode
- [LeetCode Probleme](https://leetcode.com/problemset/all/) - Offizielle Problemliste
- [Top Interview Fragen](https://leetcode.com/problem-list/top-interview-questions/)

## 📜 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

- **Kenneth E. Iverson** - Schöpfer von APL
- **LeetCode** - Für die Bereitstellung exzellenter algorithmischer Probleme
- **Dyalog Ltd** - Für die Wartung und Entwicklung von APL
- **APL-Community** - Für die Aufrechterhaltung dieser schönen Sprache

## 📧 Kontakt

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [Probleme oder Vorschläge melden](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Stern-Historie

Wenn Sie dieses Projekt nützlich finden, geben Sie ihm bitte einen Stern! ⭐

---

**Gemacht mit ❤️ und vielen ⍵, ⍺, ⌽, und ∇**

*"APL ist ein Fehler, zur Perfektion getrieben."* - Edsger W. Dijkstra

Trotz der Kritik bleibt APL eine der elegantesten und mächtigsten Sprachen für Array-Manipulation! 🎯
