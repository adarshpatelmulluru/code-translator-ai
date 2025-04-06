from pathlib import Path
from .file_utils import read_file, write_file
from .language_utils import detect_language_from_extension
from .ollama_utils import query_ollama
from .prompt import generate_translation_prompt, generate_analysis_prompt

def analyze_code(source_file, output_dir=None):
    """Analyze source code and save report"""
    try:
        source_file = Path(source_file).resolve()
        if not output_dir:
            output_dir = source_file.parent
        
        source_lang = detect_language_from_extension(source_file)
        if source_lang == "Unknown":
            raise ValueError(f"Unsupported source language for {source_file.suffix}")
        
        source_code = read_file(source_file)
        if not source_code.strip():
            raise ValueError("Source file is empty")
        
        print(f"Analyzing {source_lang} code...")
        prompt = generate_analysis_prompt(source_code, source_lang)
        analysis = query_ollama(prompt)
        
        if not analysis:
            raise RuntimeError("Analysis returned empty result")
        
        analysis_file = output_dir / f"{source_file.stem}_analysis.md"
        write_file(analysis_file, analysis)
        print(f"Analysis saved to {analysis_file}")
        return True
        
    except Exception as e:
        print(f"Analysis failed: {str(e)}")
        return False

def translate_code(source_file, dest_file):
    """Generalized code translation between any languages"""
    try:
        source_file = Path(source_file).resolve()
        dest_file = Path(dest_file).resolve()
        
        source_lang = detect_language_from_extension(source_file)
        target_lang = detect_language_from_extension(dest_file)
        
        if source_lang == "Unknown":
            raise ValueError(f"Unsupported source language for {source_file.suffix}")
        if target_lang == "Unknown":
            raise ValueError(f"Unsupported target language for {dest_file.suffix}")
        
        source_code = read_file(source_file)
        if not source_code.strip():
            raise ValueError("Source file is empty")
        
        print(f"Translating from {source_lang} to {target_lang}...")
        prompt = generate_translation_prompt(source_code, source_lang, target_lang)
        translated_code = query_ollama(prompt)
        
        if not translated_code:
            raise RuntimeError("Translation returned empty result")
        
        # Clean common artifacts from LLM output
        translated_code = '\n'.join(
            line for line in translated_code.split('\n') 
            if not line.strip().startswith('```')
        ).strip()
        
        write_file(dest_file, translated_code)
        print(f"Successfully translated to {dest_file}")
        
        # Perform analysis on source code
        analyze_code(source_file, dest_file.parent)
        return True
        
    except Exception as e:
        print(f"Translation failed: {str(e)}")
        return False