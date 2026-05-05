import os
import re

def clean_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Corrigir Comentários Aninhados (O maior vilão do Vite)
    # Transforma <!-- <!-- --> --> em <!-- - - - - -->
    def fix_comments(match):
        inner = match.group(1)
        inner = inner.replace('<!--', '- -').replace('-->', '- -')
        return f'<!--{inner}-->'
    
    content = re.sub(r'<!--(.*?)-->', fix_comments, content, flags=re.DOTALL)

    # 2. Corrigir atributos mal formados (ex: width:100% " com espaço interno)
    content = re.sub(r'style="([^"]*?) "', r'style="\1"', content)
    content = re.sub(r'class="([^"]*?) "', r'class="\1"', content)

    # 3. Remover scripts do Cloudflare/Email Decode que dão erro de resolução
    content = re.sub(r'<script [^>]*email-decode.min.js[^>]*></script>', '', content)
    
    # 4. Corrigir links com caracteres especiais quebrados (&#)
    content = content.replace('&#', '&')

    # 5. Garantir PT-BR e type="module"
    content = content.replace('lang="en"', 'lang="pt-br"')
    content = re.sub(r'<script (?!type="module")', '<script type="module" ', content)
    content = content.replace('type="module" type="module"', 'type="module"')
    
    # 6. Limpeza de caminhos (Garantir que não haja barra dupla)
    content = content.replace('/landing//landing/', '/landing/')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    src_dir = 'src'
    count = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.html'):
                clean_html(os.path.join(root, file))
                count += 1
    print(f'Sucesso! {count} arquivos sanitizados profundamente.')

if __name__ == '__main__':
    main()
