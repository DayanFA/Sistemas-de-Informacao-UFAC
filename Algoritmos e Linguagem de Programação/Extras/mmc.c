/*
Programa.: ufacEXTRA.5
Proposito: Algoritmo que fa�a mmc.
Ultima atualiza��o: 26/02/2023 Hora: 22:00
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a,b,aux1,aux2,aux3;
    printf("Entre com o primeiro n�mero(diferente de 0): ");
    scanf("%d", &a);
    printf("Entre com o segundo n�mero(diferente de 0): ");
    scanf("%d", &b);
    aux2=a;
    aux3=b;
    while (aux3 != 0)
    {
        aux1=aux2%aux3;
        aux2=aux3;
        aux3=aux1;
    }
    aux2=(a*b)/aux2;
    printf("O MMC de %d e %d � %d\n", a, b, aux2);
    return 0;
}
