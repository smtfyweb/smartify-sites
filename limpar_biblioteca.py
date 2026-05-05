import os
import re

def clean_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Corrigir Comentários Aninhados
    def fix_comments(match):
        inner = match.group(1)
        inner = inner.replace('<!--', '- -').replace('-->', '- -')
        return f'<!--{inner}-->'
    content = re.sub(r'<!--(.*?)-->', fix_comments, content, flags=re.DOTALL)

    # 2. Corrigir falta de espaço entre atributos (ex: "viewport"content)
    # Procura por algo terminado em aspas seguido direto por uma letra
    content = re.sub(r'(\"[a-zA-Z])', r'" \1', content)
    # Corrigir o erro específico reportado: "viewport"content -> "viewport" content
    content = content.replace('"content=', '" content=')
    content = content.replace('"type=', '" type=')
    content = content.replace('"href=', '" href=')

    # 3. Remover scripts do Cloudflare
    content = re.sub(r'<script [^>]*email-decode.min.js[^>]*></script>', '', content)
    
    # 4. Corrigir caminhos e links
    content = content.replace('&#', '&')
    content = content.replace('/landing//landing/', '/landing/')

    # 5. Garantir PT-BR e type="module"
    content = content.replace('lang="en"', 'lang="pt-br"')
    content = re.sub(r'<script (?!type="module")', '<script type="module" ', content)
    content = content.replace('type="module" type="module"', 'type="module"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    src_dir = 'src'
    # Remover o arquivo de documentação que está com erro e não é necessário no catálogo
    if os.path.exists('src/documentation.html'):
        os.remove('src/documentation.html')
        print('Arquivo documentation.html removido para evitar erros de build.')

    count = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.html'):
                clean_html(os.path.join(root, file))
                count += 1
    print(f'Sucesso! {count} arquivos sanitizados profundamente.')

if __name__ == '__main__':
    main()
