const { defineConfig } = require('vite');
const { resolve } = require('path');
const glob = require('glob');

// Busca todos os arquivos HTML na pasta src para configurar como inputs do Rollup (MPA)
const htmlFiles = glob.sync('src/**/*.html').reduce((acc, file) => {
    // Cria um nome de entrada amigável baseado no caminho do arquivo
    const entryName = file.replace(/^src\//, '').replace(/\.html$/, '');
    acc[entryName] = resolve(__dirname, file);
    return acc;
}, {});

module.exports = defineConfig({
    root: 'src',
    publicDir: resolve(__dirname, 'public'),
    base: '/smartify-sites/', // Nome do seu repositório no GitHub
    build: {
        outDir: '../dist',
        emptyOutDir: true,
        rollupOptions: {
            input: htmlFiles
        }
    },
    server: {
        port: 3000,
        open: true
    },
    css: {
        lightningcss: {
            errorRecovery: true
        }
    }
});
