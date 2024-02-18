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

## **Float e Clear**

As propriedades `float` e `clear` são frequentemente usadas em conjunto para criar layouts de página complexos, especialmente em designs antigos que utilizam um método chamado "float layout".

### **Float:**

A propriedade `float` é usada para especificar que um elemento deve ser retirado do fluxo normal e colocado ao lado do elemento anterior, à esquerda ou à direita, até que não haja espaço disponível ou até que outro elemento flutuante seja encontrado.

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

A propriedade ``z-index`` é utilizada para controlar a ordem de empilhamento dos elementos em um layout, especificamente em situações onde os elementos se sobrepoem uns aos outros.  
Ela determina qual elemento será exibido acima dos outros quando houver sobreposição.  

Sintaxe:

    z-index: valor;

O valor pode ser um número inteiro positivo, negativo ou auto.  
Quanto maior o valor, mais acima na pilha o elemento será empilhado.

Exemplo:

    z-index: 1;

Se dois elementos se sobrepõem e têm ``z-index`` definidos, o elemento com o maior valor de z-index será exibido acima do outro.

### **auto:**

O valor ``auto`` indica que o navegador deve calcular automaticamente a ordem de empilhamento do elemento com base na ordem de seus elementos ancestrais.

Sintaxe:

    z-index: auto;

Isso é útil quando você quer que o navegador decida a ordem de empilhamento dos elementos com base em sua hierarquia no DOM.

É importante observar que a propriedade ``z-index`` só tem efeito em elementos cuja propriedade ``position`` é definida como ``absolute``, ``relative`` ou ``fixed``.  
Além disso, ela afeta apenas elementos que estão no mesmo contexto de empilhamento, ou seja, que têm o mesmo ancestral que define uma pilha de contexto.

A propriedade ``z-index`` é uma ferramenta poderosa para controlar a sobreposição de elementos em um layout, permitindo que você crie designs complexos e dinâmicos.  
No entanto, é importante usá-la com cautela para evitar problemas de usabilidade e acessibilidade.
