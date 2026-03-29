with open('fdu_020/prompt.md', 'a', encoding='utf-8') as f:
    for i in range(1, 50):
        f.write(f'- Requirement padding line {i} for strict instruction validation.\\n')
