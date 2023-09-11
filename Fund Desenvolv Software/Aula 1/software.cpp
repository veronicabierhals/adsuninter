#include <stdio.h>
#include <stdlib.h>

/*obter notas
calcular media
verificar se aluno foi reprovado ou não
se media >= 7 aprovado
se não reprovado*/

int main(void)
{
    // declaração de variável
    float nota1, nota2, media;

    // obter as notas
    printf("Digite a primeira nota:");
    scanf("%f", &nota1);

    printf("Digite a primeira nota:");
    scanf("%f", &nota2);

    // calcular a media
    media = (nota1 + nota2) /2;

    // verificar se foi aprovado
    if (media >= 7)
        printf("Aprovado");
    else
        printf("Reprovado");
    return 0;
}