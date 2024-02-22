# **HTML**

## **Breve história**

A sigla HTML significa HyperText Markup Language. Em português, linguagem de marcação de hipertexto.

É possível colocar em uma página HTML texto, imagens, sons e vídeos, além dos links que permitem que façamos uma leitura não linear.

Pessoas visionárias propuseram, por meio de modelos teóricos, ideias que inspiraram o desenvolvimento do HTML.

Vannevar Bush foi uma dessas pessoas, com o Memex, em 1945.  
Tratava-se de uma máquina que tornava possível fazer _links_ entre documentos.

Posteriormente, em 1960, Theodor (Ted) Nelson criou o termo hipertexto/hipermídia.  
Apresentou o projeto Xanadu, cuja ideia era disponibilizar textos paralelos.
Com essa proposta, é possível visualizar documentos e suas conexões precisas, utilizando duas janelas.

Tim Bernard Lee, em 1990, desenvolveu o HTML, com o objetivo de trocar informações entre pesquisadores.  
Ele não tinha ideia da dimensão que tomaria a sua criação.

HTML teve como base o SGML (_Standard Generalized Mark-up Language_), um método acordado internacionalmente para marcar texto.

O uso de elementos como <title> e </title> foi retirado diretamente do SGML, e o mesmo ocorreu com elementos como parágrafos, títulos, listas e outros.

O elemento para _link_ e o formato www.name.name para endereços de máquina na web foram inventados por Tim.

## **HTML**

HTML é uma linguagem de marcação que o desenvolvedor usa para se comunicar com o _browser_ (navegador), que por sua vez interpreta a marcação em algo que o usuário entenda, como uma página web.

Como qualquer linguagem, HTML também tem suas regras de sintaxe e escrita.

O produto de uma marcação HTML é um arquivo de texto que deve ser gravado com a extensão .html, por exemplo `nome_arquivo.html`.

## **Estrutura mínima de uma página HTML**

No arquivo `.html` é possível digitar `!` e apertar`enter` então surgirá essa [estrutura]("./estruturaInicial.html").

## **Tags**

Para escrever em HTML, precisamos utilizar tags (etiquetas).

Iniciamos com uma tag de abertura e no fim uma tag de fechamento.

A _tag_ de fechamento é igual à _tag_ de abertura com um sinal de barra `/` na frente.

### **Títulos**

As tags de títulos são definidas de `<h1>` a `<h6>`, e são empregadas para definir os cabeçalhos em HTML.

Eles são do tipo nível de bloco.

`<h1>` define o título mais relevante.

`<h6>` define o título menos importante.

Utilize apenas um `<h1>` por página.

### **Parágrafos**

A tag `<p>` define um parágrafo. Os navegadores adicionam uma linha após um parágrafo `</p>`.

### **Quebra de linha**

A tag `<br>` força uma quebra de linha. Não possui tag de fechamento.

### **Linha horizontal**

A tag `<hr>` insere uma linha horizontal. Não possui tag de fechamento.

### **Listas ordenadas**

São envoltas por `<ol><li>Item 4</li></ol>`

### **Listas não ordenadas**

São envoltas por `<ul><li>Item 4</li></ul>`

### **Links**

Para inserir ligações (hiperlinks, links), utilizamos a tag `<a>` (anchor elemento - elemento âncora), elemento do tipo inline.

O atributo `href` (hyperlink reference - referência de hiperlink)é necessário e indica o destino do link.

**Optativo:** target alvo (onde irá abrir o _link_).
Valores:

`_self` - Predefinição. Abre o documento na mesma janela/guia em que foi clicado

`_blank` - Abre o documento em uma nova janela ou guia

`_parent` - Abre o documento no quadro pai

`_top` - Abre o documento em todo o corpo da janela

Ex.:  

    <a href="https://www.google.com" target="_blank">Visite o Google</a>

### **Imagens**

Para inserir imagens, utilizamos o elemento `<img>`.

Esse é um elemento _inline_ e não necessita da _tag_ de fechamento.

Requer dois atributos: `src` (caminho da imagem) e `alt` (texto alternativo, se a imagem por algum motivo não puder ser exibida).

Outros atributos que podem ser utilizados são `width` (largura) e `height` (altura).

### **Tabelas**

Utilizamos a tag `<table>` para criar tabelas, juntamente com os elementos:  
`<tr>` → linhas  
`<th>` → cabeçalhos (nomes de colunas e linhas, fica em negrito)
`<td>` → células de dados

**Mesclagem de tabelas**  

`colspan` → mescla colunas  
`rowspan` → mescla linhas

**Acessibilidade em tabelas**  

Utilizado por leitores de tela  
`caption` → título da tabela  
`summary` → descrever o objetivo da tabela  
`<thead>` → cabeçalhos da tabela  
`<tfoot>` → rodapé da tabela  
`<tbody>` corpo da tabela

### **Formulários**

Utiliza-se a tag `<form>` para criar um formulário.

O objetivo de utilizar formulários é receber entradas (informações) dos usuários.

Esses dados podem ser enviados para um banco de dados, ou até mesmo recebidos no _e-mail_.

Os campos devem estar entre as tags `<form> e </form>`  
`size="50"` dimensão do campo no `input`
`maxlength="50"` número máximo de caracteres digitados no `input`

---

A aplicação prática das tags estão no [exemplo.html](./exemplo.html).

## **Elementos estruturais semânticos**

Os elementos estruturais semânticos em HTML são tags que fornecem significado e estrutura ao conteúdo de uma página da web. Eles ajudam os navegadores e mecanismos de busca a entender a hierarquia e a importância do conteúdo, o que é fundamental para a acessibilidade e a indexação correta do conteúdo. 

``<header>``:  
Define o cabeçalho da página ou de uma seção específica.

    <header>
        <!-- Conteúdo do cabeçalho -->
    </header>

``<nav>``  
Utilizado para agrupar links de navegação.

    <nav>
        <!-- Links de navegação -->
    </nav>

``<main>``  
Define o conteúdo principal da página. Deve ser usado apenas uma vez em cada página.

    <main>
        <!-- Conteúdo principal -->
    </main>

``<section>``  
Representa uma seção genérica em um documento.

    <section>
        <!-- Conteúdo da seção -->
    </section>

``<article>``  
Define um conteúdo independente e autossuficiente, como uma postagem de blog ou um artigo de jornal.

    <article>
        <!-- Conteúdo do artigo -->
    </article>

``<aside>``  
Utilizado para conteúdo relacionado, como barras laterais ou informações adicionais.

    <aside>
        <!-- Conteúdo relacionado -->
    </aside>

``<footer>``  
Define o rodapé da página ou de uma seção específica.

    <footer>
        <!-- Conteúdo do rodapé -->
    </footer>

Estes são apenas alguns exemplos dos elementos semânticos em HTML. Utilizar essas tags apropriadamente ajuda não apenas na organização e na estruturação do seu código, mas também na acessibilidade e na otimização para mecanismos de busca.

``<figure>``  
Utilizado para agrupar qualquer conteúdo relacionado, como imagens e legendas.


    <figure>
        <img src="imagem.jpg" alt="Descrição da imagem">
        <figcaption>Legenda da imagem</figcaption>
    </figure>

``<figcaption>``  
Define a legenda para elementos ``<figure>``.

    <figure>
        <img src="imagem.jpg" alt="Descrição da imagem">
        <figcaption>Legenda da imagem</figcaption>
    </figure>

``<details>``  
Define um widget de controle que permite ao usuário revelar ou ocultar informações adicionais.

    <details>
        <summary>Título do detalhe</summary>
        <!-- Conteúdo adicional -->
    </details>

``<summary>``  
Define o título de um elemento ``<details>``.

    <details>
        <summary>Título do detalhe</summary>
        <!-- Conteúdo adicional -->
    </details>

``<time>``  
Define um período de tempo ou uma data específica.

    <time datetime="2024-02-22">22 de fevereiro de 2024</time>

``<mark>``  
Utilizado para destacar parte do texto.

    <p>Este é um <mark>texto destacado</mark> em um parágrafo.</p>

``<abbr>``  
Define uma abreviação ou um acrônimo, com a opção de fornecer uma descrição completa.

    <p><abbr title="Cascading Style Sheets">CSS</abbr> é usado para estilizar páginas da web.</p>

## **Posicionamento com span**

É uma técnica comum para aplicar estilos a parte do texto ou conteúdo em linha, sem quebrar o fluxo normal do texto.  

O elemento ``<span>`` é um elemento de conteúdo em linha genérico que não possui significado semântico próprio, mas pode ser usado em conjunto com classes ou IDs para aplicar estilos ou manipulações de JavaScript de forma seletiva.  

O uso de ``<span>`` para posicionamento e estilização permite uma grande flexibilidade ao trabalhar com conteúdo em linha no HTML, especialmente quando você precisa aplicar estilos ou manipulações específicas a partes específicas do texto.   

Certifique-se de usar ``<span>`` de forma semântica e significativa, evitando o uso excessivo quando elementos mais semânticos, como ``<strong>`` ou ``<em>``, forem mais apropriados.

### **Aplicando estilos a uma parte do texto**

Pode-se usar ``<span>`` para envolver uma parte específica do texto e aplicar estilos apenas a essa parte.

    <p>Este é um parágrafo com <span style="font-weight: bold;">texto em negrito</span>.</p>

Neste exemplo, o texto "texto em negrito" será exibido em negrito, enquanto o restante do parágrafo permanecerá em estilo padrão.

### **Aplicando classes para estilização**

Em vez de estilos embutidos, é recomendado aplicar estilos por meio de classes CSS para separar a estrutura do conteúdo da sua apresentação.

    html
    <p>Este é um parágrafo com <span class="destaque">texto destacado</span>.</p>

    css
    .destaque {
        color: red;
        font-size: 18px;
    }

Neste exemplo, a classe ``.destaque`` é aplicada ao ``<span>`` para definir a cor do texto como vermelho e aumentar seu tamanho para 18 pixels.

### **Manipulação de texto com JavaScript**

Também é possível usar ``<span>`` em conjunto com JavaScript para manipular dinamicamente partes do texto.

    html
    <p>Selecione o idioma: <span id="language">Inglês</span></p>
    <button onclick="changeLanguage()">Mudar idioma</button>

    <script>
        function changeLanguage() {
            var span = document.getElementById('language');
            span.textContent = 'Português';
        }
    </script>

Neste exemplo, ao clicar no botão, o texto dentro do ``<span>`` com o ID "language" será alterado de "Inglês" para "Português".




