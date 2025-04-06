def generate_translation_prompt(source_code, source_lang, target_lang):
    """Generate language-agnostic translation prompt"""
    return f"""Translate the following {source_lang} code to {target_lang}. 
Provide ONLY the translated code with:
- Add imports of necessary libraries
- Follow proper language syntax and structure
- NO additional explanations
- NO comments about the translation
- NO markdown formatting
- NO code block markers
- NO introductory text

The output should be production-ready code that compiles/runs in {target_lang}.

Source code:
{source_code}"""

def generate_analysis_prompt(source_code, source_lang):
    """Generate code analysis prompt"""
    return f"""Analyze the following {source_lang} code. Provide a concise technical analysis focusing on:
1. Code structure and organization
2. Potential bugs or edge cases
3. Performance considerations
4. Security vulnerabilities
5. Style improvements

Format as markdown with no introductory text. Omit sections where no improvements are needed.

Code to analyze:
{source_code}"""