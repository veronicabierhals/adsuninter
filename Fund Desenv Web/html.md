# **HTML**

## **Breve história**
A sigla HTML significa HyperText Markup Language. Em português, linguagem de marcação de hipertexto.  

É possível colocar em uma página HTML texto, imagens, sons e vídeos, além dos links que permitem que façamos uma leitura não linear.  

Pessoas visionárias propuseram, por meio de modelos teóricos, ideias que inspiraram o desenvolvimento do HTML.

Vannevar Bush foi uma dessas pessoas, com o Memex, em 1945.  
Tratava-se de uma máquina que tornava possível fazer *links* entre documentos.  

Posteriormente, em 1960, Theodor (Ted) Nelson criou o termo hipertexto/hipermídia.  
Apresentou o projeto Xanadu, cuja ideia era disponibilizar textos paralelos.
Com essa proposta, é possível visualizar documentos e suas conexões precisas, utilizando duas janelas.  

Tim Bernard Lee, em 1990, desenvolveu o HTML, com o objetivo de trocar informações entre pesquisadores.  
Ele não tinha ideia da dimensão que tomaria a sua criação.

HTML teve como base o SGML (*Standard Generalized Mark-up Language*), um método acordado internacionalmente para marcar texto.  

O uso de elementos como <title> e </title> foi retirado diretamente do SGML, e o mesmo ocorreu com elementos como parágrafos, títulos, listas e outros.

O elemento para *link* e o formato www.name.name para endereços de máquina na web foram inventados por Tim.  

## **HTML**

HTML é uma linguagem de marcação que o desenvolvedor usa para se comunicar com o *browser* (navegador), que por sua vez interpreta a marcação em algo que o usuário entenda, como uma página web.  

Como qualquer linguagem, HTML também tem suas regras de sintaxe e escrita.

O produto de uma marcação HTML é um arquivo de texto que deve ser gravado com a extensão .html, por exemplo ``nome_arquivo.html``.

## **Estrutura mínima de uma página HTML**

No arquivo ``.html`` é possível digitar ``!`` e apertar``enter`` então surgirá essa [estrutura]("./estruturaInicial.html").

## **Tags**

Para escrever em HTML, precisamos utilizar tags (etiquetas).  

Iniciamos com uma tag de abertura e no fim uma tag de fechamento.  

A *tag* de fechamento é igual à *tag* de abertura com um sinal de barra ``/`` na frente.  

### **Títulos**

As tags de títulos são definidas de ``<h1>`` a ``<h6>``, e são empregadas para definir os cabeçalhos em HTML.  

Eles são do tipo nível de bloco.  

``<h1>`` define o título mais relevante.

``<h6>`` define o título menos importante.

Utilize apenas um ``<h1>`` por página.

### **Parágrafos**

A tag ``<p>`` define um parágrafo. Os navegadores adicionam uma linha após um parágrafo ``</p>``.

### **Quebra de linha**

A tag ``<br>`` força uma quebra de linha. Não possui tag de fechamento.

### **Linha horizontal**

A tag ``<hr>`` insere uma linha horizontal. Não possui tag de fechamento.

### **Listas ordenadas**

São envoltas por ``<ol><li>Item 4</li></ol>``

### **Listas não ordenadas**

São envoltas por ``<ul><li>Item 4</li></ul>``

### **Links**

Para inserir ligações (hiperlinks, links), utilizamos a tag ``<a>`` (anchor elemento - elemento âncora), elemento do tipo inline.  

O atributo ``href`` (hyperlink reference - referência de hiperlink)é  necessário e indica o destino do link.

**Optativo:** target alvo (onde irá abrir o *link*).
Valores:

``_self`` - Predefinição. Abre o documento na mesma janela/guia em que foi clicado

``_blank`` - Abre o documento em uma nova janela ou guia

``_parent`` - Abre o documento no quadro pai

``_top`` - Abre o documento em todo o corpo da janela

Ex.:  
``<a href="https://www.google.com" target="_blank">Visite o Google</a>``

### **Imagens**

Para inserir imagens, utilizamos o elemento ``<img>``.  

Esse é um elemento *inline* e não necessita da *tag* de fechamento.  

Requer dois atributos: ``src`` (caminho da imagem) e ``alt`` (texto alternativo, se a imagem por algum motivo não puder ser exibida).  

Outros atributos que podem ser utilizados são ``width`` (largura) e ``height`` (altura).

### **Tabelas**

Utilizamos a tag ``<table>`` para tabelas, juntamente com os elementos ``<tr>``, ``<th>`` e ``<td>``.

### **Formulários**

Utiliza-se a tag ``<form>`` para criar um formulário.

O objetivo de utilizar formulários é receber entradas (informações) dos usuários.  

Esses dados podem ser enviados para um banco de dados, ou até mesmo recebidos no *e-mail*.  

Os campos devem estar entre as tags ``<form> e </form>``

___
A aplicação prática das tags estão no [exemplo.html](./exemplo.html).
