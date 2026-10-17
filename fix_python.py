import os, re

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='latin1') as f:
                    content = f.read()
                content = content.replace('.iteritems()', '.items()')
                content = re.sub(r'\bprint\s+([^\(\n].*?)$', r'print(\1)', content, flags=re.MULTILINE)
                with open(path, 'w', encoding='latin1') as f:
                    f.write(content)
            except Exception:
                pass
