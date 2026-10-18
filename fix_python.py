import os, re

# Carpetas críticas a corregir (evitando bionic y external que se rompen)
TARGET_DIRS = ['build', 'device', 'vendor', 'system']

for target_dir in TARGET_DIRS:
    if not os.path.exists(target_dir):
        continue
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='latin1') as f:
                        content = f.read()
                    
                    # Reemplazar iteritems
                    content = content.replace('.iteritems()', '.items()')
                    
                    # Convertir print de Python 2 a Python 3 solo si no tiene paréntesis
                    content = re.sub(r'\bprint\s+([^\(\n\s].*?)$', r'print(\1)', content, flags=re.MULTILINE)
                    
                    with open(path, 'w', encoding='latin1') as f:
                        f.write(content)
                except Exception:
                    pass
