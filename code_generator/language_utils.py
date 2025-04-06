from pathlib import Path
# Extended language mapping with common extensions
LANGUAGE_MAP = {
    # Scripting languages
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.pl': 'Perl',
    '.lua': 'Lua',
    '.r': 'R',
    
    # Compiled languages
    '.java': 'Java',
    '.cs': 'C#',
    '.cpp': 'C++',
    '.c': 'C',
    '.go': 'Go',
    '.rs': 'Rust',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.scala': 'Scala',
    
    # Web languages
    '.ts': 'TypeScript',
    '.jsx': 'JSX',
    '.tsx': 'TSX',
    '.vue': 'Vue',
    '.svelte': 'Svelte',
    
    # Shell/sysadmin
    '.sh': 'Bash',
    '.ps1': 'PowerShell',
    '.bat': 'Batch',
    
    # Configuration
    '.json': 'JSON',
    '.yaml': 'YAML',
    '.yml': 'YAML',
    '.toml': 'TOML',
    '.xml': 'XML'
}

def detect_language_from_extension(file_path):
    """Detect programming language from file extension with fallback"""
    ext = Path(file_path).suffix.lower()
    return LANGUAGE_MAP.get(ext, "Unknown")