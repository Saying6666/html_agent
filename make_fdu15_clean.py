import os

with open('fdu_015/prompt.md', 'w', encoding='utf-8') as f:
    text = '''# Modern Premium Glassmorphism UI Development Specification\n\n''' * 170
    f.write(text)

with open('fdu_015/src/index.html', 'w', encoding='utf-8') as f:
    text = '''<!DOCTYPE html>\n<html>\n<head><title>Test</title></head>\n<body>\n''' 
    body = '''<div><h1>Hello</h1><p>Test</p></div>\n''' * 650
    text += body + '''</body>\n</html>'''
    f.write(text)

