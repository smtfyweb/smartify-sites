# Diretrizes Técnicas - Projeto Smartify WEB

Este documento serve como guia técnico e histórico para o desenvolvimento e modernização do repositório de templates focado em **Negócios Locais**.

## 1. Estado Atual do Repositório (Legacy Stack)
O repositório contém uma coleção de templates baseados no tema Porto, higienizados (White Label) para a marca "Smartify WEB".

*   **Arquitetura**: Sites estáticos multipágina (MPA).
*   **Frontend**: HTML5, Bootstrap v4.x, jQuery v3.x.
*   **Ativos**: Font Awesome 5, Simple Line Icons, Owl Carousel, Nouislider.
*   **Idioma**: Configurado para `pt-br` em todos os arquivos HTML.

## 2. Visão de Negócio
O objetivo é criar uma agência de desenvolvimento rápido para negócios locais (dentistas, advogados, oficinas, etc.), utilizando GitHub Pages para hospedagem de demonstrações (previews) e implementando backends customizados apenas sob demanda após a venda.

## 3. Plano de Modernização Proposto (Vite Workflow)
Para otimizar a performance e modernizar o desenvolvimento sem alterar a linguagem base, propõe-se a introdução do **Vite** como ferramenta de build.

### Objetivos Técnicos da Modernização:
*   **Build Tool**: Utilizar Vite para gerenciar ativos e servir um ambiente de desenvolvimento com Hot Module Replacement (HMR).
*   **Otimização de Imagens**: Conversão automática de ativos `.jpg`/`.png` para **WebP/AVIF** via plugins do Vite (ex: `vite-plugin-imagemin`).
*   **CSS Purging**: Implementação de **PurgeCSS** ou **UnCSS** para remover estilos não utilizados do Bootstrap, reduzindo drasticamente o peso dos arquivos finais.
*   **Minificação**: Compactação agressiva de HTML, CSS e JS para a pasta de distribuição (`/dist`).
*   **Deployment**: Pipeline automatizada via GitHub Actions para publicar a pasta `/dist` no GitHub Pages.

### Estrutura de Pastas Alvo:
```text
/
├── src/                # Arquivos HTML/CSS/JS originais (Editáveis)
├── public/             # Ativos estáticos que não precisam de build
├── dist/               # Resultado final otimizado (Gerado pelo Vite)
├── package.json        # Dependências e scripts do Vite
└── vite.config.js      # Configurações de otimização
```

## 4. Diretrizes para Personalização
Ao criar um novo template para um nicho específico:
1.  **Herança de Estilos**: Utilizar o arquivo `css/custom-local.css` para sobreposições de design premium (Glassmorphism, animações).
2.  **Conversão de Leads**: Priorizar CTAs de WhatsApp e Formulários de Contato.
3.  **SEO Local**: Implementar Microdados JSON-LD (`LocalBusiness`) em cada template.

## 5. Integração de Backend
O backend deve ser tratado como uma camada desacoplada:
*   **Fase de Preview**: Utilizar serviços serverless para formulários (ex: Formspree).
*   **Fase de Produção**: Implementar APIs REST conforme a necessidade do cliente, mantendo o frontend estático otimizado.

---
*Documento gerado por Antigravity AI em 04/05/2026 para fins de continuidade de desenvolvimento.*
