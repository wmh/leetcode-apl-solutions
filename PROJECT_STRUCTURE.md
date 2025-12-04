# 📁 Project Structure Overview

## Directory Tree

```
leetcode-apl-solutions/
│
├── 📄 README.md (+ 6 language versions)         # Main entry point
├── 📄 PROBLEMS_INDEX.md (+ 6 language versions) # Complete problem list
├── 📄 HOW_TO_ADD_PROBLEMS.md                    # Contribution guide
├── 📄 QUICK_START.zh-CN.md                      # Quick start (Chinese)
├── 📄 MIGRATION_SUMMARY.md                      # Migration documentation
├── 📄 PROJECT_STRUCTURE.md                      # This file
│
├── 🔧 generate_static_readmes.py                # Main generator script
├── 🔧 generate_problems.py                      # Legacy generator
├── 🔧 generate_problems_batch.sh                # Batch processor
│
└── 📂 problems/
    ├── 📄 index.json                            # Problem metadata
    │
    ├── 📂 001-two-sum/
    │   ├── 📄 README.md                         # English
    │   ├── 📄 README.zh-CN.md                   # Simplified Chinese
    │   ├── �� README.zh-TW.md                   # Traditional Chinese
    │   ├── 📄 README.ja.md                      # Japanese
    │   ├── 📄 README.es.md                      # Spanish
    │   ├── 📄 README.de.md                      # German
    │   └── 📄 README.fr.md                      # French
    │
    ├── 📂 136-single-number/
    │   └── ... (7 language files)
    │
    └── 📂 206-reverse-linked-list/
        └── ... (7 language files)
```

## File Statistics

| Category | Count |
|----------|-------|
| Total Markdown Files | 42 |
| Main READMEs | 7 |
| Problem Index Files | 7 |
| Problem Directories | 3 |
| Problem READMEs | 21 (3 problems × 7 languages) |
| Documentation Files | 4 |
| Scripts | 3 |

## Language Support

All user-facing content is available in **7 languages**:

| Code | Language | Flag |
|------|----------|------|
| en | English | 🇬🇧 |
| zh-CN | 简体中文 (Simplified Chinese) | 🇨🇳 |
| zh-TW | 繁體中文 (Traditional Chinese) | 🇹🇼 |
| ja | 日本語 (Japanese) | 🇯🇵 |
| es | Español (Spanish) | 🇪🇸 |
| de | Deutsch (German) | 🇩🇪 |
| fr | Français (French) | 🇫🇷 |

## Key Files Description

### Main Documentation

| File | Purpose |
|------|---------|
| `README.md` | Project homepage with overview and featured problems |
| `PROBLEMS_INDEX.md` | Complete table of all problems with links |
| `HOW_TO_ADD_PROBLEMS.md` | Guide for contributors |
| `QUICK_START.zh-CN.md` | Quick start guide in Chinese |
| `MIGRATION_SUMMARY.md` | Documentation of migration from server to static |
| `PROJECT_STRUCTURE.md` | This file - project structure overview |

### Scripts

| File | Purpose |
|------|---------|
| `generate_static_readmes.py` | Generates all README files from JSON data |
| `generate_problems.py` | Legacy problem generator (can create new problem JSON files) |
| `generate_problems_batch.sh` | Batch processing utility |

### Data Files

| File | Purpose |
|------|---------|
| `problems/index.json` | Master list of all problems |
| `problems/*.json` | Individual problem data files |

## Problem File Structure

Each problem has:
- 1 JSON source file (e.g., `001-two-sum.json`)
- 1 directory (e.g., `001-two-sum/`)
- 7 README files (one per language)

### Example Problem Directory

```
001-two-sum/
├── README.md           # English - default
├── README.zh-CN.md     # Simplified Chinese
├── README.zh-TW.md     # Traditional Chinese
├── README.ja.md        # Japanese
├── README.es.md        # Spanish
├── README.de.md        # German
└── README.fr.md        # French
```

## Content Flow

```
JSON Source Files
      ↓
[generate_static_readmes.py]
      ↓
Markdown README Files
      ↓
GitHub / User Browser
```

## Navigation Flow

```
README.md (Homepage)
    ↓
PROBLEMS_INDEX.md (Problem List)
    ↓
001-two-sum/README.md (Specific Problem)
    ↓
(Language Switcher at top of page)
    ↓
001-two-sum/README.zh-CN.md (Same problem, different language)
```

## Update Workflow

1. **Add new problem**:
   ```bash
   # Create problems/XXX-name.json
   # Add entry to problems/index.json
   ```

2. **Generate READMEs**:
   ```bash
   python3 generate_static_readmes.py
   ```

3. **Result**:
   - Creates `problems/XXX-name/` directory
   - Generates 7 README files
   - Updates all PROBLEMS_INDEX files

## Expansion Capacity

Current structure can easily support:
- ✅ 1000+ problems
- ✅ Additional languages
- ✅ Multiple solution approaches per problem
- ✅ Category-based organization
- ✅ Difficulty-based indexes
- ✅ Tag-based filtering

## Technology Stack

| Component | Technology |
|-----------|------------|
| Content Format | Markdown |
| Data Format | JSON |
| Generator | Python 3 |
| Hosting | GitHub (static) |
| Version Control | Git |
| Languages | 7 (i18n) |

## Dependencies

### Required
- Python 3.6+
- Standard library only (json, os, pathlib)

### Optional
- Markdown viewer (VS Code, Typora, etc.)
- APL interpreter (Dyalog, GNU APL)

## Best Practices

### For Readers
1. Start with `README.md`
2. Browse `PROBLEMS_INDEX.md`
3. Use language switcher for preferred language
4. Try code at [TryAPL.org](https://tryapl.org/)

### For Contributors
1. Read `HOW_TO_ADD_PROBLEMS.md`
2. Create well-formatted JSON
3. Test APL code before submitting
4. Ensure all 7 languages are included
5. Run generator and verify output

### For Maintainers
1. Keep `index.json` sorted by problem number
2. Maintain consistent naming: `XXX-slug-name`
3. Regenerate all READMEs after JSON changes
4. Test links after major updates
5. Keep translations synchronized

## Future Enhancements

Possible additions:
- [ ] Category-based problem grouping
- [ ] Difficulty-specific index pages
- [ ] Algorithm pattern guides
- [ ] Interactive APL playground links
- [ ] Video explanations
- [ ] Test cases for each problem
- [ ] Alternative solution approaches
- [ ] Related problems suggestions

---

**Last Updated**: December 2024
**Total Problems**: 3 (fully documented)
**Target**: 100+ problems
**Languages**: 7
**Format**: 100% static Markdown
