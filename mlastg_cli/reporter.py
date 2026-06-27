import json
from typing import List, Dict, Any
from datetime import datetime

def generate_report(results: List[Dict[str, Any]], output_file: str, format_type: str = 'both'):
    """Generates a compliance report based on the test results."""
    
    if format_type in ['json', 'both']:
        json_file = output_file if output_file.endswith('.json') else output_file.replace('.md', '.json')
        with open(json_file, 'w') as f:
            json.dump({"timestamp": datetime.now().isoformat(), "results": results}, f, indent=2)
            
    if format_type in ['markdown', 'both']:
        md_file = output_file if output_file.endswith('.md') else output_file.replace('.json', '.md')
        
        passed = [r for r in results if r['status'] == 'pass']
        failed = [r for r in results if r['status'] == 'fail']
        errors = [r for r in results if r['status'] == 'error']
        
        total = len(results)
        score = (len(passed) / total * 100) if total > 0 else 0
        
        md_content = f"# MLASTG Compliance Report\n\n"
        md_content += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md_content += f"**Compliance Score:** {score:.1f}%\n\n"
        
        md_content += f"## Summary\n"
        md_content += f"- **Passed:** {len(passed)}\n"
        md_content += f"- **Failed:** {len(failed)}\n"
        md_content += f"- **Errors:** {len(errors)}\n\n"
        
        md_content += f"## Detailed Findings\n\n"
        
        if failed:
            md_content += f"### ❌ Failed Controls\n"
            for fail in failed:
                md_content += f"#### {fail['test_id']}: {fail['name']} (Severity: {fail['severity']})\n"
                md_content += f"- **Control:** {fail['control']}\n"
                md_content += f"- **Evidence:** {fail['evidence'][0]}\n\n"
                
        if passed:
            md_content += f"### ✅ Passed Controls\n"
            for p in passed:
                md_content += f"- **{p['test_id']}**: {p['name']} ({p['control']})\n"
                
        if errors:
            md_content += f"\n### ⚠️ Test Execution Errors\n"
            for e in errors:
                md_content += f"- **{e['test_id']}**: Test could not be completed successfully.\n"
                
        with open(md_file, 'w') as f:
            f.write(md_content)
