#!/usr/bin/env python3
"""
Generate static README files for all LeetCode problems.
Converts JSON problem files into beautiful markdown READMEs.
"""

import json
import os
from pathlib import Path

# Define difficulty emoji and colors
DIFFICULTY_MAP = {
    "easy": {"emoji": "🟢", "label": "Easy"},
    "medium": {"emoji": "🟡", "label": "Medium"},
    "hard": {"emoji": "🔴", "label": "Hard"}
}

# Language labels
LANG_LABELS = {
    "en": "🇬🇧 English",
    "zh-CN": "🇨🇳 简体中文",
    "zh-TW": "🇹🇼 繁體中文",
    "ja": "🇯🇵 日本語",
    "es": "🇪🇸 Español",
    "de": "🇩🇪 Deutsch",
    "fr": "🇫🇷 Français"
}

def generate_problem_readme(problem_data, problems_dir):
    """Generate a README.md for a single problem in all languages."""
    
    number = problem_data.get('number')
    title = problem_data.get('title')
    difficulty = problem_data.get('difficulty', 'medium')
    
    # Create problem directory
    problem_dir = problems_dir / f"{number:03d}-{title.lower().replace(' ', '-')}"
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate README for each language
    for lang_code in LANG_LABELS.keys():
        readme_name = f"README.{lang_code}.md" if lang_code != "en" else "README.md"
        readme_path = problem_dir / readme_name
        
        content = generate_readme_content(problem_data, lang_code, difficulty)
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return problem_dir

def generate_readme_content(problem, lang, difficulty):
    """Generate markdown content for a problem in a specific language."""
    
    number = problem.get('number')
    title = problem.get('title')
    diff_info = DIFFICULTY_MAP.get(difficulty, DIFFICULTY_MAP['medium'])
    
    description = problem.get('description', {}).get(lang, "No description available.")
    explanation = problem.get('explanation', {}).get(lang, "No explanation available.")
    apl_solution = problem.get('aplSolution', '# No solution available')
    time_complexity = problem.get('timeComplexity', 'N/A')
    space_complexity = problem.get('spaceComplexity', 'N/A')
    
    # Build language navigation
    lang_nav = " | ".join([
        f"[{LANG_LABELS[lc].split()[1]}](README.{lc}.md)" if lc != "en" 
        else f"[{LANG_LABELS[lc].split()[1]}](README.md)" 
        for lc in LANG_LABELS.keys()
    ])
    
    # Translations
    translations = {
        "en": {
            "back": "⬅️ Back to Problems",
            "problem": "Problem",
            "difficulty": "Difficulty",
            "solution": "APL Solution",
            "explanation": "Explanation",
            "complexity": "Complexity Analysis",
            "time": "Time Complexity",
            "space": "Space Complexity",
            "tags": "Tags",
            "similar": "Similar Problems",
            "resources": "Resources"
        },
        "zh-CN": {
            "back": "⬅️ 返回题目列表",
            "problem": "题目",
            "difficulty": "难度",
            "solution": "APL 解法",
            "explanation": "解释",
            "complexity": "复杂度分析",
            "time": "时间复杂度",
            "space": "空间复杂度",
            "tags": "标签",
            "similar": "相似题目",
            "resources": "资源"
        },
        "zh-TW": {
            "back": "⬅️ 返回題目列表",
            "problem": "題目",
            "difficulty": "難度",
            "solution": "APL 解法",
            "explanation": "解釋",
            "complexity": "複雜度分析",
            "time": "時間複雜度",
            "space": "空間複雜度",
            "tags": "標籤",
            "similar": "相似題目",
            "resources": "資源"
        },
        "ja": {
            "back": "⬅️ 問題リストに戻る",
            "problem": "問題",
            "difficulty": "難易度",
            "solution": "APL 解法",
            "explanation": "説明",
            "complexity": "複雑度分析",
            "time": "時間計算量",
            "space": "空間計算量",
            "tags": "タグ",
            "similar": "類似問題",
            "resources": "リソース"
        },
        "es": {
            "back": "⬅️ Volver a Problemas",
            "problem": "Problema",
            "difficulty": "Dificultad",
            "solution": "Solución APL",
            "explanation": "Explicación",
            "complexity": "Análisis de Complejidad",
            "time": "Complejidad Temporal",
            "space": "Complejidad Espacial",
            "tags": "Etiquetas",
            "similar": "Problemas Similares",
            "resources": "Recursos"
        },
        "de": {
            "back": "⬅️ Zurück zu Problemen",
            "problem": "Problem",
            "difficulty": "Schwierigkeit",
            "solution": "APL-Lösung",
            "explanation": "Erklärung",
            "complexity": "Komplexitätsanalyse",
            "time": "Zeitkomplexität",
            "space": "Raumkomplexität",
            "tags": "Tags",
            "similar": "Ähnliche Probleme",
            "resources": "Ressourcen"
        },
        "fr": {
            "back": "⬅️ Retour aux Problèmes",
            "problem": "Problème",
            "difficulty": "Difficulté",
            "solution": "Solution APL",
            "explanation": "Explication",
            "complexity": "Analyse de Complexité",
            "time": "Complexité Temporelle",
            "space": "Complexité Spatiale",
            "tags": "Tags",
            "similar": "Problèmes Similaires",
            "resources": "Ressources"
        }
    }
    
    t = translations.get(lang, translations["en"])# Generate markdown
    md = f"""# {number}. {title}

{lang_nav}

[{t['back']}](../../README{'.' + lang if lang != 'en' else ''}.md)

---

## {diff_info['emoji']} {t['difficulty']}: {diff_info['label']}

## {t['problem']}

{description}

## 💡 {t['solution']}

```apl
{apl_solution}
```

## 📝 {t['explanation']}

{explanation}

## ⏱️ {t['complexity']}

- **{t['time']}**: `{time_complexity}`
- **{t['space']}**: `{space_complexity}`

---

## 📚 {t['resources']}

- [LeetCode Problem #{number}](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README{'.' + lang if lang != 'en' else ''}.md)
"""
    
    return md

def generate_index_readme(problems_list, output_path, lang="en"):
    """Generate the main index README with all problems listed."""
    
    # Sort problems by number
    sorted_problems = sorted(problems_list, key=lambda x: x.get('number', 0))
    
    # Count by difficulty
    difficulty_counts = {"easy": 0, "medium": 0, "hard": 0}
    for p in sorted_problems:
        diff = p.get('difficulty', 'medium')
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
    
    # Translations
    translations = {
        "en": {
            "title": "LeetCode APL Solutions - Problem Index",
            "subtitle": "100+ Classic LeetCode Problems Solved in APL",
            "back": "⬅️ Back to Main",
            "stats": "Statistics",
            "total": "Total Problems",
            "list": "Problem List",
            "number": "#",
            "title_col": "Title",
            "difficulty": "Difficulty",
            "complexity": "Complexity"
        },
        "zh-CN": {
            "title": "LeetCode APL 解法 - 题目索引",
            "subtitle": "100+ 道 LeetCode 经典题目的 APL 解法",
            "back": "⬅️ 返回主页",
            "stats": "统计信息",
            "total": "题目总数",
            "list": "题目列表",
            "number": "编号",
            "title_col": "题目",
            "difficulty": "难度",
            "complexity": "复杂度"
        },
        "zh-TW": {
            "title": "LeetCode APL 解法 - 題目索引",
            "subtitle": "100+ 道 LeetCode 經典題目的 APL 解法",
            "back": "⬅️ 返回主頁",
            "stats": "統計資訊",
            "total": "題目總數",
            "list": "題目列表",
            "number": "編號",
            "title_col": "題目",
            "difficulty": "難度",
            "complexity": "複雜度"
        },
        "ja": {
            "title": "LeetCode APL 解法 - 問題インデックス",
            "subtitle": "100+ の LeetCode クラシック問題の APL 解法",
            "back": "⬅️ メインに戻る",
            "stats": "統計",
            "total": "合計問題数",
            "list": "問題リスト",
            "number": "番号",
            "title_col": "タイトル",
            "difficulty": "難易度",
            "complexity": "計算量"
        },
        "es": {
            "title": "Soluciones LeetCode APL - Índice de Problemas",
            "subtitle": "100+ Problemas Clásicos de LeetCode Resueltos en APL",
            "back": "⬅️ Volver a Principal",
            "stats": "Estadísticas",
            "total": "Problemas Totales",
            "list": "Lista de Problemas",
            "number": "N°",
            "title_col": "Título",
            "difficulty": "Dificultad",
            "complexity": "Complejidad"
        },
        "de": {
            "title": "LeetCode APL Lösungen - Problemindex",
            "subtitle": "100+ klassische LeetCode-Probleme in APL gelöst",
            "back": "⬅️ Zurück zur Hauptseite",
            "stats": "Statistiken",
            "total": "Gesamtprobleme",
            "list": "Problemliste",
            "number": "Nr.",
            "title_col": "Titel",
            "difficulty": "Schwierigkeit",
            "complexity": "Komplexität"
        },
        "fr": {
            "title": "Solutions LeetCode APL - Index des Problèmes",
            "subtitle": "100+ Problèmes Classiques LeetCode Résolus en APL",
            "back": "⬅️ Retour à l'Accueil",
            "stats": "Statistiques",
            "total": "Problèmes Totaux",
            "list": "Liste des Problèmes",
            "number": "N°",
            "title_col": "Titre",
            "difficulty": "Difficulté",
            "complexity": "Complexité"
        }
    }
    
    t = translations.get(lang, translations["en"])
    
    # Build problem table
    table_rows = []
    for p in sorted_problems:
        num = p.get('number')
        title = p.get('title')
        diff = p.get('difficulty', 'medium')
        diff_info = DIFFICULTY_MAP.get(diff, DIFFICULTY_MAP['medium'])
        time_c = p.get('timeComplexity', 'N/A')
        
        # Problem link
        problem_slug = f"{num:03d}-{title.lower().replace(' ', '-')}"
        readme_link = f"problems/{problem_slug}/README{'.' + lang if lang != 'en' else ''}.md"
        
        table_rows.append(
            f"| {num} | [{title}]({readme_link}) | {diff_info['emoji']} {diff_info['label']} | {time_c} |"
        )
    
    table = "\n".join(table_rows)
    
    # Generate markdown
    md = f"""# {t['title']}

{t['subtitle']}

[{t['back']}](README{'.' + lang if lang != 'en' else ''}.md)

---

## 📊 {t['stats']}

| {t['difficulty']} | Count | Percentage |
|------------|-------|------------|
| 🟢 Easy    | {difficulty_counts['easy']}   | {difficulty_counts['easy'] * 100 // len(sorted_problems)}%       |
| 🟡 Medium  | {difficulty_counts['medium']}   | {difficulty_counts['medium'] * 100 // len(sorted_problems)}%       |
| 🔴 Hard    | {difficulty_counts['hard']}   | {difficulty_counts['hard'] * 100 // len(sorted_problems)}%       |
| **{t['total']}**  | **{len(sorted_problems)}** | **100%** |

---

## 📝 {t['list']}

| {t['number']} | {t['title_col']} | {t['difficulty']} | {t['complexity']} |
|------|-------|------------|------------|
{table}

---

**Made with ❤️ using APL** • [View on GitHub](https://github.com/wmh/leetcode-apl-solutions)
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

def main():
    """Main function to generate all static README files."""
    
    # Get current directory
    base_dir = Path(__file__).parent
    problems_json_dir = base_dir / "problems"
    problems_output_dir = base_dir / "problems"
    
    # Load index.json to get all problems
    index_file = problems_json_dir / "index.json"
    
    if not index_file.exists():
        print("❌ index.json not found!")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    print(f"📚 Found {len(index_data)} problems in index.json")
    
    # Load all problem data
    all_problems = []
    
    for item in index_data:
        problem_file = problems_json_dir / item['file']
        
        if problem_file.exists():
            with open(problem_file, 'r', encoding='utf-8') as f:
                problem_data = json.load(f)
                all_problems.append(problem_data)
                
                # Generate README for this problem
                problem_dir = generate_problem_readme(problem_data, problems_output_dir)
                print(f"✅ Generated: {problem_dir.name}")
        else:
            print(f"⚠️  Skipped: {item['file']} (not found)")
    
    # Generate index READMEs for all languages
    for lang in LANG_LABELS.keys():
        index_name = f"PROBLEMS_INDEX.{lang}.md" if lang != "en" else "PROBLEMS_INDEX.md"
        index_path = base_dir / index_name
        generate_index_readme(all_problems, index_path, lang)
        print(f"✅ Generated: {index_name}")
    
    print(f"\n🎉 Done! Generated {len(all_problems)} problem READMEs in 7 languages")
    print(f"📁 Total files created: {len(all_problems) * 7 + 7}")

if __name__ == "__main__":
    main()
