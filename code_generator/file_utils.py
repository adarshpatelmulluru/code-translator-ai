from pathlib import Path

def read_file(file_path):
    """Universal file reader with encoding detection"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            
        # Try UTF-8 first
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            # Fallback to common encodings
            for encoding in ['utf-16', 'cp1252']:
                try:
                    return content.decode(encoding)
                except UnicodeDecodeError:
                    continue
            raise ValueError(f"Could not decode {file_path} with standard encodings")
    except Exception as e:
        raise IOError(f"Failed to read {file_path}: {str(e)}")

def write_file(file_path, content):
    """Universal file writer with directory creation"""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise IOError(f"Failed to write {file_path}: {str(e)}")