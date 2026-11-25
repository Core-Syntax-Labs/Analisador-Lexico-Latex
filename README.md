# 📊 Apresentação: Analisador Léxico - Linguagens Formais e Automato

Este repositório contém o código-fonte em **LaTeX** e o arquivo compilado em **PDF** de uma apresentação de slides (utilizando a classe `Beamer`) sobre **Analisador Léxico**, um componente fundamental na arquitetura de compiladores.

## 👥 Participantes

| Nome do Aluno | Nº da Matrícula | 
| ----- | ----- | 
| \[Alanderson Santos Lima de Queiroz\] | `[01696725]` | 
| \[Ryan Rodrigues dos Santos\] | `[01707035]` | 
| \[Daniel Manoel Santos da Silva\] | `[01841723]` | 
| \[Rafael Alexandre Soares Leite Galvão\] | `[01841723]` | 
| \[Samuel Douglas dos Santos\] | `[01709345]` | 

## 📁 Estrutura do Repositório

Abaixo está a descrição dos principais arquivos presentes no projeto:

* `Analisador Léxico.tex` — Código-fonte principal da apresentação em LaTeX.

* `Analisador Léxico.pdf` — Versão final compilada dos slides pronta para visualização/apresentação.

* `LICENSE` — Arquivo de licença do projeto.

* `README.md` — Documentação do repositório.

> **Nota sobre arquivos auxiliares:** O repositório também inclui arquivos gerados automaticamente durante o processo de compilação do LaTeX/Beamer (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.synctex.gz`, `.toc`, `.vrb`).

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** LaTeX

* **Classe de Documento:** Beamer *(identificada pelos arquivos auxiliares `.nav`, `.snm` e `.vrb`)*

* **Distribuição/Compilador utilizado:** MiKTeX (`pdflatex`)

## 🚀 Como Compilar o Projeto

Caso deseje editar o arquivo `.tex` e gerar um novo `.pdf`, siga os passos abaixo:

### 1. Compilação Local (via Terminal)

Certifique-se de ter uma distribuição LaTeX instalada em sua máquina (como **MiKTeX**, **TeX Live** ou **MacTeX**) e execute:

```
pdflatex "Analisador Léxico.tex"

```

*(Dica: Execute o comando duas vezes seguidas para garantir que o sumário `.toc` e as referências de navegação dos slides sejam atualizados corretamente).*

### 2. Compilação Online (Overleaf)

1. Crie um novo projeto em branco no [Overleaf](https://www.overleaf.com/).

2. Faça o upload do arquivo `Analisador Léxico.tex` (e eventuais imagens/recursos, caso adicione).

3. Clique em **Recompile** para visualizar e baixar o PDF atualizado.

## 🧹 Dica de Boas Práticas (`.gitignore`)

Para manter o repositório mais limpo em futuras atualizações, recomenda-se adicionar um arquivo `.gitignore` para evitar o versionamento de arquivos temporários de compilação e bloqueio, tais como:

```
*.aux
*.log
*.nav
*.out
*.snm
*.synctex.gz
*.toc
*.vrb
*.lock

```

## 📄 Licença

Este projeto está sob a licença especificada no arquivo [LICENSE](LICENSE).