#!/usr/bin/env python3
"""
Validate APL solutions by actually running them in GNU APL interpreter.
"""

import json
import subprocess
import os
from pathlib import Path
import time

class APLValidator:
    def __init__(self):
        self.results = {
            'validated': [],
            'failed': [],
            'syntax_errors': [],
            'not_tested': []
        }
    
    def test_apl_code(self, code, test_input=None):
        """Test APL code in GNU APL interpreter."""
        try:
            # Create temporary APL script
            script = code
            if test_input:
                script += f"\n{test_input}"
            
            # Run in APL
            result = subprocess.run(
                ['apl', '--silent', '--'],
                input=script,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Timeout'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def validate_problem(self, problem_file):
        """Validate a single problem's APL solution."""
        print(f"\n{'='*60}")
        print(f"Testing: {problem_file.name}")
        print('='*60)
        
        with open(problem_file, 'r', encoding='utf-8') as f:
            problem = json.load(f)
        
        num = problem['number']
        title = problem['title']
        solution = problem['aplSolution']
        
        print(f"#{num} - {title}")
        print(f"\nAPL Code:")
        print(solution)
        print()
        
        # Test the code
        result = self.test_apl_code(solution)
        
        if result['success']:
            print("✅ Syntax OK")
            if result['output']:
                print(f"Output: {result['output'][:200]}")
            self.results['validated'].append({
                'num': num,
                'title': title,
                'file': problem_file.name
            })
            return True
        else:
            print(f"❌ FAILED")
            if result['error']:
                print(f"Error: {result['error'][:500]}")
            self.results['syntax_errors'].append({
                'num': num,
                'title': title,
                'file': problem_file.name,
                'error': result['error']
            })
            return False
    
    def validate_all(self, problems_dir):
        """Validate all problem solutions."""
        problems_dir = Path(problems_dir)
        problem_files = sorted(problems_dir.glob('[0-9]*.json'))
        
        print(f"\n🔍 Found {len(problem_files)} problem files to validate\n")
        
        for i, problem_file in enumerate(problem_files, 1):
            print(f"\n[{i}/{len(problem_files)}]", end=' ')
            self.validate_problem(problem_file)
            time.sleep(0.1)  # Small delay between tests
        
        self.print_summary()
    
    def print_summary(self):
        """Print validation summary."""
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)
        
        total = len(self.results['validated']) + len(self.results['failed']) + len(self.results['syntax_errors'])
        
        print(f"\n✅ Passed (Syntax OK):     {len(self.results['validated'])}/{total}")
        print(f"❌ Syntax Errors:          {len(self.results['syntax_errors'])}/{total}")
        print(f"⚠️  Not Tested:            {len(self.results['not_tested'])}/{total}")
        
        if self.results['syntax_errors']:
            print("\n" + "-"*60)
            print("PROBLEMS WITH SYNTAX ERRORS:")
            print("-"*60)
            for item in self.results['syntax_errors'][:10]:  # Show first 10
                print(f"  #{item['num']} - {item['title']}")
                if 'error' in item:
                    error_lines = item['error'].split('\n')[:3]
                    for line in error_lines:
                        if line.strip():
                            print(f"    {line[:100]}")
        
        # Save detailed results
        with open('validation_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📄 Detailed results saved to: validation_results.json")
        
        # Calculate percentage
        if total > 0:
            pass_rate = (len(self.results['validated']) / total) * 100
            print(f"\n📊 Pass Rate: {pass_rate:.1f}%")

def main():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           APL Solutions Validation System                     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    validator = APLValidator()
    
    # Validate all problems
    problems_dir = Path(__file__).parent / 'problems'
    validator.validate_all(problems_dir)

if __name__ == '__main__':
    main()
