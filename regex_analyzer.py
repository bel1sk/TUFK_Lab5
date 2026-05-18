import re

class RegexAnalyzer:
    def __init__(self):
        self.patterns = [
            r"<!--[\s\S]*?-->",
            r"\{[\s\S]*?\}|\(\*[\s\S]*?\*\)",
            r"(?i)\brgb\(\s*(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*,\s*(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*,\s*(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*\)"
        ]

    def analyze(self, code, choice_index):
        if choice_index < 0 or choice_index >= len(self.patterns):
            return []
            
        pattern = self.patterns[choice_index]
        matches = list(re.finditer(pattern, code))
        
        results = []
        for match in matches:
            substr = match.group(0)
            start_pos = match.start()
            
            lines = code[:start_pos].split('\n')
            row = len(lines)
            col = len(lines[-1]) + 1
            
            results.append({
                'substring': substr,
                'row': row,
                'col': col,
                'length': len(substr)
            })
            
        return results
