# JavaScript

## **Ambientes de desenvolvimento online**

Ambientes de desenvolvimento _on-line_ disponibilizam um editor de código e executam o código diretamente no navegador _web_, tornando possível compartilhar os códigos digitados.

Os editores _on-line_ têm características similares.
São normalmente utilizados como plataformas de teste ou treinamento e para postar soluções de problemas de programação.

Alguns ambientes de programação:

-   [CodePen](https://codepen.io/pen/)
-   [JsBin](https://jsbin.com/?html,output)
-   [JSFiddle](https://jsfiddle.net/)

São soluções didáticas e para testes, porém não são ambientes de desenvolvimento completos.

## **Ambientes de desenvolvimento local**

### **Editores de códigos**

-   **_Visual Studio Code_ (VS Code)** – bastante utilizado e gratuito, conta com recursos integrados, como depurador _JavaScript_ e ferramentas que otimizam projetos; é personalizável, com a possibilidade de baixar extensões.

-   **_WebStorm_** – adequado para grandes projetos, pesado e complexo para pequenos programas; destina-se a uso comercial e não é gratuito.

-   **_Sublime Text_** – rápido e fácil de usar, pode ser utilizado por um período de avaliação; Para uso por tempo mais longo, é necessário adquirir uma licença paga.

-   **_NotePad++_** – de uso gratuito, é leve e rápido.

### **Interpretador**

O interpretador é um programa que executa instrução por instrução.

Ao desenvolver um aplicativo que rode do lado do servidor, certamente o interpretador escolhido pode ser o node.js.

Se o programa rodar no lado do cliente, o próprio navegador será o interpretador.

Todos os navegadores contam com interpretadores integrados.

### **Depurador**

São ferramentas que permitem executar instruções de um programa, passo a passo.

Quando usamos o navegador _web_ como interpretador de _JavaScript,_ também obtemos um depurador.

Todos os navegadores possuem ferramentas de desenvolvedor.

Durante a visualização de páginas _web_, quando você está navegando habitualmente, não os vê; é necessário ativar essas ferramentas.

As ferramentas normalmente disponibilizadas pelos navegadores são:

-   **Inspetor de códigos**: permite, por exemplo, verificar os elementos HTML individuais de um _site_ aberto.

-   **Console _JavaScript_**: exibe informações sobre os erros e nos permite executar comandos _JavaScript_ exclusivos no contexto da página atual.

-   **Depurador**: permite executar passo a passo as instruções.

Dependendo do navegador, o comando para exibir as ferramentas de desenvolvimento pode ser diferente.

Vale também fazer uma pesquisa no _Google_, sempre que esquecer os comandos, ou mudar de navegador.

Combinação de tecla(s) para exibir o depurador (console):

-   _Internet Explorer_ e _Edge_: tecla F12.
-   Demais navegadores: teclas CTRL+SHIFT+J.

### **Ferramentas**

-   **Gerenciadores de pacotes**: permitem utilizar bibliotecas que contêm soluções prontas para ser empregadas em programas ou componentes para o desenvolvimento, como por exemplo: Npm ou Yarn. O Npm é o gerenciador-padrão do node.js, e o Yarn foi desenvolvido pelo _Facebook_.

-   **Executores de tarefas e empacotadores de módulos**: possibilitam automatizar o processo de desenvolvimento de _software_ e agrupar o código resultante de vários arquivos e bibliotecas, como Grunt ou Webpack.

-   **_Frameworks_ de teste**: permitem executar testes automáticos; como exemplos, temos Mocha, Jasmine ou Jest.

-   **_Scanners_ de segurança**: possibilitam verificar a segurança da solução. Snyk e RetireJs são alguns exemplos.

## **Variáveis**

São usadas para armazenar dados. Você pode declarar variáveis usando as palavras-chave `var`, `let` ou `const`.

`var`: Era a forma antiga de declarar variáveis, ainda suportada, mas menos utilizada atualmente.

    var nomeDaVariavel = valor;

`let`: Introduzida no ECMAScript 6 (ES6), é usada para declarar variáveis que podem ser reatribuídas.

    let nomeDaVariavel = valor;

`const`: Também introduzida no ES6, é usada para declarar variáveis ​​com valores que não mudam.

    const nomeDaVariavel = valor;

Exemplo:

    let idade = 25; // Declara uma variável 'idade' e atribui o valor 25
    const PI = 3.14; // Declara uma variável constante 'PI' e atribui o valor 3.14

Você pode usar variáveis para armazenar números, strings, booleanos, objetos, arrays e muito mais.

### **Nomes de variáveis**

Em JavaScript, os nomes de variáveis seguem algumas regras:

-   Podem conter letras, dígitos, underscores (\_) e cifrões ($).
-   Devem começar com uma letra, um underscore (\_) ou um cifrão ($). Não podem começar com um dígito.
-   São case-sensitive, ou seja, diferenciam maiúsculas de minúsculas.
-   Não podem ser palavras reservadas, como var, let, const, function, entre outras.

Exemplos válidos de nomes de variáveis:

    let nome;
    let idadeUsuario;
    let _variavel;
    let $precoProduto;
    let meuNomeCompleto;

Exemplos inválidos de nomes de variáveis:

    let 1numero; // começa com um dígito
    let minha variavel; // contém um espaço
    let função; // palavra reservada

É uma prática recomendada escolher nomes de variáveis descritivos e significativos para tornar seu código mais legível e compreensível.

## **Tipos de dados**

Existem diversos tipos de dados que podem ser atribuídos a variáveis.

Aqui estão os principais tipos:

**Number (Número)**:  
Representa números inteiros ou de ponto flutuante.

    let idade = 25;
    let preco = 9.99;

**String (Texto)**:  
Sequência de caracteres entre aspas simples ou duplas.

    let nome = "João";
    let mensagem = 'Bem-vindo!';

**Boolean**:  
Representa um valor lógico verdadeiro ou falso.

    let aprovado = true;
    let maiorDeIdade = false;

**Undefined**:  
Representa uma variável que foi declarada, mas não atribuída a um valor.

    let cidade;

**Null**:  
Representa a ausência intencional de qualquer valor ou objeto.

    let carro = null;

**Object (Objeto)**:  
Coleção de pares chave-valor.

    let pessoa = {
        nome: "Maria",
        idade: 30,
        cidade: "São Paulo"
    };

**Array (Matriz)**:  
Objeto usado para armazenar vários valores em uma única variável.

    let frutas = ["maçã", "banana", "laranja"];

**Function (Função)**:  
Blocos de código reutilizável que podem ser chamados para realizar uma tarefa específica.

    function somar(a, b) {
        return a + b;
    }

## **Autoboxing**

Conceito relacionado, mas mais comumente encontrado em linguagens de programação como Java.  
No entanto, em JavaScript, também existe um fenômeno semelhante.  
O JavaScript tem tipos primitivos (como números, strings e booleanos) e tipos de objetos (como objetos, matrizes e funções), e às vezes ocorre uma conversão automática entre esses tipos primitivos e seus equivalentes de objeto.  
Isso é chamado de autoboxing.

Por exemplo, quando você chama métodos ou acessa propriedades em valores primitivos, o JavaScript automaticamente "empacota" o valor primitivo em um objeto temporário (autoboxing) para que você possa acessar os métodos ou propriedades.  
Quando a operação é concluída, o valor primitivo é automaticamente "desempacotado" de volta.  
Isso geralmente acontece de forma transparente para o desenvolvedor.

Por exemplo:

    let nome = "João";
    console.log(nome.length); // O comprimento da string é acessado através do autoboxing

## **Métodosg**

São funções que estão associadas a objetos.  
Eles permitem que você execute ações específicas em um objeto e podem ser acessados usando a notação de ponto.

Por exemplo, considere um objeto pessoa com um método dizerOla():

    let pessoa = {
        nome: "João",
        idade: 30,
        dizerOla: function() {
            console.log("Olá! Meu nome é " + this.nome);
        }
    };

    pessoa.dizerOla(); // Saída: Olá! Meu nome é João

Aqui, dizerOla() é um método que pertence ao objeto pessoa.

## **Métodos com strings**

**length**:  
Retorna o número de caracteres em uma string.

    let frase = "Olá, mundo!";
    console.log(frase.length); // Saída: 11

**charAt(index)**:  
Retorna o caractere na posição especificada pelo índice na string. O índice começa em 0.

    let palavra = "JavaScript";
    console.log(palavra.charAt(0)); // Saída: J
    console.log(palavra.charAt(4)); // Saída: S

**slice(start, end)**:  
Retorna uma parte da string, começando do índice start até (mas não incluindo) o índice end. Se end for omitido, extrai até o final da string.

    let frase = "Bom dia, mundo!";
    console.log(frase.slice(4, 7)); // Saída: dia
    console.log(frase.slice(8)); // Saída: mundo!

**split(separator)**:  
Divide uma string em um array de substrings, usando o separator como ponto de divisão. O separator pode ser um caractere específico ou uma expressão regular.

    let frase = "Olá, mundo!";
    let palavras = frase.split(" ");
    console.log(palavras); // Saída: ["Olá,", "mundo!"]

## **Como fazer comentários no código**

Os comentários são ignorados pelo interpretador JavaScript e são úteis para documentar seu código, explicar partes complexas, ou desativar temporariamente partes do código durante o desenvolvimento.

**Comentários de uma linha**:  
Utilize `//` para comentar uma única linha.

    // Este é um comentário de uma linha
    let nome = "João"; // Este comentário está ao lado de uma linha de código

**Comentários de várias linhas**:  
Utilize /\* \*/ para comentar várias linhas ou um bloco de código.

    /*
     Este é um comentário de várias linhas.
     Pode abranger várias linhas de código.
    */
    let idade = 30;

## **Operadores**

### **Operadores Aritméticos**

Usados para realizar operações matemáticas em números.

Adição (`+`): Soma dois valores.  
Subtração (`-`): Subtrai o segundo valor do primeiro.  
Multiplicação (`*`): Multiplica dois valores.  
Divisão (`/`): Divide o primeiro valor pelo segundo.  
Módulo (`%`): Retorna o resto da divisão inteira do primeiro valor pelo segundo.

    let soma = 10 + 5; // soma = 15
    let resto = 10 % 3; // resto = 1

### **Operadores de Atribuição**

Usados para atribuir valores a variáveis.

Atribuição (`=`): Atribui o valor à variável.  
Atribuição de Adição (`+=`): Adiciona o valor à variável.  
Atribuição de Subtração (`-=`): Subtrai o valor da variável.

    let x = 10;
    x += 5; // Agora x = 15

### **Operadores de Comparação**

Usados para comparar dois valores.

Igual a (`== ou ===`): Compara se dois valores são iguais.  
Diferente de (`!=` ou `!==`): Compara se dois valores são diferentes.

Maior que (`>`), Menor que (`<`), Maior ou igual a (`>=`), Menor ou igual a (`<=`): Comparam se um valor é maior, menor, maior ou igual, ou menor ou igual a outro.

    console.log(10 === "10"); // Saída: false (comparação estrita)
    console.log(10 == "10"); // Saída: true (comparação solta)

### **Operadores Lógicos**

Usados para combinar ou inverter valores booleanos.

E lógico (`&&`): Retorna true se ambos os operandos forem verdadeiros.  
Ou lógico (`||`): Retorna true se pelo menos um dos operandos for verdadeiro.  
Não lógico (`!`): Inverte o valor do operando.

    let x = 10;
    let y = 5;
    console.log(x > 5 && y < 10); // Saída: true

## \*\*Interação com usuário

### **Eventos de Mouse e Teclado**

Responder a eventos do mouse, como cliques, movimentos, passagens do mouse sobre elementos, e eventos do teclado, como pressionamentos de teclas.

    document.getElementById("meuBotao").addEventListener("click", function() {
        alert("Botão clicado!");
    });

### **Entrada do Usuário**

Coletar entrada do usuário por meio de campos de texto, caixas de seleção, botões de rádio e outras formas de entrada.

    <input type="text" id="meuCampo">
    <button onclick="mostrarValor()">Mostrar Valor</button>

    <script>
        function mostrarValor() {
            let valor = document.getElementById("meuCampo").value;
            alert("O valor é: " + valor);
        }
    </script>

### **Manipulação do DOM**

Alterar dinamicamente o conteúdo, estilo e estrutura do documento HTML para refletir as ações do usuário.

    document.getElementById("meuParagrafo").innerHTML = "Novo texto!";

### **Requisições AJAX**

Enviar solicitações assíncronas ao servidor para buscar ou enviar dados sem recarregar a página inteira.

    fetch("https://api.example.com/dados")
        .then(response => response.json())
        .then(data => console.log(data));

### **alert**

Exibe uma caixa de diálogo com uma mensagem e um botão "OK". É frequentemente usado para exibir mensagens informativas para o usuário.

Exemplo:

    alert("Olá! Bem-vindo ao nosso site!");

### **confirm**

Exibe uma caixa de diálogo com uma mensagem, um botão "OK" e um botão "Cancelar". É usado para obter a confirmação do usuário antes de realizar uma ação.

Exemplo:

    let confirmacao = confirm("Tem certeza de que deseja excluir este item?");
    if (confirmacao) {
        // Código para excluir o item
    } else {
        // Código para cancelar a exclusão
    }

Alert e confirm são úteis para interações simples com o usuário, como exibir mensagens de aviso, solicitar confirmação antes de executar uma ação crítica, etc.  
No entanto, eles têm limitações em termos de personalização e estilo, então em aplicações mais complexas, pode ser necessário usar bibliotecas ou frameworks para criar caixas de diálogo mais elaboradas.

### **Frameworks e Bibliotecas**

Utilizar bibliotecas como React, Vue.js ou Angular pode simplificar significativamente a interação com o usuário, fornecendo ferramentas e padrões para criar interfaces interativas de forma mais eficiente.

## **Estruturas de controle de fluxo**

### **Estrutura Simples**

É uma instrução de controle de fluxo que executa uma única ação. Geralmente é representada por uma única instrução condicional ou de repetição.

Exemplo de condicional simples (IF):

    let idade = 18;
    if (idade >= 18) {
        console.log("Você é maior de idade.");
    }

Exemplo de repetição simples (FOR):

    for (let i = 0; i < 5; i++) {
        console.log("Iteração: " + i);
    }

### **Estrutura Composta**

Consiste em um conjunto de instruções agrupadas em um bloco de código. Pode incluir múltiplas instruções condicionais ou de repetição.

**Condicional IF-ELSE**  
Usado para executar blocos de código se uma condição for verdadeira e outro bloco se a condição for falsa.

    let idade = 18;
    if (idade >= 18) {
        console.log("Você é maior de idade.");
    } else {
        console.log("Você é menor de idade.");
    }

### **Condicionais Aninhadas**

São condicionais dentro de outras condicionais. Permitem lidar com múltiplas condições de forma hierárquica.

Exemplo:

    let nota = 85;
    if (nota >= 90) {
        console.log("A");
    } else if (nota >= 80) {
        console.log("B");
    } else if (nota >= 70) {
        console.log("C");
    } else {
        console.log("D");
    }

### **Múltipla Escolha (Switch)**

Permite avaliar múltiplas condições de uma variável e executar blocos de código com base no valor da variável.

Exemplo:

    let diaDaSemana = 3;
    switch (diaDaSemana) {
        case 1:
            console.log("Segunda-feira");
            break;
        case 2:
            console.log("Terça-feira");
            break;
        // e assim por diante...
        default:
            console.log("Dia inválido");
    }

## **Laços de repetição**

### **WHILE**  
Executa um bloco de código enquanto a condição especificada for verdadeira.

    let contador = 0;
    while (contador < 5) {
        console.log("Contagem: " + contador);
        contador++;
    }

### **DO-WHILE**  
Similar ao while, mas garante que o bloco de código seja executado pelo menos uma vez, mesmo se a condição for falsa inicialmente.

    let contador = 0;
    do {
        console.log("Contagem: " + contador);
        contador++;
    } while (contador < 5);

### **FOR**
Utilizado quando você sabe exatamente quantas vezes deseja que um bloco de código seja executado.

    for (let i = 0; i < 5; i++) {
        console.log("Iteração: " + i);
    }
