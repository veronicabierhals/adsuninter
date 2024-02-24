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

## **Interação com usuário**

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

## **Objetos**

São estruturas de dados fundamentais que permitem armazenar e organizar dados de forma mais complexa do que simples valores primitivos.  
Um objeto em JavaScript é uma coleção de pares chave-valor, onde cada chave (também chamada de propriedade) está associada a um valor.

Eles são extremamente versáteis e podem ser usados para representar praticamente qualquer estrutura de dados, desde dados simples até estruturas de dados complexas e até mesmo classes em orientação a objetos. Eles são essenciais para escrever código JavaScript eficiente e organizado.

    let pessoa = {
        nome: "João",
        idade: 30,
        cidade: "São Paulo"
    };

Neste exemplo, pessoa é um objeto com três propriedades: nome, idade e cidade, e cada propriedade está associada a um valor específico.

é possível acessar as propriedades de um objeto usando a notação de ponto (objeto.propriedade) ou a notação de colchetes (objeto["propriedade"]), como mostrado abaixo:

    console.log(pessoa.nome); // Saída: João
    console.log(pessoa["idade"]); // Saída: 30

Além disso, você pode adicionar novas propriedades a um objeto, modificar propriedades existentes e até mesmo excluir propriedades:

    pessoa.profissao = "Desenvolvedor";
    pessoa.idade = 31;
    delete pessoa.cidade;

Além das propriedades de valor simples, os objetos JavaScript também podem conter métodos, que são funções associadas ao objeto:

    let carro = {
        marca: "Toyota",
        modelo: "Corolla",
        ano: 2020,
        descricao: function() {
            return "Um " + this.marca + " " + this.modelo + " do ano " + this.ano;
        }
    };

    console.log(carro.descricao()); // Saída: Um Toyota Corolla do ano 2020

### **This**

A palavra-chave `this` é usada para se referir ao objeto atual em que um determinado código está sendo executado.  
O valor de this depende do contexto de execução e de como uma função é chamada.

**Dentro de um método de objeto**:  
Em um método de objeto, this se refere ao próprio objeto que contém o método.

    let pessoa = {
        nome: "João",
        saudacao: function() {
            return "Olá, eu sou " + this.nome;
        }
    };

    console.log(pessoa.saudacao()); // Saída: Olá, eu sou João

**Em uma função normal**:  
Quando uma função é chamada diretamente, this se refere ao objeto global (no navegador, geralmente é o objeto window). Se o modo estrito ("use strict") estiver ativado, this será undefined em vez de apontar para o objeto global.

    function exibirNome() {
        console.log("Meu nome é " + this.nome);
    }

    let pessoa = {
        nome: "Maria"
    };

    exibirNome(); // Saída (sem o modo estrito): Meu nome é undefined

**Call e Apply**:  
Os métodos call e apply permitem definir explicitamente o valor de this ao chamar uma função. Eles são frequentemente usados para chamar uma função em um contexto específico.

    function exibirNome(greeting) {
        console.log(greeting + ", meu nome é " + this.nome);
    }

    let pessoa = {
        nome: "Ana"
    };

    exibirNome.call(pessoa, "Olá"); // Saída: Olá, meu nome é Ana
    exibirNome.apply(pessoa, ["Oi"]); // Saída: Oi, meu nome é Ana

**Em arrow functions**:  
Em uma arrow function, this se comporta de forma diferente, ela não tem seu próprio this e se comporta como se estivesse capturando o this do contexto circundante.

    let pessoa = {
        nome: "Paulo",
        saudacao: () => {
            console.log("Olá, eu sou " + this.nome);
        }
    };

    pessoa.saudacao(); // Saída: Olá, eu sou undefined

Entender como this funciona é fundamental para escrever código JavaScript eficiente e sem bugs, especialmente ao lidar com objetos e funções.

## **Laço for... in**

Usado para iterar sobre as propriedades enumeráveis de um objeto. Ele percorre todas as propriedades próprias e enumeráveis de um objeto e de seus protótipos herdados.

Aqui está a sintaxe básica do for...in:

    for (variavel in objeto) {
        // código a ser executado para cada propriedade
    }

Por exemplo, vamos supor que temos o seguinte objeto pessoa:

    let pessoa = {
        nome: "João",
        idade: 30,
        cidade: "São Paulo"
    };

Podemos usar o for...in para iterar sobre as propriedades deste objeto:

    for (let propriedade in pessoa) {
        console.log(propriedade + ": " + pessoa[propriedade]);
    }

Este loop irá iterar sobre cada propriedade do objeto pessoa (como nome, idade e cidade) e imprimir o nome da propriedade seguido pelo seu valor.

É importante notar que o for...in também itera sobre as propriedades herdadas do protótipo do objeto. Para evitar isso, você pode usar hasOwnProperty() para verificar se a propriedade pertence ao próprio objeto:

    for (let propriedade in pessoa) {
        if (pessoa.hasOwnProperty(propriedade)) {
            console.log(propriedade + ": " + pessoa[propriedade]);
        }
    }

Isso garantirá que apenas as propriedades próprias do objeto pessoa sejam iteradas. O for...in é útil para situações em que você precisa iterar dinamicamente sobre as propriedades de um objeto, por exemplo, para realizar operações em todos os pares chave-valor de um objeto.

## **Arrays**

São estruturas de dados que permitem armazenar múltiplos valores em uma única variável.

Você pode criar um array literalmente, envolvendo os valores entre colchetes `[]`, separados por vírgulas.

    let numeros = [1, 2, 3, 4, 5];
    let frutas = ["maçã", "banana", "laranja"];

Para acessar elementos de um array usa-se a notação de colchetes [], com o índice do elemento desejado (os índices começam em 0).

    console.log(frutas[0]); // Saída: maçã
    console.log(numeros[2]); // Saída: 3

**Propriedade Length**:
A propriedade length retorna o número de elementos em um array.

    console.log(frutas.length); // Saída: 3

### **Métodos de Array**

`push()`: Adiciona um ou mais elementos ao final do array.

    let numeros = [1, 2, 3];
    numeros.push(4, 5);
    console.log(numeros); // Saída: [1, 2, 3, 4, 5]

`pop()`: Remove o último elemento do array e o retorna.

    let numeros = [1, 2, 3];
    let ultimoElemento = numeros.pop();
    console.log(ultimoElemento); // Saída: 3
    console.log(numeros); // Saída: [1, 2]

`shift()`: Remove o primeiro elemento do array e o retorna.

    let numeros = [1, 2, 3];
    let primeiroElemento = numeros.shift();
    console.log(primeiroElemento); // Saída: 1
    console.log(numeros); // Saída: [2, 3]

`unshift()`: Adiciona um ou mais elementos no início do array.

    let numeros = [2, 3];
    numeros.unshift(0, 1);
    console.log(numeros); // Saída: [0, 1, 2, 3]

`concat()`: Combina dois ou mais arrays.

    let numeros1 = [1, 2];
    let numeros2 = [3, 4];
    let numerosConcatenados = numeros1.concat(numeros2);
    console.log(numerosConcatenados); // Saída: [1, 2, 3, 4]

`splice()`: Adiciona ou remove elementos de um array.

    let numeros = [1, 2, 3, 4, 5];
    numeros.splice(2, 1); // Remove 1 elemento a partir do índice 2
    console.log(numeros); // Saída: [1, 2, 4, 5]

    numeros.splice(2, 0, 3); // Adiciona o número 3 no índice 2
    console.log(numeros); // Saída: [1, 2, 3, 4, 5]

`slice()`: Retorna uma cópia de parte do array.

    let numeros = [1, 2, 3, 4, 5];
    let parteDoArray = numeros.slice(2);
    console.log(parteDoArray); // Saída: [3, 4, 5]

`forEach()`: Executa uma função para cada elemento do array.

    let numeros = [1, 2, 3];
    numeros.forEach(function(numero) {
        console.log(numero);
    });
    // Saída:
    // 1
    // 2
    // 3

`map()`: Cria um novo array com o resultado de chamar uma função em cada elemento do array original.

    let numeros = [1, 2, 3];
    let quadrados = numeros.map(function(numero) {
        return numero * numero;
    });
    console.log(quadrados); // Saída: [1, 4, 9]

`filter()`: Cria um novo array com todos os elementos que passam em um teste especificado por uma função.

    let numeros = [1, 2, 3, 4, 5];
    let numerosPares = numeros.filter(function(numero) {
        return numero % 2 === 0;
    });
    console.log(numerosPares); // Saída: [2, 4]

`indexOf()`: Retorna o índice da primeira ocorrência de um elemento especificado em um array, ou -1 se o elemento não for encontrado.

    let frutas = ["maçã", "banana", "laranja", "banana", "uva"];
    let indiceBanana = frutas.indexOf("banana");
    console.log(indiceBanana); // Saída: 1

    let indiceAbacaxi = frutas.indexOf("abacaxi");
    console.log(indiceAbacaxi); // Saída: -1 (não encontrado)

`reverse()`: Inverte a ordem dos elementos em um array e retorna o array invertido.

    let numeros = [1, 2, 3, 4, 5];
    numeros.reverse();
    console.log(numeros); // Saída: [5, 4, 3, 2, 1]

## **Loop for...of**

Permite iterar sobre elementos de uma estrutura de dados iterável, como um array, de forma mais simples e legível do que as alternativas tradicionais, como o for convencional ou o forEach().

Sintaxe básica do for...of:

    for (variavel of iteravel) {
        // código a ser executado para cada elemento
    }

Por exemplo, vamos supor que temos o seguinte array de números:

    let numeros = [1, 2, 3, 4, 5];

Podemos usar o for...of para iterar sobre cada elemento deste array:

    for (let numero of numeros) {
        console.log(numero);
    }

Este loop irá iterar sobre cada número no array numeros e imprimir o valor de cada número.

## **Funções**

São blocos de código reutilizável que podem ser chamados para executar uma ação específica. Elas são fundamentais para organizar e reutilizar o código em seus programas. Aqui estão alguns conceitos importantes sobre funções em JavaScript:

Pode-se declarar uma função usando a palavra-chave `function`, seguida pelo nome da função e uma lista de parâmetros entre parênteses, se houver. O corpo da função é colocado entre chaves {}.

    function saudacao(nome) {
        console.log("Olá, " + nome + "!");
    }

Para executar uma função, você precisa chamá-la pelo seu nome, seguido por parênteses (). Se a função espera parâmetros, você precisa passá-los durante a chamada.

    saudacao("João"); // Saída: Olá, João!

### **Retorno de Valor (return)**

Uma função pode retornar um valor usando a palavra-chave `return`. Isso é útil quando você deseja obter um resultado específico do processamento da função.

    function soma(a, b) {
        return a + b;
    }

    let resultado = soma(3, 5);
    console.log(resultado); // Saída: 8

### **Funções Anônimas**

Você também pode criar funções sem nome, chamadas de funções anônimas. Elas são frequentemente usadas como argumentos para outras funções ou atribuídas a variáveis.

    let dobrar = function(x) {
        return x * 2;
    };

    console.log(dobrar(5)); // Saída: 10

### **Arrow Functions**

As arrow functions são uma sintaxe mais curta e concisa para declarar funções em JavaScript, introduzidas no ECMAScript 6 (ES6).

    let quadrado = (x) => {
        return x * x;
    };

    console.log(quadrado(3)); // Saída: 9

### **Escopo de Variáveis**

As variáveis declaradas dentro de uma função são locais para essa função e não podem ser acessadas fora dela, a menos que sejam explicitamente retornadas. Isso é conhecido como escopo de função.

### **Parâmetros Default**

Pode-se definir valores padrão para os parâmetros de uma função, que serão usados se nenhum valor for fornecido durante a chamada da função.

    function saudacao(nome = "mundo") {
        console.log("Olá, " + nome + "!");
    }

    saudacao(); // Saída: Olá, mundo!

### **Recursividade**

Uma função pode chamar a si mesma repetidamente até atingir uma condição de parada. É possível usar a recursividade para resolver problemas que podem ser divididos em subproblemas semelhantes.

    function contarAteDez(numero) {
        if (numero <= 10) {
            console.log(numero);
            contarAteDez(numero + 1); // Chama a função novamente com o próximo número
        }
    }

    contarAteDez(1); // Chama a função pela primeira vez com 1 como argumento inicial

Neste exemplo, a função contarAteDez imprime os números de 1 a 10. Quando a função é chamada, ela verifica se o número é menor ou igual a 10. Se for, imprime o número e chama a si mesma com o próximo número como argumento. Este processo continua até que a condição de parada (número > 10) seja atingida.

A recursividade é frequentemente usada para resolver problemas que podem ser divididos em casos base e casos recursivos.  
Um caso base é a condição que indica quando a função deve parar de se chamar a si mesma. Se não houver um caso base, a função continuará chamando a si mesma indefinidamente, resultando em um estouro de pilha (stack overflow).

É importante ter cuidado ao usar recursividade, pois ela pode consumir muita memória e tempo de execução se não for implementada corretamente. Além disso, é essencial garantir que haja uma condição de parada para evitar loops infinitos. No entanto, quando usada corretamente, a recursividade pode ser uma ferramenta poderosa para resolver problemas complexos de forma elegante e concisa.

## **Objeto date**

Usado para trabalhar com datas e horas. Ele fornece métodos para criar, manipular e formatar datas de várias maneiras. 

**Criando uma nova instância de Date**:  

Você pode criar uma nova instância de Date usando o construtor ``new Date()``. Se não passar nenhum argumento, ele retornará a data e hora atuais.

    let dataAtual = new Date();
    console.log(dataAtual); // Saída: Data e hora atuais

**Passando argumentos para criar uma data específica**:  

É possível passar argumentos para o construtor Date para criar uma data específica. Os argumentos incluem ano, mês (começando de 0 para janeiro), dia, hora, minuto, segundo e milissegundo.

    let dataEspecifica = new Date(2023, 0, 1); // 1º de janeiro de 2023
    console.log(dataEspecifica); // Saída: Sun Jan 01 2023 00:00:00 GMT-0500 (Eastern Standard Time)

### **Métodos date**

``get/setFullYear()``: Obtém ou define o ano da data.

    let data = new Date();
    let ano = data.getFullYear(); // Obtém o ano atual
    data.setFullYear(2025); // Define o ano para 2025

``get/setMonth()``: Obtém ou define o mês da data (0-11).

    let data = new Date();
    let mes = data.getMonth(); // Obtém o mês atual
    data.setMonth(5); // Define o mês para junho (5)

``get/setDate()``: Obtém ou define o dia do mês da data (1-31).

    let data = new Date();
    let dia = data.getDate(); // Obtém o dia do mês atual
    data.setDate(15); // Define o dia do mês para o dia 15

``get/setHours()``: Obtém ou define a hora da data (0-23).

    let data = new Date();
    let hora = data.getHours(); // Obtém a hora atual
    data.setHours(15); // Define a hora para 15 (3 PM)

``get/setMinutes()``: Obtém ou define os minutos da data (0-59).

    let data = new Date();
    let minutos = data.getMinutes(); // Obtém os minutos atuais
    data.setMinutes(30); // Define os minutos para 30

``get/setSeconds()``: Obtém ou define os segundos da data (0-59).

    let data = new Date();
    let segundos = data.getSeconds(); // Obtém os segundos atuais
    data.setSeconds(45); // Define os segundos para 45

``get/setMilliseconds()``: Obtém ou define os milissegundos da data (0-999).

    let data = new Date();
    let milissegundos = data.getMilliseconds(); // Obtém os milissegundos atuais
    data.setMilliseconds(500); // Define os milissegundos para 500

``getTime()``: Retorna o número de milissegundos desde 1º de janeiro de 1970 00:00:00 UTC.

    let data = new Date();
    let milissegundosDesde1970 = data.getTime();

``getDay()``: Retorna o dia da semana para a data (0-6, onde 0 representa Domingo, 1 Segunda-feira, e assim por diante).

    let data = new Date();
    let diaDaSemana = data.getDay(); // Obtém o dia da semana atual

### **Formatando datas**
O objeto Date não possui um método direto para formatar datas, mas você pode criar sua própria função de formatação ou usar bibliotecas externas como o moment.js para isso.

### **Manipulação de datas**
Você pode usar métodos como setFullYear(), setMonth(), setDate(), setHours(), setMinutes(), setSeconds(), setMilliseconds() para alterar componentes específicos de uma data.

    let data = new Date();
    data.setFullYear(2025);
    console.log(data); // Saída: Data e hora atual com o ano alterado para 2025

## **Browser Object Model (BOM)**

É uma parte do ambiente de execução do navegador que fornece objetos e métodos para interagir com o navegador em si, incluindo a janela do navegador, o histórico de navegação, os cookies e outros recursos relacionados ao navegador.

### **Objeto Window**

O objeto window representa a janela do navegador. Ele contém métodos e propriedades para controlar o navegador e manipular o documento exibido.

### **Closed**

A propriedade ``closed`` do objeto window indica se a janela do navegador está fechada ou não. Ela retorna true se a janela estiver fechada e false se estiver aberta.

    if (window.closed) {
        console.log("A janela está fechada.");
    } else {
        console.log("A janela está aberta.");
    }

### **Document**

O objeto ``document`` representa o conteúdo da página HTML carregada na janela do navegador. Ele fornece métodos para acessar e manipular elementos HTML na página.

    let titulo = document.title; // Obtém o título da página
    let paragrafos = document.getElementsByTagName("p"); // Obtém todos os parágrafos na página

### **History**

O objeto ``history`` contém o histórico de navegação do navegador. Ele fornece métodos para navegar para páginas anteriores ou posteriores no histórico.

    history.back(); // Navega para a página anterior no histórico
    history.forward(); // Navega para a próxima página no histórico

### **Open e Close**

Os métodos ``open()`` e ``close()`` do objeto window são usados para abrir e fechar novas janelas do navegador, respectivamente.

    let novaJanela = window.open("https://www.example.com", "_blank"); // Abre uma nova janela
    novaJanela.close(); // Fecha a nova janela

### **Onload**

O evento onload é acionado quando um documento HTML e todos os recursos associados a ele (como imagens e estilos) foram carregados completamente.

    <script>
        window.onload = function() {
            console.log("O documento foi completamente carregado.");
        };
    </script>

Exemplo de Aplicabilidade Prática:

Um exemplo de aplicação prática do BOM seria a criação de um botão que, quando clicado, abre uma nova janela do navegador para exibir um site específico:

    html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Open New Window</title>
    </head>
    <body>
        <button onclick="abrirJanela()">Abrir Nova Janela</button>

        <script>
            function abrirJanela() {
                window.open("https://www.example.com", "_blank");
            }
        </script>
    </body>
    </html>

Neste exemplo, quando o botão é clicado, a função ``abrirJanela()`` é chamada, que por sua vez chama o método ``window.open()`` para abrir uma nova janela do navegador para o site "https://www.example.com". Isso demonstra como você pode usar os recursos do BOM para interagir com o navegador e criar experiências de usuário mais ricas e interativas.

## **Document Object Model (DOM)**

É uma interface de programação de aplicações (API) para documentos HTML, XML e SVG. Ele representa a estrutura hierárquica de um documento web e fornece métodos e propriedades para interagir com os elementos do documento.

``getElementById()``  

É usado para obter uma referência a um elemento HTML com base no valor de seu atributo id.

    let meuElemento = document.getElementById("meuId");

``getElementsByTagName()``  

É usado para obter uma coleção de elementos HTML com base no nome da tag.

    let paragrafos = document.getElementsByTagName("p");

``getElementsByClassName()``  

É usado para obter uma coleção de elementos HTML com base no valor de sua classe.

    let elementos = document.getElementsByClassName("minhaClasse");

``querySelector()``

É usado para selecionar o primeiro elemento HTML que corresponde a um seletor CSS especificado.

    let primeiroParagrafo = document.querySelector("p");

``querySelectorAll()``  

É usado para selecionar todos os elementos HTML que correspondem a um seletor CSS especificado, retornando uma NodeList.

    let todosParagrafos = document.querySelectorAll("p");

``textContent``  

É usada para obter ou definir o conteúdo de texto de um elemento HTML.

    let meuElemento = document.getElementById("meuId");
    let texto = meuElemento.textContent; // Obtém o conteúdo de texto
    meuElemento.textContent = "Novo texto"; // Define um novo conteúdo de texto

``innerHTML``  

É usada para obter ou definir o conteúdo HTML de um elemento HTML.

    let meuElemento = document.getElementById("meuId");
    let html = meuElemento.innerHTML; // Obtém o conteúdo HTML
    meuElemento.innerHTML = "<strong>Novo</strong> conteúdo"; // Define um novo conteúdo HTML

``element.style``  

A propriedade style de um elemento HTML é usada para obter ou definir estilos CSS inline para o elemento.

    let meuElemento = document.getElementById("meuId");
    meuElemento.style.color = "red"; // Define a cor do texto para vermelho
    meuElemento.style.backgroundColor = "yellow"; // Define a cor de fundo para amarelo

## **Eventos**

São ações que ocorrem em elementos HTML, como cliques do mouse, movimentos do mouse, pressionamentos de teclas, carregamento da página, etc. 

**click:**
acionado quando um elemento é clicado com o mouse.

**dblclick:**
acionado quando um elemento é clicado duas vezes rapidamente com o mouse.

**mousedown:**
 acionado quando um botão do mouse é pressionado enquanto o cursor está sobre um elemento.

**mouseover:**
acionado quando o cursor do mouse entra na área de um elemento.

**mouseout:**
acionado quando o cursor do mouse deixa a área de um elemento.

**mousemove:**
acionado quando o cursor do mouse se move sobre um elemento.

*load:*
acionado quando a página da web é totalmente carregada, incluindo todos os seus recursos (imagens, estilos, scripts, etc.).

**unload:**
acionado quando a página da web está prestes a ser descarregada (quando o usuário navega para outra página ou fecha a janela do navegador).

**scroll:**
acionado quando o usuário rola a página para cima ou para baixo.

**focus:**
acionado quando um elemento recebe foco, como um campo de entrada de texto.  

Esses são apenas alguns exemplos de eventos em JavaScript.  
Para lidar com esses eventos, pode-se usar o método ``addEventListener()``, que permite que associe uma função de retorno de chamada (callback) a um evento em um elemento específico.  

Exemplo de uso do addEventListener() para lidar com o evento de clique:

    let meuElemento = document.getElementById("meuId");

    meuElemento.addEventListener("click", function() {
        console.log("O elemento foi clicado!");
    });

Neste exemplo, quando o elemento com o ID "meuId" é clicado, a mensagem "O elemento foi clicado!" será exibida no console.  
Você pode substituir "click" por qualquer outro evento que desejar lidar. Isso permite que você crie interações dinâmicas e responsivas em suas páginas web usando JavaScript.

