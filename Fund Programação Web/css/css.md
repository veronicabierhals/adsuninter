# Cascading Style Sheets (CSS)

Em português, Folhas de Estilo em Cascata.  
É um mecanismo simples para adicionar estilos.

**Sintaxe**  
![sintaxe CSS](./img/sintaxeCSS.png)

## **Seletores**

### **Seletores ID**

Um id é um seletor que deve ser único em todo o documento HTML. Cada elemento pode ter apenas um id.

Os ids são usados quando você deseja estilizar um elemento específico e não pretende reutilizar o estilo.

Para selecionar um elemento por id no CSS, use uma hashtag `(#)` seguida pelo nome do id.

Exemplo:

    #cabecalho { font-size: 24px; }

### **Seletores class**

Uma classe é um seletor que pode ser aplicado a vários elementos em um documento HTML.

Você pode usar a mesma classe em múltiplos elementos para aplicar estilos semelhantes a eles.

Para selecionar um elemento por classe no CSS, use um ponto `(.)` seguido pelo nome da classe.

Exemplo:

    .botao-vermelho { color: red; }

### **Seletores universal**

O seletor universal `(*)` seleciona todos os elementos em um documento HTML.

É útil quando você deseja aplicar um estilo global a todos os elementos do documento.

No entanto, deve ser usado com cautela, pois pode afetar o desempenho do seu CSS, especialmente em documentos grandes.

Exemplo:

    * { margin: 0; padding: 0; }

### **Agrupamento de seletores**

O agrupamento de seletores permite aplicar o mesmo conjunto de estilos a múltiplos seletores.

Isso pode reduzir a repetição de código e tornar seu CSS mais conciso e legível.

Você pode agrupar seletores separando-os por vírgulas (,).

Exemplo:

    h1, h2, h3 { font-family: Arial, sans-serif; }

## **Como aplicar o CSS**

### **Externo**

O CSS externo é definido em um arquivo separado com extensão `.css` e, em seguida, é vinculado ao documento HTML usando a tag `<link>` no elemento ´`<head>``.

    <link rel="stylesheet" type="text/css" href="styles.css">

### **Interno (incorporado)**

O CSS interno é definido dentro da seção `<style>` no elemento `<head>` do documento HTML e afeta apenas o documento onde está definido.

    <style>
        /* Estilos internos */
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: blue;
        }
    </style>

### **Inline**

O CSS inline é aplicado diretamente a um elemento HTML usando o atributo `style`.

`<h1 style="color: blue;">Este é um cabeçalho</h1>`

## **Hierarquia do CSS**

### **1. Importância:**

A importância é uma propriedade que pode ser atribuída a uma regra de estilo usando o valor `!important`.

Uma regra com `!important` sempre prevalecerá sobre outras regras, independentemente de sua especificidade ou ordem de declaração.

No entanto, o uso excessivo de !important pode dificultar a manutenção do código, então deve ser usado com moderação.  
<br>

### **2. Especificidade:**

A especificidade é a característica que determina qual regra CSS será aplicada a um elemento quando várias regras se aplicam a ele.

Cada seletor tem uma pontuação de especificidade atribuída, que é calculada com base nos tipos de seletores usados (id, classe, elemento).

Quanto mais específico for o seletor, maior será sua pontuação de especificidade.

Se houver um empate na especificidade, a regra que aparece por último no código prevalecerá.  
<br>

### **3. Ordem de Declaração:**

A ordem em que as regras CSS são declaradas também é importante.

Se duas regras têm a mesma especificidade, a última regra declarada prevalece.

Portanto, a ordem em que você define suas regras CSS no arquivo é crucial.

## **Comentários**

Os comentários são usados para explicar o código e podem ajudar você a editar o código-fonte posteriormente.

Eles não serão exibidos pelos navegadores.

Um comentário CSS é colocado dentro do `<style>` no arquivo HTML.

    /* comentário aqui */

## **Tipos de Cores**

Podem ser aplicadas em textos, fundos e bordas.

### **Por Nome:**

Usando uma cor pré-definida, como "red", "blue", "green", etc.

Exemplo:

    color: red;

### **Hexadecimal:**

Você pode especificar uma cor usando seu valor hexadecimal. Isso envolve uma combinação de seis caracteres, que representam os componentes de cor vermelha, verde e azul (RGB).

Exemplo:

    color: #ff0000;

(vermelho)

### **RGB (Red, Green, Blue):**

Usar os valores de intensidade de vermelho, verde e azul em uma escala de 0 a 255.

Exemplo:

    color: rgb(255, 0, 0);

(vermelho)

### **RGBA (Red, Green, Blue, Alpha):**

Semelhante ao RGB, mas com um quarto valor para a transparência (alfa), que varia de 0 (totalmente transparente) a 1 (totalmente opaco).

Exemplo:

    color: rgba(255, 0, 0, 0.5);

(vermelho com 50% de transparência)

### **HSL (Hue, Saturation, Lightness):**

Definir uma cor usando matiz (um ângulo de 0 a 360 graus), saturação (porcentagem) e luminosidade (porcentagem).

Exemplo:

    color: hsl(0, 100%, 50%);

### **HSLA (Hue, Saturation, Lightness, Alpha):**

Semelhante ao HSL, mas com um quarto valor para a transparência (alfa), que varia de 0 (totalmente transparente) a 1 (totalmente opaco).

Exemplo:

    color: hsla(0, 100%, 50%, 0.5);

(vermelho com 50% de transparência)

## **Como aplicar as cores**

### **Texto (color):**

Você pode definir a cor do texto usando a propriedade `color`.

Exemplo:

    color: blue;

### **Fundo (background-color):**

Você pode definir a cor de fundo de um elemento usando a propriedade `background-color`.

Exemplo:

    background-color: #ff0000;

(vermelho)

### **Bordas (border-color):**

Você pode definir a cor das bordas de um elemento usando a propriedade `border-color`.

Exemplo:

    border-color: rgb(0, 255, 0);

(verde)

### **Gradientes (background-image):**

Além de cores sólidas, você pode aplicar gradientes usando a propriedade `background-image`.

Exemplo:

    background-image: linear-gradient(to right, red, yellow);

### **Sombra (box-shadow, text-shadow):**

Você pode definir a cor da sombra de um elemento usando as propriedades `box-shadow` (para sombras de caixa) e `text-shadow` (para sombras de texto).

Exemplo:

    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);

(Sombra preta com 50% de transparência)

### **Elementos SVG:**

Em elementos SVG, você pode definir cores diretamente ou usando a propriedade `fill` para preenchimento e `stroke` para contorno.

Exemplo:

    fill: #00ff00;` (verde)
    stroke: blue;

### **Pseudo-elementos (before, after):**

Você pode aplicar cores a pseudo-elementos usando as mesmas propriedades que aplicaria a elementos regulares.

Exemplo:

    .elemento::before {background-color: rgba(255, 0, 0, 0.5)}

(vermelho com 50% de transparência)

## **Margens**

### **Propriedade de Margem Simples:**

A propriedade margin pode ser usada para definir a margem em todas as quatro direções simultaneamente.

Sintaxe:

    margin: 10px;

Margem de 10 pixels em todas as direções

### **Propriedades de Margem Individual:**

Você também pode definir a margem para cada direção separadamente usando as propriedades margin-top, margin-right, margin-bottom e margin-left.

Sintaxe:  
`margin-top: 10px;` margem superior de 10 pixels  
`margin-right: 20px;` margem direita de 20 pixels  
`margin-bottom: 15px;`margem inferior de 15 pixels  
`margin-left: 5px;` margem esquerda de 5 pixels

### **Margem Negativa:**

Você também pode usar valores negativos para criar margens negativas, que podem ser úteis para sobreposição de elementos ou layout avançado.

Sintaxe:

    margin: -10px;

margem de -10 pixels em todas as direções

### **Margem Automática:**

A palavra-chave auto pode ser usada para definir margens automáticas, o que permite que um elemento seja centralizado horizontalmente dentro de seu contêiner.

Sintaxe:

    margin: auto;

centraliza horizontalmente o elemento dentro do contêiner

### **Múltiplas Margens:**

Você pode definir margens diferentes para cada lado separadamente, em uma única declaração.

Sintaxe:

    margin: 10px 20px 15px 5px;

margem superior, direita, inferior e esquerda, respectivamente

## **Bordas**

### **Borda Simples:**

A propriedade `border` define uma borda em todas as quatro direções simultaneamente.

Sintaxe:

    border: 1px solid black;

Borda de 1 pixel de largura, sólida e preta

### **Bordas Individuais:**

Você também pode definir bordas separadamente para cada lado usando as propriedades `border-top`, `border-right`, `border-bottom` e `border-left`.

Sintaxe:

    border-top: 2px dashed red;

Borda superior de 2 pixels de largura, tracejada e vermelha

### **Estilo da Borda:**

O estilo da borda pode ser especificado usando palavras-chave como `solid` (sólido), `dashed` (tracejado), `dotted` (pontilhado), entre outros.

Sintaxe:

    border: 2px dashed blue;

Borda de 2 pixels de largura, tracejada e azul

### **Largura da Borda:**

Você pode definir a largura da borda em pixels (px), emems (em), rem, ou como uma porcentagem (%) da largura do elemento.

Sintaxe:

    border: 3px solid green;

Borda de 3 pixels de largura, sólida e verde

### **Cor da Borda:**

A cor da borda pode ser especificada usando nomes de cores, códigos hexadecimais, RGB, RGBA ou HSL.

Sintaxe:

    border: 1px solid #ff0000;

Borda de 1 pixel de largura, sólida e vermelha

### **Borda Arredondada:**

Você pode criar bordas arredondadas usando as propriedades `border-radius` para especificar o raio dos cantos.

Sintaxe:

    border-radius: 5px;

Raio de 5 pixels para todos os cantos

## **Padding**

O preenchimento (padding) em CSS é usado para controlar o espaço entre o conteúdo de um elemento e suas bordas.  
Ele cria um espaço interno dentro do elemento.

### **Padding Simples:**

A propriedade `padding` define o preenchimento em todas as quatro direções simultaneamente.

Sintaxe:

    padding: 10px;

Preenchimento de 10 pixels em todas as direções

### **Preenchimento Individual:**

Você também pode definir o preenchimento separadamente para cada direção usando as propriedades `padding-top`, `padding-right`, `padding-bottom` e `padding-left`.

Sintaxe:  
`padding-top: 5px;` Preenchimento superior de 5 pixels  
`padding-right: 15px;` Preenchimento direito de 15 pixels  
`padding-bottom: 10px;`Preenchimento inferior de 10 pixels  
`padding-left: 20px;` Preenchimento esquerdo de 20 pixels

### **Preenchimento Múltiplo:**

Você pode definir diferentes valores de preenchimento para cada lado em uma única declaração.

Sintaxe:

    padding: 10px 20px 15px 5px;

Preenchimento superior, direito, inferior e esquerdo, respectivamente

### **Preenchimento com Porcentagem:**

Além de valores fixos, você também pode especificar o preenchimento como uma porcentagem da largura do elemento pai.

Sintaxe:

    padding: 5% 10% 7% 3%;

Preenchimento superior, direito, inferior e esquerdo, respectivamente, em porcentagem

### **Valores Negativos de Preenchimento:**

Assim como com as margens, você também pode usar valores negativos de preenchimento para ajustar o layout e a sobreposição de elementos.

Sintaxe:

    padding: -10px;

Preenchimento de -10 pixels em todas as direções

## **Height (altura) e Width (largura )**

`height` e `width` usadas para definir a altura e a largura de um elemento.

`max-width` é usada para definir a largura máxima de um elemento.

### **Valores**

`auto` - este é o padrão. O navegador calcula a altura e a largura;  
`length` - define a altura/largura em px, cm e etc.;  
`%` - define a altura/largura em porcentagem do bloco que contém.

## **Formatação de texto**

A formatação de texto em CSS permite que você personalize a aparência do texto em seus elementos HTML.  
Existem várias propriedades que você pode usar para controlar o tamanho, a cor, o estilo da fonte e muito mais.  
Aqui estão algumas das principais propriedades de formatação de texto e suas sintaxes:

### **Cor do Texto (color)**:

A propriedade `color` define a cor do texto.

Sintaxe:

    color: blue;

Define a cor do texto como azul

### **Tamanho da Fonte (font-size):**

A propriedade `font-size` define o tamanho da fonte do texto.

Sintaxe:

    font-size: 16px;

Define o tamanho da fonte como 16 pixels

## **Estilo da Fonte (font-style):**

A propriedade `font-style` define o estilo da fonte do texto, como normal, itálico ou obliquo.

Sintaxe:

    font-style: italic;

Define o estilo da fonte como itálico

### **Peso da Fonte (font-weight):**

A propriedade `font-weight` define a espessura da fonte, como normal, negrito ou mais leve.

Sintaxe:

    font-weight: bold;

Define o peso da fonte como negrito

### **Família da Fonte (font-family):**

A propriedade `font-family` define a família da fonte a ser usada, como Arial, Times New Roman, etc.

Sintaxe:

    font-family: Arial, sans-serif;

Define a família da fonte como Arial, com fallback para fontes sans-serif

### **Decoração do Texto (text-decoration):**

A propriedade text-decoration define a decoração do texto, como sublinhado, tachado, etc.

Sintaxe:

    text-decoration: underline;

Define o texto como sublinhado

### **Alinhamento do Texto (text-align):**

A propriedade `text-align` define o alinhamento horizontal do texto, como esquerda, direita, centralizado ou justificado.

Sintaxe:

    text-align: center;

Alinha o texto ao centro

## **Box model**

![Box Model](./img/boxModel.png)

O modelo de caixa (box model) é uma parte fundamental do layout em CSS, que descreve como os elementos HTML são renderizados no navegador.  
Ele consiste em quatro partes principais:

### **Conteúdo (Content):**

O conteúdo é a parte interna do elemento HTML onde o texto e outros elementos são exibidos.  
Não há uma propriedade específica para definir o conteúdo diretamente.  
O tamanho do conteúdo é determinado automaticamente com base no tamanho do elemento e seu conteúdo.

### **Preenchimento (Padding):**

O preenchimento é a área entre o conteúdo e a borda. Ele define o espaço entre o conteúdo do elemento e sua borda.

Sintaxe:

    padding: 10px;

### **Borda (Border):**

A borda é uma linha que circunda o elemento, separando o conteúdo e o preenchimento de sua margem.

Sintaxe:

    border: largura estilo cor;

### **Margem (Margin):**

A margem é a área externa da borda, que define o espaço entre o elemento e outros elementos circundantes.

Sintaxe:

    margin: valor;

## **Box-sizing**

A propriedade `box-sizing` é utilizada para definir como o navegador deve calcular a largura total e a altura de um elemento, incluindo seu conteúdo, preenchimento (padding) e borda (border).

A propriedade `box-sizing` é especialmente útil em layouts responsivos e quando você precisa controlar precisamente o tamanho e o posicionamento dos elementos em sua página da web.

Existem dois valores principais para a propriedade box-sizing:

### **Content-Box:**

Este é o valor padrão.
Com `box-sizing: content-box;`, a largura e a altura especificadas em CSS representam apenas o conteúdo do elemento, excluindo o preenchimento e a borda.  
Isso significa que o preenchimento e a borda são adicionados ao tamanho total do elemento.

### **Border-Box:**

Com `box-sizing: border-box;`, a largura e a altura especificadas em CSS incluem o conteúdo, o preenchimento e a borda do elemento.  
O tamanho total do elemento é calculado a partir da borda externa, em vez do conteúdo interno.

A principal vantagem de usar `box-sizing: border-box;` é que você pode definir a largura de um elemento com preenchimento e borda e saber que o tamanho total do elemento permanecerá consistente, independentemente de alterações no conteúdo interno ou na largura da borda.

## **Formatação de colunas**

### **Float e Clear**

As propriedades `float` e `clear` são frequentemente usadas em conjunto para criar layouts de página complexos, especialmente em designs antigos que utilizam um método chamado "float layout".

### **Float:**

A propriedade `float` é usada para especificar que um elemento deve ser retirado do fluxo normal e colocado ao lado do elemento anterior, à esquerda ou à direita, até que não haja espaço disponível ou até que outro elemento flutuante seja encontrado.

**Quando usar:** O uso de float é útil para layouts mais antigos ou para oferecer suporte a navegadores mais antigos que não suportam as técnicas mais modernas, como flex ou grid.

**Vantagens:** É amplamente suportado em navegadores mais antigos, relativamente simples de implementar.

**Desvantagens:** Pode causar problemas de layout quando mal utilizado, especialmente em layouts responsivos.

Sintaxe:

    float: none | left | right;

none: O elemento não flutua e é exibido no fluxo normal.  
left: O elemento flutua para a esquerda.  
right: O elemento flutua para a direita.

### **Clear:**

A propriedade `clear` é usada para especificar em qual lado um elemento não deve flutuar.  
Isso é útil quando você deseja que um elemento não flutue ao lado de um elemento flutuante anterior.

Sintaxe:

    clear: none | left | right | both;

none: Não há restrição em relação a flutuação.  
left: O elemento não flutua ao lado do elemento flutuante à esquerda.  
right: O elemento não flutua ao lado do elemento flutuante à direita.  
both: O elemento não flutua ao lado de nenhum elemento flutuante.

Exemplo:

    .clearfix::after {
        content: "";
        display: table;
        clear: both;
    }

Neste exemplo, a classe .clearfix é aplicada ao contêiner pai de elementos flutuantes para garantir que ele envolva corretamente todos os elementos flutuantes dentro dele, impedindo que ele flutue ao lado deles.

É importante notar que o uso excessivo de float pode levar a problemas de layout, especialmente em designs responsivos.  
Alternativas modernas, como `flexbox` e `grid layout`, geralmente são preferíveis para criar layouts mais flexíveis e robustos.

### **display: inline-block;:**

Permite que os elementos se comportem como blocos, mas mantenham a capacidade de alinhamento horizontal.

**Quando usar:** É útil quando você deseja que os elementos se comportem como blocos, mas mantenham a capacidade de alinhamento horizontal e a capacidade de ter elementos em linha.

**Vantagens:** Oferece a capacidade de alinhar elementos horizontalmente, útil para criar layouts de grade simples.

**Desvantagens:** Pode ser complicado de alinhar verticalmente e pode apresentar espaços em branco indesejados entre os elementos.

Exemplo:

css
.column {
width: 30%; /_ Largura da coluna _/
display: inline-block;
margin-right: 2%; /_ Margem direita para criar espaçamento entre as colunas _/
vertical-align: top; /_ Alinhamento vertical ao topo _/
}

### **display: grid;:**

Maneira mais moderna de criar layouts de coluna e oferece mais controle sobre a disposição das colunas.

**Quando usar:** É ideal para layouts complexos que requerem controle preciso sobre a disposição de elementos, como layouts de grade ou layouts responsivos.

**Vantagens:** Oferece controle granular sobre a disposição de elementos, facilita a criação de layouts responsivos e suporta alinhamento vertical e horizontal.

**Desvantagens:** Pode ser mais complicado de entender e implementar, especialmente para iniciantes em CSS.

Exemplo:

    css
    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* Três colunas com larguras iguais */
        gap: 10px; /* Espaçamento entre as colunas */
    }

### **display: flex;:**

Também é uma opção moderna e flexível para criar layouts de coluna.  

**Quando usar:** É ótimo para layouts simples de linha ou coluna, como barras de navegação ou seções de página.  

**Vantagens:** É fácil de entender e implementar, oferece controle flexível sobre a distribuição de espaço e suporta alinhamento vertical e horizontal.  

**Desvantagens:** Pode ser menos adequado para layouts complexos que requerem disposições bidimensionais.

Exemplo:

    css
    .container {
        display: flex;
    }

    .column {
        flex: 1; /* Ocupa espaço igualmente */
        margin-right: 10px; /* Margem direita para criar espaçamento entre as colunas */
    }

### **Sintaxe para Selecionar Colunas:**

Você pode selecionar colunas da mesma maneira que seleciona outros elementos HTML, usando classes, IDs ou seletores de elementos.

Exemplo:

css
.column {
/_ Estilos para todas as colunas com a classe .column _/
}

## **Elementos block e inline**

Os elementos de bloco e de linha são a base do modelo de caixa (box model) em CSS, e eles determinam como os elementos HTML são exibidos na página.  
Aqui está uma explicação de cada tipo de elemento e sua sintaxe:

### **Elementos de Bloco:**

Os elementos de bloco ocupam toda a largura disponível horizontalmente e começam em uma nova linha.

Eles podem conter outros elementos (incluindo elementos de bloco e de linha) e são frequentemente usados para estruturar o layout da página.

Exemplos de elementos de bloco comuns:  
`<div>`,` <p>`, `<h1>-<h6>`, `<ul>`, `<ol>`, `<li>`, `<header>`, `<footer>`, `<section>`, `<article>`, `<nav>`, `<main>`, `<aside>`, `<blockquote>`, entre outros.

Sintaxe:  
html

    <div>Conteúdo do elemento de bloco</div>

### **Elementos de Linha:**

Os elementos de linha são renderizados em linha, um após o outro, dentro do fluxo de conteúdo.  
Eles ocupam apenas a largura necessária para seu conteúdo e não iniciam uma nova linha.

Exemplos de elementos de linha comuns:  
`<span>`, `<a>`, `<strong>`, `<em>`, `<img>`, `<input>`, `<button>`, entre outros.

Sintaxe:  
html

    <span>Conteúdo do elemento de linha</span>

## **Display**

Você pode alterar o comportamento padrão de exibição de um elemento usando a propriedade `display` em CSS.  
Por exemplo, você pode tornar um elemento de bloco em um elemento de linha e vice-versa.

Alterando um Elemento para Bloco:

    display: block;

Alterando um Elemento para Linha:

    display: inline;

Além disso, existem propriedades como `display: inline-block;` que combinam características de elementos de bloco e de linha, permitindo que o elemento ocupe apenas o espaço necessário, mas ainda possa ter largura, altura e preenchimento especificados.  
Esses conceitos são fundamentais para criar layouts flexíveis e responsivos em CSS.

## **Position**

A propriedade position em CSS é usada para controlar o método de posicionamento de um elemento na página.  
Ela permite que você especifique como um elemento deve ser posicionado em relação ao seu contêiner pai ou ao documento como um todo.  
Aqui estão os principais valores da propriedade position e suas sintaxes:

### **Static:**

Este é o valor padrão.  
O elemento é posicionado de acordo com o fluxo normal do documento.

Sintaxe:

    position: static;

### **Relative:**

O elemento é posicionado em relação à sua posição normal no fluxo do documento, mas pode ser deslocado usando as propriedades top, right, bottom e left.

Sintaxe:

    position: relative;

### **Absolute:**

O elemento é posicionado em relação ao primeiro ancestral posicionado (ou seja, cuja propriedade position não seja static), se houver.  
Caso contrário, ele é posicionado em relação ao próprio documento.

Sintaxe:

    position: absolute;

### **Fixed:**

O elemento é posicionado em relação à janela de visualização, ou seja, ele permanecerá fixo mesmo quando a página for rolada.

Sintaxe:

    position: fixed;

### **Sticky:**

O elemento é posicionado em relação ao contêiner pai mais próximo com uma posição scrolling (rolagem).  
Ele age como relative até que seu contêiner pai seja rolado até um certo ponto, então se comporta como fixed.

Sintaxe:

    position: sticky;

Para além do valor position, você também pode ajustar a posição de um elemento usando as propriedades `top`, `right`, `bottom` e `left`.

Por exemplo:

    top: 10px;
    right: 20px;
    bottom: 30px;
    left: 40px;

Estas propriedades especificam a distância entre o elemento e o topo, direita, inferior e esquerda do seu contêiner pai, respectivamente. Lembre-se de que essas propriedades só têm efeito em elementos com uma propriedade position diferente de static.

## **Z-index**

A propriedade `z-index` é utilizada para controlar a ordem de empilhamento dos elementos em um layout, especificamente em situações onde os elementos se sobrepoem uns aos outros.  
Ela determina qual elemento será exibido acima dos outros quando houver sobreposição.

Sintaxe:

    z-index: valor;

O valor pode ser um número inteiro positivo, negativo ou auto.  
Quanto maior o valor, mais acima na pilha o elemento será empilhado.

Exemplo:

    z-index: 1;

Se dois elementos se sobrepõem e têm `z-index` definidos, o elemento com o maior valor de z-index será exibido acima do outro.

### **auto:**

O valor `auto` indica que o navegador deve calcular automaticamente a ordem de empilhamento do elemento com base na ordem de seus elementos ancestrais.

Sintaxe:

    z-index: auto;

Isso é útil quando você quer que o navegador decida a ordem de empilhamento dos elementos com base em sua hierarquia no DOM.

É importante observar que a propriedade `z-index` só tem efeito em elementos cuja propriedade `position` é definida como `absolute`, `relative` ou `fixed`.  
Além disso, ela afeta apenas elementos que estão no mesmo contexto de empilhamento, ou seja, que têm o mesmo ancestral que define uma pilha de contexto.

A propriedade `z-index` é uma ferramenta poderosa para controlar a sobreposição de elementos em um layout, permitindo que você crie designs complexos e dinâmicos.  
No entanto, é importante usá-la com cautela para evitar problemas de usabilidade e acessibilidade.

## **Árvore do documento**

A árvore do documento (DOM - Document Object Model) é uma representação hierárquica de todos os elementos HTML de uma página web.  
Essa estrutura de árvore permite que os navegadores interpretem e processem o conteúdo da página de forma eficiente, facilitando a manipulação e interação com os elementos por meio de JavaScript e CSS.  
A árvore do documento é essencial para entender a estrutura e a organização de uma página web.  
Ela permite que os desenvolvedores manipulem dinamicamente o conteúdo, a aparência e o comportamento dos elementos HTML, tornando possível criar experiências interativas e dinâmicas na web.

### **Elementos HTML:**

Os elementos HTML são os blocos de construção básicos de uma página web e formam os nós da árvore do documento.  
Cada elemento é representado por uma tag HTML, como `<div>`, `<p>`, `<h1>`, etc.

Exemplo:

    html
    <div>Conteúdo do elemento</div>

### **Atributos:**

Os atributos fornecem informações adicionais sobre os elementos HTML e são definidos dentro das tags.  
Eles geralmente consistem em um nome e um valor, separados por um sinal de igual (=).

Exemplo:

    html
    <img src="imagem.jpg" alt="Imagem de exemplo">

### **Elementos Filhos:**

Elementos que estão contidos dentro de outros elementos são considerados filhos desses elementos.  
Eles formam a estrutura hierárquica da árvore do documento.

Exemplo:

    html
    <div>
        <p>Este é um parágrafo dentro de um elemento div.</p>
    </div>

### **Navegação na Árvore:**

Você pode acessar os elementos da árvore do documento usando métodos e propriedades em JavaScript, como `document.getElementById()`, `document.querySelector()`, `parentNode`, `childNodes`, `children`, entre outros.

Exemplo:

    javascript

    // Acessando um elemento pelo ID
    var elemento = document.getElementById('meuElemento');

    // Acessando os filhos de um elemento
    var filhos = elemento.children;

### **Seletores de decendência**

Os seletores de descendência permitem que você selecione elementos com base em sua relação de descendência em relação a outros elementos.

Sintaxe:

    css
    elemento-pai elemento-filho {
        propriedade: valor;
    }

Exemplo:

    css
    nav ul {
        list-style-type: none;
    }

## **Combinadores em CSS**

Eles são usados para selecionar elementos com base em sua relação com outros elementos no documento.  
Esses combinadores oferecem maneiras de segmentar elementos com base em sua posição relativa dentro da estrutura do documento HTML.

### **Combinador filho (E > F):**

Este combinador seleciona elementos F que são filhos diretos de elementos E.

Sintaxe:

    E > F {
        propriedade: valor;
    }

Exemplo:

    nav > ul {
        list-style-type: none;
    }

Este exemplo selecionará apenas as listas não ordenadas (<ul>) que são filhas diretas de elementos <nav>.

### **Combinador irmão adjacente (E + F):**

Este combinador seleciona elementos F que são imediatamente precedidos por elementos E, e ambos compartilham o mesmo pai.

Sintaxe:

    E + F {
        propriedade: valor;
    }

Exemplo:

    h2 + p {
        font-weight: bold;
    }

Neste exemplo, o estilo será aplicado apenas aos parágrafos (`<p>`) que são irmãos adjacentes imediatamente após um título de segundo nível (`<h2>`).

### **Combinador irmão geral (E ~ F):**

Este combinador seleciona elementos F que são irmãos de elementos E, ou seja, ambos compartilham o mesmo pai, e F segue E.

Sintaxe:

    E ~ F {
        propriedade: valor;
    }

Exemplo:

    p ~ span {
        color: red;
    }

Neste exemplo, o estilo será aplicado a todos os elementos `<span>` que são irmãos de parágrafos `<p>` e vêm depois deles.

## **pseudo-classes estruturais em CSS**

São usados para selecionar elementos com base em sua posição dentro de um contêiner pai.  
Oferecem maneiras de selecionar e estilizar elementos com base em sua posição relativa dentro da estrutura do documento HTML.  
São especialmente úteis para aplicar estilos a listas, galerias de imagens e outros tipos de conteúdo estruturado.

### **:first-child:**

Seleciona o elemento que é o primeiro filho de seu contêiner pai.

Sintaxe:

    E:first-child {
        propriedade: valor;
    }

Exemplo:

    li:first-child {
        color: red;
    }

Neste exemplo, o estilo será aplicado apenas ao primeiro elemento `<li>` dentro de seu contêiner pai.

### **:last-child:**

Seleciona o elemento que é o último filho de seu contêiner pai.

Sintaxe:

    E:last-child {
        propriedade: valor;
    }

Exemplo:

    p:last-child {
        font-weight: bold;
    }

Neste exemplo, o estilo será aplicado apenas ao último elemento `<p>` dentro de seu contêiner pai.

### **:nth-child(n):**

Seleciona o enésimo filho de seu contêiner pai, onde n é um número inteiro ou uma expressão an+b.

Sintaxe:

    E:nth-child(n) {
        propriedade: valor;
    }

Exemplo:

    div:nth-child(2) {
        background-color: yellow;
    }

Neste exemplo, o estilo será aplicado apenas ao segundo elemento `<div>` dentro de seu contêiner pai.

### **:hover, :active e :focus:**

Selecionam elementos com base em interações do usuário, como passar o mouse (:hover), clicar (:active) ou focar (:focus).

Sintaxe:

css

    E:hover {
        /* Estilos para hover */
    }

    E:active {
        /* Estilos para clicar */
    }

    E:focus {
        /* Estilos para focar */
    }

Exemplo:

    css
    a:hover {
        color: red;
    }

### **:not():**

Seleciona elementos que não correspondem ao seletor dentro dos parênteses.

Sintaxe:

    css
    E:not(seletor) {
        /* Estilos para elementos que não correspondem ao seletor */
    }

Exemplo:

    css
    li:not(.destaque) {
        color: #333;
    }

## **Pseudo-elementos**

Recursos do CSS que permitem aplicar estilos a partes específicas de um elemento ou a estados específicos do elemento.

### **::before e ::after:**

Adicionam conteúdo antes e depois do conteúdo real do elemento, respectivamente.

Sintaxe:

    css
    E::before {
        content: "Texto ou conteúdo adicional";
        /* Estilos adicionais aqui */
    }

    E::after {
        content: "Texto ou conteúdo adicional";
        /* Estilos adicionais aqui */
    }

Exemplo:

    css
    p::before {
        content: ">> ";
        color: blue;
    }

### **::first-line e ::first-letter:**

Selecionam a primeira linha e a primeira letra do conteúdo do elemento, respectivamente.

Sintaxe:

    css
    E::first-line {
        /* Estilos para a primeira linha */
    }

    E::first-letter {
        /* Estilos para a primeira letra */
    }

Exemplo:

css
p::first-line {
font-weight: bold;
}

    p::first-letter {
        font-size: 150%;
    }

## **Barras de navegação**

As barras de navegação, comumente conhecidas como "navbars", são elementos importantes em muitos sites, pois fornecem uma maneira de navegar facilmente por diferentes seções ou páginas do site.  
Elas são geralmente implementadas usando listas não ordenadas `<ul>` e listas ordenadas `<ol>`, combinadas com estilos CSS para criar uma aparência visual atraente e funcional.  
Aqui está uma explicação sobre como criar uma barra de navegação básica usando HTML e CSS:

HTML:

    <nav>
        <ul>
            <li><a href="#">Página Inicial</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Serviços</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>

Neste exemplo, temos um elemento `<nav>` contendo uma lista não ordenada `<ul>`. Cada item da lista `<li>` representa um link de navegação, e os links são criados usando a tag `<a>` com o atributo href para especificar o destino do link.

CSS:

    nav {
        background-color: #333;
    }

    ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    li {
        display: inline;
    }

    a {
        display: block;
        padding: 10px 20px;
        text-decoration: none;
        color: #fff;
    }

    a:hover {
        background-color: #555;
    }

Neste exemplo de CSS, definimos o estilo para a barra de navegação e seus itens.  
Aqui está uma breve explicação das principais propriedades utilizadas:

`background-color:` Define a cor de fundo da barra de navegação.

`list-style-type`, `padding` e `margin`: Removem os estilos de lista padrão e o espaçamento entre os elementos da lista.

`display: inline`: Faz com que os itens da lista sejam exibidos em linha, lado a lado.

`display: block`: Faz com que os links ocupem todo o espaço disponível no contêiner `<li>`.

`padding`: Adiciona espaço interno aos links para melhorar a usabilidade.

`text-decoration`: Remove o sublinhado padrão dos links.

`color`: Define a cor do texto dos links.

`:hover`: Define os estilos de hover para os links, mudando a cor de fundo quando o mouse passa sobre eles.

### **Barra de navegação vertical:**

HTML:

    <nav class="vertical">
        <ul>
            <li><a href="#">Página Inicial</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Serviços</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>

CSS:

    nav.vertical {
        width: 200px;
        background-color: #333;
    }

    nav.vertical ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    nav.vertical li {
        text-align: center;
    }

    nav.vertical a {
        display: block;
        padding: 10px 0;
        text-decoration: none;
        color: #fff;
    }

    nav.vertical a:hover {
        background-color: #555;
    }

### **Barra de navegação horizontal:**

HTML:

    <nav class="horizontal">
        <ul>
            <li><a href="#">Página Inicial</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Serviços</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>

CSS:

    nav.horizontal {
        background-color: #333;
    }

    nav.horizontal ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    nav.horizontal li {
        display: inline-block;
    }

    nav.horizontal a {
        display: block;
        padding: 10px 20px;
        text-decoration: none;
        color: #fff;
    }

    nav.horizontal a:hover {
        background-color: #555;
    }

### **Menu suspenso:**

HTML:

    <nav class="dropdown">
        <ul>
            <li><a href="#">Página Inicial</a></li>
            <li><a href="#">Sobre</a></li>
            <li class="dropdown-menu">
                <a href="#">Serviços</a>
                <ul class="dropdown-content">
                    <li><a href="#">Serviço 1</a></li>
                    <li><a href="#">Serviço 2</a></li>
                    <li><a href="#">Serviço 3</a></li>
                </ul>
            </li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>

CSS:

    nav.dropdown ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }

    nav.dropdown li {
        display: inline-block;
        position: relative;
    }

    nav.dropdown a {
        display: block;
        padding: 10px 20px;
        text-decoration: none;
        color: #fff;
    }

    nav.dropdown a:hover {
        background-color: #555;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #333;
        min-width: 150px;
        z-index: 1;
    }

    .dropdown-content li {
        display: block;
    }

    .dropdown-menu:hover .dropdown-content {
        display: block;
    }

## **Botões**

Os botões são elementos fundamentais em interfaces de usuário web, usados para realizar ações como enviar formulários, navegar para outras páginas, executar scripts e muito mais.  
Eles podem ser criados usando a tag `<button>` ou `<input>` com o atributo `type="button"`.

### **Botão usando a tag `<button>`:**

HTML:

    <button>Enviar</button>

CSS:

    button {
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }

### **Botão usando a tag `<input>`:**

HTML:

    <input type="button" value="Enviar">

CSS:

    input[type="button"] {
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    input[type="button"]:hover {
        background-color: #0056b3;
    }

Esses exemplos criam botões estilizados com um fundo azul, texto branco e cantos arredondados.  
Quando o mouse passa sobre o botão, a cor de fundo muda para uma tonalidade mais escura de azul.  
Esses estilos são apenas exemplos básicos; você pode personalizá-los conforme necessário para atender aos requisitos de design do seu site.

Além disso, existem diferentes tipos de botões que podem ser criados, como botões de envio de formulário, botões de reinício, botões de ação, botões de alternância (toggle), entre outros.  
Você pode especificar o tipo de botão usando o atributo type com os valores "submit", "reset", "button", "checkbox", "radio", etc.  
Cada tipo tem seu comportamento específico, que pode ser estilizado com CSS conforme necessário.

### **Tipos de botão**

`submit`: Submete o formulário quando clicado.
`reset`: Limpa os campos de formulário quando clicado.
`button`: Comportamento padrão de um botão.
`checkbox`: Botão de seleção de caixa de seleção.
`radio`: Botão de seleção de rádio.

**Exemplo de Botão de Envio de Formulário:**

    html
    <form action="/submit">
    <button type="submit">Enviar</button>
    </form>

**Exemplo de Botão de Reinício de Formulário:**

    html
    <form action="/reset">
    <button type="reset">Limpar</button>
    </form>

**Exemplo de Botão de Ação:**

    html
    <button type="button" onclick="alert('Botão clicado!')">Clique aqui</button>

**Exemplo de Botão de Alternância (Toggle):**

    html
    <input type="checkbox" id="toggle">
    <label for="toggle">Alternar</label>

## **Variáveis**

Também conhecidas como "custom properties" (propriedades personalizadas), são recursos que permitem armazenar valores para reutilização em um documento CSS.  
Eles oferecem uma maneira de definir valores uma vez e usá-los em vários lugares em seu código CSS, facilitando a manutenção e a atualização.

### **Definindo Variáveis:**

As variáveis em CSS são definidas usando a sintaxe `--nome-da-variavel: valor;`.

Por exemplo:

    :root {
        --cor-primaria: #ff0000;
        --tamanho-fonte: 16px;
    }

Neste exemplo, `--cor-primaria` e `--tamanho-fonte` são variáveis CSS, e seus valores são #ff0000 (vermelho) e 16px, respectivamente.  
A declaração `:root` é usada para definir as variáveis globalmente para todo o documento.

### **Utilizando Variáveis:**

As variáveis definidas podem ser utilizadas em qualquer lugar em seu documento CSS, incluindo seletores, propriedades e valores.  
Para acessar uma variável, use a sintaxe `var(--nome-da-variavel)`.

Por exemplo:

    body {
        color: var(--cor-primaria);
        font-size: var(--tamanho-fonte);
    }

Exemplo Completo:

    :root {
        --cor-primaria: #ff0000;
        --cor-secundaria: #00ff00;
        --tamanho-fonte: 16px;
    }

    body {
        color: var(--cor-primaria);
        background-color: var(--cor-secundaria);
        font-size: var(--tamanho-fonte);
    }

Neste exemplo, a cor do texto é definida como a cor primária, o fundo como a cor secundária e o tamanho da fonte como o tamanho-fonte definido anteriormente.

Variáveis em CSS são uma maneira eficiente e flexível de gerenciar valores em seu código, permitindo maior consistência e facilidade de manutenção.  
Elas também são especialmente úteis em cenários de design responsivo, onde os valores podem precisar ser ajustados com base no tamanho da tela ou em outras condições.

## **Imagens**

### **Propriedades de Formatação de Imagens:**

`width e height:` Definem a largura e a altura da imagem.

Exemplo:

    img {
        width: 200px;
        height: auto; /* Mantém a proporção original */
    }

`object-fit`: Especifica como a imagem deve ser redimensionada para caber no contêiner.

Exemplo:

    img {
        width: 200px;
        height: 200px;
        object-fit: cover; /* A imagem é redimensionada para preencher o contêiner, mantendo a proporção e cortando o excesso */
    }

`border`: Adiciona uma borda à imagem.

Exemplo:

    img {
        border: 2px solid #333;
    }

`border-radius`: Adiciona cantos arredondados à imagem.

Exemplo:

    img {
        border-radius: 10px;
    }

`box-shadow`: Adiciona uma sombra à imagem.

Exemplo:

    img {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

### **Sintaxe Básica para Selecionar Imagens:**

Para aplicar estilos a todas as imagens em seu documento HTML, você pode usar a seguinte sintaxe:

    css
    img {
        /* Estilos para todas as imagens */
    }

Se você deseja estilizar apenas imagens com uma classe específica, pode fazer assim:

    css
    .classe-da-imagem {
        /* Estilos para imagens com a classe .classe-da-imagem */
    }

Além disso, você também pode selecionar imagens com base em outros atributos, como o atributo src:

    css
    img[src="caminho/para/imagem.jpg"] {
        /* Estilos para a imagem com o atributo src igual a "caminho/para/imagem.jpg" */
    }

Essas são apenas algumas das maneiras de formatar imagens em CSS. Você pode combinar diferentes propriedades e técnicas para criar o estilo desejado para suas imagens, de acordo com as necessidades de design do seu site.

## **Transformações 2D

permitem mover, girar, escalar e inclinar elementos em um plano 2D.  
Isso é útil para criar efeitos visuais interessantes em elementos HTML, como animações e transições.  

### **translate():**

Move o elemento ao longo do eixo X e/ou Y.

Sintaxe:

    transform: translate(valorX, valorY);

Exemplo:

    .elemento {
        transform: translate(50px, 20px);
    }

### **rotate():**

Gira o elemento em torno de um ponto específico.

Sintaxe:

    transform: rotate(angulo);

Exemplo:

    .elemento {
        transform: rotate(45deg);
    }

### **scale():**

Escala o tamanho do elemento em relação ao ponto de origem.

Sintaxe:

    transform: scale(valorX, valorY);

Exemplo:

    .elemento {
        transform: scale(1.5, 2);
    }

**skew():**

Inclina o elemento ao longo do eixo X e/ou Y.

Sintaxe:

    transform: skew(anguloX, anguloY);

Exemplo:

    .elemento {
        transform: skew(30deg, 20deg);
    }

**matrix():**

Permite especificar uma transformação 2D complexa em uma única função.

Sintaxe:

    transform: matrix(a, b, c, d, e, f);

Cada valor representa uma transformação específica: a e d para escala, b e c para inclinação e e e f para translação.

Exemplo:

    .elemento {
        transform: matrix(1, 0.5, -0.5, 1, 50, 100);
    }

## **Transições**

Permitem animar as mudanças de propriedades CSS de um estado para outro de maneira suave.  
Isso é útil para adicionar efeitos de animação a elementos HTML, como mudanças de cor, tamanho, posição e muito mais.   
As transições CSS oferecem uma maneira simples de adicionar animações suaves a elementos HTML, tornando a experiência do usuário mais dinâmica e interativa.

### **Propriedades de Transição:**

``transition-property``: Especifica qual propriedade CSS deve ser animada.

 Sintaxe:

    transition-property: propriedade1, propriedade2, ...;

``transition-duration``: Especifica a duração da transição.

Sintaxe:

    transition-duration: tempo;

O tempo pode ser definido em segundos (s) ou milissegundos (ms).

``transition-timing-function``: Especifica como a transição deve se comportar em relação ao tempo.

Sintaxe:

    transition-timing-function: função;

Existem várias funções de temporização disponíveis, como ease, linear, ease-in, ease-out, ease-in-out, entre outras.

``transition-delay``: Especifica um atraso antes de iniciar a transição.

Sintaxe:

    transition-delay: tempo;

### **Sintaxe Geral:**

    seletor {
        transition-property: propriedade;
        transition-duration: tempo;
        transition-timing-function: função;
        transition-delay: tempo;
    }

Exemplo de Uso:

Aqui está um exemplo básico de como usar transições CSS:

    .botao {
        background-color: #3498db;
        transition-property: background-color;
        transition-duration: 0.3s;
        transition-timing-function: ease-in-out;
    }

    .botao:hover {
        background-color: #2980b9;
    }

Neste exemplo, quando o mouse passa sobre o botão com a classe ``.botao``, a cor de fundo muda de #3498db para #2980b9 suavemente ao longo de 0.3 segundos, utilizando uma função de temporização ease-in-out.

## **Grids**

Sistemas de layout que nos permitem organizar o conteúdo de uma página da web em linhas e colunas.  
Esses sistemas são especialmente úteis para criar layouts responsivos e bem estruturados. 

### **Grids CSS**

Com o advento do CSS Grid Layout, agora temos uma maneira flexível de criar grids diretamente em CSS, sem depender tanto de estruturas HTML específicas.  
O CSS Grid permite criar layouts bidimensionais, com linhas e colunas, e posicionar elementos de forma precisa.

As propriedades do CSS Grid são usadas para definir a estrutura visual do layout do grid, enquanto o HTML fornece o conteúdo semântico da página. Ao usar CSS Grid, é importante escolher elementos HTML semanticamente apropriados para o seu conteúdo e aplicar o layout de grid usando CSS para organizar esse conteúdo visualmente. Isso ajuda a manter a acessibilidade e a semântica da sua página enquanto cria layouts flexíveis e responsivos.

Exemplo básico de CSS Grid:

    .container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; /* 3 colunas de largura igual */
        grid-gap: 10px; /* Espaçamento entre as células */
    }

### **Grids HTML**

Antes do CSS Grid, os desenvolvedores frequentemente recorriam a sistemas de grid baseados em classes HTML e frameworks CSS como Bootstrap ou Foundation.  
Esses sistemas geralmente exigem uma estrutura HTML específica, com classes que definem o comportamento das células do grid.

Exemplo básico de grid HTML com Bootstrap:

    <div class="container">
        <div class="row">
            <div class="col">Coluna 1</div>
            <div class="col">Coluna 2</div>
            <div class="col">Coluna 3</div>
        </div>
    </div>

### **Grid Container**

É o elemento que contém os itens do grid. É o pai dos itens do grid e onde você define as propriedades de layout do grid.  

Em termos de semântica, o Grid Container pode ser qualquer elemento HTML que faça sentido em seu contexto.  

Por exemplo, você pode usar um ``<div>`` genérico como contêiner de grid ou um elemento com significado semântico, como ``<section>`` ou ``<main>``, dependendo da estrutura do seu conteúdo.

    html
    <div class="grid-container">
    <!-- Itens do grid aqui -->
    </div>
Neste exemplo, um ``<div>`` é usado como um contêiner de grid. Este elemento contém os itens do grid e é onde as propriedades de layout do grid serão aplicadas.


### **grid-template-columns e grid-template-rows**

Permitem definir o número e o tamanho das colunas e linhas do grid, respectivamente.  

Você pode especificar os tamanhos das colunas/linhas em pixels, porcentagens, unidades flexíveis (fr) ou outras unidades CSS.  

    css
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr; /* Define três colunas com larguras proporcionais */
        grid-template-rows: auto 100px; /* Define duas linhas, uma com altura automática e outra com 100 pixels */
    }

### **Gap**

Define o espaçamento entre as células do grid, tanto horizontalmente quanto verticalmente.  

Você pode especificar um valor para o espaçamento em pixels, em porcentagens ou em outras unidades CSS.  

    css
    .grid-container {
        display: grid;
        grid-gap: 20px; /* Define um espaçamento de 20 pixels entre as células do grid */
    }


### **grid-template**

É uma propriedade abreviada que combina as propriedades grid-template-rows, grid-template-columns e grid-template-areas em uma única declaração.  

Ela permite definir a estrutura do grid, incluindo as linhas, colunas e áreas nomeadas, tudo em uma única linha de código.  

    css
    .grid-container {
        display: grid;
        grid-template:
            "header header header"
            "sidebar content content"
            "footer footer footer";
    }
Neste exemplo, estamos definindo um layout de grid com três linhas e três colunas, onde as áreas são nomeadas como "header", "sidebar", "content" e "footer".

### **grid-items**

O posicionamento de grid-items no CSS Grid refere-se à maneira como os itens individuais dentro do grid são colocados e organizados.  
Isso pode ser feito especificando as linhas e colunas em que cada item deve ser colocado ou usando propriedades que afetam o posicionamento dentro das células do grid. 

**Definindo linhas e colunas:**  

Você pode usar as propriedades ``grid-column`` e ``grid-row`` para especificar em qual linha e coluna um item do grid deve ser colocado.

    .grid-item {
        grid-column: 2 / 4; /* Ocupa da segunda à quarta coluna */
        grid-row: 1 / 3; /* Ocupa da primeira à segunda linha */
    }

**Posicionamento automático:**  

Se você não especificar explicitamente o posicionamento de um item, ele será colocado automaticamente em ordem, começando da primeira linha e primeira coluna.

    .grid-item:nth-child(2) {
        /* Este item será colocado automaticamente na segunda posição do grid */
    }

**Espaçamento interno:**

Você pode usar a propriedade ``grid-gap`` para adicionar espaçamento entre os itens do grid, o que pode afetar indiretamente o posicionamento visual.

    .grid-container {
        display: grid;
        grid-gap: 20px; /* Adiciona espaçamento de 20 pixels entre os itens do grid */
    }

**Alinhamento e justificação:**

As propriedades ``justify-self`` e ``align-self`` podem ser usadas para alinhar itens individualmente dentro das células do grid.

    .grid-item {
        justify-self: center; /* Alinha o item horizontalmente no centro da célula */
        align-self: end; /* Alinha o item verticalmente na parte inferior da célula */
    }

**Ordenação:**

A propriedade ``order`` permite reorganizar visualmente a ordem dos itens do grid, independentemente da ordem no HTML.

    .grid-item:nth-child(3) {
        order: 1; /* Coloca este item como o primeiro visualmente */
    }

### **Função repeat()**

A função ``repeat()`` permite repetir um padrão de valores várias vezes.  
Ela é frequentemente usada em conjunto com propriedades que aceitam uma lista de valores, como ``grid-template-columns`` e ``grid-template-rows``, para definir um padrão de colunas ou linhas de forma mais concisa.

A sintaxe básica da função repeat() é ``repeat(n, value)``, onde n é o número de repetições e value é o valor a ser repetido.  

Exemplo de uso da função repeat() com grid-template-columns:

    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 100px); /* Cria três colunas de 100 pixels cada */
    }

Neste exemplo, repeat(3, 100px) cria três colunas de 100 pixels cada dentro do grid.

### **Função calc()**

A função ``calc()`` permite realizar cálculos matemáticos para definir valores de propriedades CSS.   
Ela é útil para criar layouts mais dinâmicos e adaptáveis, especialmente em situações onde valores precisam ser relativos a outras propriedades.  

A sintaxe básica da função calc() é ``calc(expressão)``, onde expressão é uma expressão matemática que pode incluir operadores aritméticos (+, -, *, /) e unidades de medida.  

Exemplo de uso da função calc() para definir a largura de um elemento com base em porcentagem:

    .element {
        width: calc(50% - 20px); /* Define a largura como metade do contêiner menos 20 pixels */
    }

Neste exemplo, a largura do elemento é definida como metade da largura do contêiner, subtraindo 20 pixels.

### **Posicionamento com regiões nomeadas**

É uma técnica avançada de layout no CSS Grid, onde é possível nomear áreas específicas dentro do grid e, em seguida, posicionar os itens do grid nessas áreas nomeadas.  

Ele oferece uma maneira clara e declarativa de definir a estrutura do layout, o que pode melhorar a legibilidade e a manutenção do código CSS.

**Definindo áreas nomeadas:**  

Para definir áreas nomeadas em um grid, você usa a propriedade ``grid-template-areas`` no ``grid-Container``, especificando os nomes das áreas em um esquema de grade.

    css
    .grid-container {
        display: grid;
        grid-template-areas:
            "header header"
            "sidebar content"
            "footer footer";
    }

Neste exemplo, estamos definindo três áreas nomeadas: "header", "sidebar" e "footer", cada uma ocupando duas colunas no grid.

**Posicionando itens nas áreas nomeadas:**

Depois de definir as áreas nomeadas, você pode posicionar os itens do grid nessas áreas usando a propriedade ``grid-area``.

    css
    .item {
        grid-area: header;
    }

Neste exemplo, estamos posicionando um item do grid na área nomeada "header".

Exemplo completo:

    html

    <div class="grid-container">
        <div class="item" style="grid-area: header;">Header</div>
        <div class="item" style="grid-area: sidebar;">Sidebar</div>
        <div class="item" style="grid-area: content;">Content</div>
        <div class="item" style="grid-area: footer;">Footer</div>
    </div>

    css

        .grid-container {
            display: grid;
            grid-template-areas:
                "header header"
                "sidebar content"
                "footer footer";
            grid-gap: 10px;
        }
        .item {
            border: 1px solid #ccc;
            padding: 20px;
        }

### **Unidade de Medida fr**

A unidade de medida ``fr`` (fração) é uma unidade de medida exclusiva do CSS Grid que permite distribuir o espaço disponível em uma grade entre as colunas ou linhas de forma proporcional.  
A unidade ``fr`` divide o espaço disponível em partes iguais, atribuindo uma fração do espaço a cada coluna ou linha com base na proporção especificada.

A semântica da unidade ``fr`` está diretamente relacionada à distribuição de espaço dentro de um contêiner de grid.  
Ela permite criar layouts flexíveis e responsivos, onde as colunas e linhas podem se ajustar dinamicamente ao tamanho do contêiner e ao conteúdo dentro dele.  

A unidade de medida fr é uma ferramenta poderosa para criar layouts fluidos e responsivos com o CSS Grid. Ela oferece uma maneira simples e eficaz de distribuir o espaço disponível em uma grade de forma proporcional, o que é fundamental para criar layouts flexíveis e adaptáveis a diferentes tamanhos de tela e dispositivos.  

Aqui estão alguns exemplos de como pode-se usar a unidade fr:

**Distribuição proporcional de espaço:**

    css

    .grid-container {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr; /* Distribui o espaço em três colunas, sendo a segunda coluna com o dobro do tamanho da primeira e terceira */
    }

**Uso em conjunto com outras unidades de medida:**

    css
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 100px 2fr; /* Distribui o espaço em três colunas, sendo a primeira e terceira coluna ocupando uma fração do espaço disponível e a segunda coluna com 100 pixels de largura */
    }

**Uso em linhas:**

    css
    .grid-container {
        display: grid;
        grid-template-rows: 1fr 2fr; /* Distribui o espaço em duas linhas, sendo a segunda linha com o dobro do tamanho da primeira */
    }

**Uso em layouts responsivos:**

    css
    .grid-container {
        display: grid;
        grid-template-columns: 1fr; /* Distribui o espaço em uma única coluna, ocupando todo o espaço disponível */
    }

    @media (min-width: 768px) {
        .grid-container {
            grid-template-columns: repeat(2, 1fr); /* Em telas maiores, distribui o espaço em duas colunas com larguras iguais */
        }
    }

### **Função minmax()**

Permite definir um intervalo para o tamanho de uma coluna ou linha em uma grade.  
Essa função é útil para criar layouts flexíveis, onde você deseja especificar um tamanho mínimo e máximo para elementos de grade, permitindo que eles se ajustem dinamicamente dependendo do conteúdo ou do espaço disponível.  

A função ``minmax()`` é especialmente útil quando combinada com outras unidades de medida, como ``fr``, para criar layouts flexíveis e responsivos.   
Ela permite que especifique limites claros para o tamanho dos elementos de grade, garantindo que o layout se adapte de forma eficaz a diferentes tamanhos de tela e conteúdos variáveis.  

A semântica da função minmax() está diretamente relacionada à definição de intervalos de tamanho para colunas e linhas em uma grade, o que é essencial para garantir layouts responsivos e adaptáveis.

Aqui está a sintaxe básica da função minmax():

    css
    minmax(min, max)

Onde:

``min`` é o tamanho mínimo que a coluna ou linha pode ter.  
``max`` é o tamanho máximo que a coluna ou linha pode ter.

Exemplo de uso da função ``minmax()`` para definir o tamanho das colunas em uma grade:

    css
    .grid-container {
        display: grid;
        grid-template-columns: minmax(100px, 1fr) minmax(200px, 2fr);
    }

Neste exemplo, estamos definindo duas colunas em uma grade.  
A primeira coluna terá um tamanho mínimo de 100 pixels e uma fração do espaço disponível (1fr) como tamanho máximo.  
A segunda coluna terá um tamanho mínimo de 200 pixels e o dobro da fração do espaço disponível (2fr) como tamanho máximo.

## **Flexbox**

Ou Flexible Box Layout, é um modelo de layout bidimensional que permite criar layouts mais complexos e flexíveis em CSS.  

Ele introduz um novo sistema de layout, que é especialmente útil para organizar elementos em uma única dimensão - seja horizontal ou verticalmente.  

### **Container (Pai)**

O elemento que envolve todos os itens flexíveis. Para criar um container flexível, você define o display como flex:

    css
    .container {
        display: flex;
    }

### **Flex Item (Filho)**

Os elementos filhos dentro do container flexível são chamados de itens flexíveis.  
Eles se adaptam ao espaço disponível dentro do container de acordo com as propriedades do Flexbox.

### **Propriedades do Container (Pai)**

``display``  
Define um container como um flex container.  

Sintaxe:

    display: flex;

``flex-direction``  
Define a direção principal dos itens flexíveis no container.  

Sintaxe:

    flex-direction: row | row-reverse | column | column-reverse;

``justify-content``  
Alinha os itens flexíveis ao longo do eixo principal do container.  

Sintaxe:

    justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly;

``flex-wrap``  
Define se os itens flexíveis devem envolver em múltiplas linhas ou não.

Sintaxe:

    flex-wrap: nowrap | wrap | wrap-reverse;

``align-items``  
Alinha os itens flexíveis ao longo do eixo transversal do container.  

Sintaxe:

    align-items: stretch | flex-start | flex-end | center | baseline;

``align-conten``  
Alinha as linhas flexíveis quando há espaço extra no eixo transversal.  

Sintaxe:

    align-content: flex-start | flex-end | center | space-between | space-around | stretch;

Exemplo completo:

    css

    .container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        align-content: space-around;
    }

    .item {
        flex: 1 1 200px; /* Tamanho flexível: grow, shrink, base */
        /* Outras propriedades de estilo */
    }

Neste exemplo, temos um container flexível com vários itens flexíveis.  

Os itens são distribuídos horizontalmente (``flex-direction: row``) com espaço entre eles (``justify-content: space-between``).  

Eles são alinhados verticalmente no centro (``align-items: center``).  

Se houver mais de uma linha de itens, o espaço extra é distribuído uniformemente ao redor de cada linha (``align-content: space-around``).  

Cada item flexível possui uma largura mínima de 200 pixels e pode crescer e encolher conforme necessário.

## **Media queries**

As Media Queries são uma parte crucial do desenvolvimento responsivo da web, permitindo que os estilos CSS sejam adaptados com base nas características do dispositivo ou do navegador em que o conteúdo está sendo exibido.  

As Media Queries oferecem uma boa maneira de criar layouts responsivos e adaptáveis, garantindo que o conteúdo seja exibido de forma adequada em uma variedade de dispositivos e tamanhos de tela.  
A estratégia "Mobile First" é uma abordagem eficaz para garantir uma experiência de usuário consistente em todos os dispositivos.

### **Anatomia das Media Queries:**

Uma Media Query consiste em uma regra de CSS que define um conjunto de estilos a serem aplicados quando determinadas condições são atendidas.  

A sintaxe básica de uma Media Query é:

    @media (condição) {
        /* Estilos a serem aplicados */
    }

### **Funcionalidades Media Query:**

**Width (largura) e Height (altura):**  
Controla as larguras e alturas da janela do navegador.

    @media (min-width: 768px) {
        /* Estilos para telas maiores que 768px de largura */
    }

**Device-Width (largura do dispositivo) e Device-Height (altura do dispositivo):**  
Controla as dimensões físicas do dispositivo.

    @media (max-device-width: 480px) {
        /* Estilos para dispositivos com largura máxima de 480px */
    }

**Orientation (orientação):**  
Controla a orientação do dispositivo (paisagem ou retrato).

    @media (orientation: landscape) {
        /* Estilos para dispositivos na orientação paisagem */
    }

**Aspect-Ratio (proporção de aspecto) e Device-Aspect-Ratio (proporção de aspecto do dispositivo):**  
Controla a proporção de aspecto da tela ou do dispositivo.

    @media (min-aspect-ratio: 16/9) {
        /* Estilos para telas com uma proporção de aspecto mínima de 16:9 */
    }

**Color, Color-Index e Monochrome:**  
Controla a profundidade de cor, o índice de cores e a capacidade monocromática do dispositivo.

    @media (min-color: 256) {
        /* Estilos para dispositivos com capacidade de cor mínima de 256 */
    }

**Resolution (resolução):**  
Controla a resolução de exibição do dispositivo.

    @media (min-resolution: 300dpi) {
        /* Estilos para dispositivos com resolução mínima de 300dpi */
    }

**Scan (varredura) e Grid:**  
Controla a progressão de varredura da tela e a capacidade de grid do dispositivo.

### **Breakpoints:**

Os breakpoints são pontos específicos em que o layout de uma página da web muda em resposta à largura da tela ou a outras características do dispositivo.  

No modelo "Mobile First", o design é primeiro otimizado para dispositivos móveis e, em seguida, é gradualmente aprimorado para dispositivos maiores usando Media Queries.  


Exemplo de Uso:

css

    /* Estilos base para dispositivos móveis */
    body {
        font-size: 16px;
    }

    /* Media Query para telas maiores que 768px */
    @media (min-width: 768px) {
        body {
            font-size: 18px;
        }
    }

Neste exemplo, o tamanho da fonte é aumentado para 18 pixels em dispositivos com largura de tela maior que 768 pixels.

## **Responsividade em imagens**

A responsividade em imagens é uma parte importante do desenvolvimento web moderno, garantindo que as imagens sejam exibidas de forma adequada e otimizada em uma variedade de dispositivos e tamanhos de tela.  
Existem várias técnicas para tornar as imagens responsivas.

### **Largura máxima com max-width:**

Essa técnica permite que as imagens redimensionem proporcionalmente em dispositivos menores, impedindo que ultrapassem a largura do contêiner pai.  

    html

    <img src="imagem.jpg" style="max-width: 100%;" alt="Descrição da imagem">

Neste exemplo, a largura máxima da imagem é definida como 100%, garantindo que ela nunca ultrapasse a largura do contêiner pai, tornando-a responsiva.  

### **Largura em porcentagem:**

É possível definir diretamente a largura da imagem em porcentagem, em relação à largura do contêiner pai.

    html

    <img src="imagem.jpg" style="width: 50%;" alt="Descrição da imagem">

Neste caso, a imagem terá sempre metade da largura do contêiner pai, tornando-a responsiva.  

### **CSS com max-width:**

Aplicar estilos CSS para imagens no arquivo de estilo, usando max-width para garantir a responsividade.

    css

    img {
        max-width: 100%;
        height: auto;
    }

Isso garante que todas as imagens do site tenham uma largura máxima de 100% do contêiner pai e mantenham sua proporção original de largura para altura, tornando-as responsivas.  

### **Unidades de viewport:**

Usar unidades de viewport, como ``vw`` (viewport width) e ``vh`` (viewport height), para definir as dimensões das imagens em relação às dimensões da janela do navegador.

    css

    img {
        width: 50vw;
        height: auto;
    }

Neste exemplo, a largura da imagem é definida como 50% da largura da viewport, tornando-a proporcional ao tamanho da tela do dispositivo.

### **Media Queries:**

Usar Media Queries para definir estilos diferentes para diferentes tamanhos de tela, incluindo a largura das imagens.

    css

    @media (max-width: 768px) {
        img {
            width: 100%;
            height: auto;
        }
    }

Neste exemplo, a largura da imagem é definida como 100% quando a largura da tela é igual ou inferior a 768 pixels, garantindo que a imagem se ajuste à largura do dispositivo em telas menores.

Essas são algumas das técnicas comuns para tornar as imagens responsivas em uma página da web. Ao aplicar essas técnicas, você pode garantir que suas imagens sejam exibidas de forma adequada e otimizada em uma variedade de dispositivos e tamanhos de tela.


### **Atributos HTML para imagens flexíveis:**

``srcset``  
Permite especificar uma lista de imagens e suas larguras correspondentes, permitindo que o navegador escolha a melhor imagem com base na resolução do dispositivo.

    html

    <img src="imagem-pequena.jpg" srcset="imagem-grande.jpg 2x" alt="Descrição da imagem">

Neste exemplo, se o dispositivo tiver uma densidade de pixels (pixel ratio) de 2x, o navegador carregará a imagem imagem-grande.jpg para uma melhor qualidade.

``sizes``  
Informa ao navegador como as imagens devem ser exibidas em diferentes tamanhos de tela. Ele define o tamanho da imagem em relação à largura da janela do navegador.

    html

    <img src="imagem-pequena.jpg" srcset="imagem-pequena.jpg 500w, imagem-media.jpg 800w, imagem-grande.jpg 1200w" sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px" alt="Descrição da imagem">

Neste exemplo, o tamanho da imagem é ajustado com base no tamanho da janela do navegador.  
Ela será exibida em 100% da largura da janela para dispositivos com largura máxima de 600px, em 50% da largura da janela para dispositivos com largura máxima de 1200px, e com uma largura fixa de 800px para dispositivos maiores que 1200px.

Exemplo completo com CSS:

Além dos atributos HTML, você também pode usar CSS para estilizar e controlar ainda mais o comportamento das imagens flexíveis:

    html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Imagens Flexíveis</title>
        <style>
            img {
                max-width: 100%; /* Garante que a imagem não exceda o tamanho do contêiner */
                height: auto; /* Mantém a proporção original da imagem */
                display: block; /* Remove o espaço extra abaixo da imagem */
            }
        </style>
    </head>
    <body>
        <img src="imagem.jpg" srcset="imagem.jpg 1x, imagem-2x.jpg 2x" sizes="(max-width: 600px) 100vw, 50vw" alt="Descrição da imagem">
    </body>
    </html>

Neste exemplo, a imagem será redimensionada automaticamente para se ajustar ao tamanho do contêiner pai, garantindo uma experiência responsiva em diferentes dispositivos e tamanhos de tela.

### **Picture**

A declaração ``<picture>`` é uma forma avançada de fornecer imagens flexíveis e responsivas em páginas da web.  

Permitindo que personalize a experiência visual de acordo com as características do dispositivo e do contexto de visualização.   

Isso é essencial para garantir uma experiência de usuário consistente e de alta qualidade em diferentes dispositivos e tamanhos de tela.

Ela permite que seja especificado várias fontes de imagem e condições de mídia para que o navegador possa escolher a melhor imagem com base nas características do dispositivo, como densidade de pixels, tamanho da tela e orientação.  

Isso é particularmente útil quando é necessário fornecer diferentes imagens para diferentes dispositivos ou contextos de visualização.  

Sintaxe:

    html

    <picture>
        <source srcset="imagem-grande.jpg" media="(min-width: 1200px)">
        <source srcset="imagem-media.jpg" media="(min-width: 600px)">
        <img src="imagem-pequena.jpg" alt="Descrição da imagem">
    </picture>


A declaração ``<picture>`` oferece suporte à técnica de "art direction", que é a prática de escolher diferentes imagens com base em considerações estéticas ou de layout específicas para diferentes contextos de visualização.

Exemplo de Uso:

    html

    <picture>
        <source srcset="imagem-grande.jpg" media="(min-width: 1200px)">
        <source srcset="imagem-media.jpg" media="(min-width: 600px)">
        <img src="imagem-pequena.jpg" alt="Descrição da imagem">
    </picture>

Neste exemplo:

Se a largura da janela do navegador for maior ou igual a 1200 pixels, o navegador carregará a imagem imagem-grande.jpg.  
Se a largura da janela do navegador for maior ou igual a 600 pixels (mas menor que 1200 pixels), o navegador carregará a imagem imagem-media.jpg.  
Se a largura da janela do navegador for menor que 600 pixels, o navegador carregará a imagem imagem-pequena.jpg.  


