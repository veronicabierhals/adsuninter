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

Exemplo: `#cabecalho { font-size: 24px; }`  
<br>

### **Seletores class**

Uma classe é um seletor que pode ser aplicado a vários elementos em um documento HTML.

Você pode usar a mesma classe em múltiplos elementos para aplicar estilos semelhantes a eles.

Para selecionar um elemento por classe no CSS, use um ponto `(.)` seguido pelo nome da classe.

Exemplo: `.botao-vermelho { color: red; }`  
<br>

### **Seletores universal**

O seletor universal `(*)` seleciona todos os elementos em um documento HTML.

É útil quando você deseja aplicar um estilo global a todos os elementos do documento.

No entanto, deve ser usado com cautela, pois pode afetar o desempenho do seu CSS, especialmente em documentos grandes.

Exemplo: `* { margin: 0; padding: 0; }`  
<br>

### **Agrupamento de seletores**

O agrupamento de seletores permite aplicar o mesmo conjunto de estilos a múltiplos seletores.

Isso pode reduzir a repetição de código e tornar seu CSS mais conciso e legível.

Você pode agrupar seletores separando-os por vírgulas (,).

Exemplo: `h1, h2, h3 { font-family: Arial, sans-serif; }`

## **Como aplicar o CSS**

### **Externo**

O CSS externo é definido em um arquivo separado com extensão `.css` e, em seguida, é vinculado ao documento HTML usando a tag `<link>` no elemento ´`<head>``.

`<link rel="stylesheet" type="text/css" href="styles.css">`

### **Interno (incorporado)**

O CSS interno é definido dentro da seção `<style>` no elemento `<head>` do documento HTML e afeta apenas o documento onde está definido.

`<style>
        /* Estilos internos */
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            color: blue;
        }
    </style>
   `

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

`/* comentário aqui */`

## **Tipos de Cores**

Podem ser aplicadas em textos, fundos e bordas.

### **Por Nome:**

Usando uma cor pré-definida, como "red", "blue", "green", etc.

Exemplo:  
`color: red;`

### **Hexadecimal:**

Você pode especificar uma cor usando seu valor hexadecimal. Isso envolve uma combinação de seis caracteres, que representam os componentes de cor vermelha, verde e azul (RGB).

Exemplo:  
`color: #ff0000;` (vermelho)

### **RGB (Red, Green, Blue):**

Usar os valores de intensidade de vermelho, verde e azul em uma escala de 0 a 255.

Exemplo:  
`color: rgb(255, 0, 0);` (vermelho)

### **RGBA (Red, Green, Blue, Alpha):**

Semelhante ao RGB, mas com um quarto valor para a transparência (alfa), que varia de 0 (totalmente transparente) a 1 (totalmente opaco).

Exemplo:  
`color: rgba(255, 0, 0, 0.5);`  
(vermelho com 50% de transparência)

### **HSL (Hue, Saturation, Lightness):**

Definir uma cor usando matiz (um ângulo de 0 a 360 graus), saturação (porcentagem) e luminosidade (porcentagem).

Exemplo:  
`color: hsl(0, 100%, 50%);`

### **HSLA (Hue, Saturation, Lightness, Alpha):**

Semelhante ao HSL, mas com um quarto valor para a transparência (alfa), que varia de 0 (totalmente transparente) a 1 (totalmente opaco).

Exemplo:  
`color: hsla(0, 100%, 50%, 0.5);`  
(vermelho com 50% de transparência)

## **Como aplicar as cores**

### **Texto (color):**

Você pode definir a cor do texto usando a propriedade `color`.

Exemplo:  
`color: blue;`

### **Fundo (background-color):**

Você pode definir a cor de fundo de um elemento usando a propriedade `background-color`.

Exemplo:  
`background-color: #ff0000;` (vermelho)

### **Bordas (border-color):**

Você pode definir a cor das bordas de um elemento usando a propriedade `border-color`.

Exemplo:  
`border-color: rgb(0, 255, 0);` (verde)

### **Gradientes (background-image):**

Além de cores sólidas, você pode aplicar gradientes usando a propriedade `background-image`.

Exemplo: `background-image: linear-gradient(to right, red, yellow);`

### **Sombra (box-shadow, text-shadow):**

Você pode definir a cor da sombra de um elemento usando as propriedades `box-shadow` (para sombras de caixa) e `text-shadow` (para sombras de texto).

Exemplo: `box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);` (Sombra preta com 50% de transparência)

### **Elementos SVG:**

Em elementos SVG, você pode definir cores diretamente ou usando a propriedade `fill` para preenchimento e `stroke` para contorno.

Exemplo:  
`fill: #00ff00;` (verde)  
`stroke: blue;`

### **Pseudo-elementos (before, after):**

Você pode aplicar cores a pseudo-elementos usando as mesmas propriedades que aplicaria a elementos regulares.

Exemplo:  
`.elemento::before {background-color: rgba(255, 0, 0, 0.5)}`  
(vermelho com 50% de transparência)

## **Margens**

## **Propriedade de Margem Simples:**

A propriedade margin pode ser usada para definir a margem em todas as quatro direções simultaneamente.

Sintaxe:  
`margin: 10px;`  
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
`margin: -10px;`  
margem de -10 pixels em todas as direções

### **Margem Automática:**

A palavra-chave auto pode ser usada para definir margens automáticas, o que permite que um elemento seja centralizado horizontalmente dentro de seu contêiner.

Sintaxe:  
`margin: auto;`
centraliza horizontalmente o elemento dentro do contêiner

### **Múltiplas Margens:**

Você pode definir margens diferentes para cada lado separadamente, em uma única declaração.

Sintaxe:  
`margin: 10px 20px 15px 5px;`  
margem superior, direita, inferior e esquerda, respectivamente

## **Bordas**

### **Borda Simples:**

A propriedade `border` define uma borda em todas as quatro direções simultaneamente.

Sintaxe:  
`border: 1px solid black;`  
Borda de 1 pixel de largura, sólida e preta

### **Bordas Individuais:**

Você também pode definir bordas separadamente para cada lado usando as propriedades `border-top`, `border-right`, `border-bottom` e `border-left`.

Sintaxe:  
`border-top: 2px dashed red;`  
Borda superior de 2 pixels de largura, tracejada e vermelha

### **Estilo da Borda:**

O estilo da borda pode ser especificado usando palavras-chave como `solid` (sólido), `dashed` (tracejado), `dotted` (pontilhado), entre outros.

Sintaxe:  
`border: 2px dashed blue;`  
Borda de 2 pixels de largura, tracejada e azul

### **Largura da Borda:**

Você pode definir a largura da borda em pixels (px), emems (em), rem, ou como uma porcentagem (%) da largura do elemento.

Sintaxe:  
`border: 3px solid green;`  
Borda de 3 pixels de largura, sólida e verde

### **Cor da Borda:**

A cor da borda pode ser especificada usando nomes de cores, códigos hexadecimais, RGB, RGBA ou HSL.

Sintaxe:  
`border: 1px solid #ff0000;`  
Borda de 1 pixel de largura, sólida e vermelha

### **Borda Arredondada:**

Você pode criar bordas arredondadas usando as propriedades `border-radius` para especificar o raio dos cantos.

Sintaxe:  
`border-radius: 5px;`  
Raio de 5 pixels para todos os cantos

## **Padding**

O preenchimento (padding) em CSS é usado para controlar o espaço entre o conteúdo de um elemento e suas bordas.  
Ele cria um espaço interno dentro do elemento.  

### **Padding Simples:**

A propriedade ``padding`` define o preenchimento em todas as quatro direções simultaneamente.  

Sintaxe:
``padding: 10px;``  
Preenchimento de 10 pixels em todas as direções

### **Preenchimento Individual:**

Você também pode definir o preenchimento separadamente para cada direção usando as propriedades ``padding-top``, ``padding-right``, ``padding-bottom`` e ``padding-left``.  

Sintaxe:  
``padding-top: 5px;`` Preenchimento superior de 5 pixels  
``padding-right: 15px;`` Preenchimento direito de 15 pixels  
``padding-bottom: 10px;``Preenchimento inferior de 10 pixels  
``padding-left: 20px;``  Preenchimento esquerdo de 20 pixels  

### **Preenchimento Múltiplo:**

Você pode definir diferentes valores de preenchimento para cada lado em uma única declaração.  

Sintaxe:
``padding: 10px 20px 15px 5px;``  
Preenchimento superior, direito, inferior e esquerdo, respectivamente

### **Preenchimento com Porcentagem:**

Além de valores fixos, você também pode especificar o preenchimento como uma porcentagem da largura do elemento pai.  

Sintaxe:
``padding: 5% 10% 7% 3%;``  
Preenchimento superior, direito, inferior e esquerdo, respectivamente, em porcentagem

### **Valores Negativos de Preenchimento:**

Assim como com as margens, você também pode usar valores negativos de preenchimento para ajustar o layout e a sobreposição de elementos.

Sintaxe:  
``padding: -10px;``  
Preenchimento de -10 pixels em todas as direções

