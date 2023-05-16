#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>
#include <C:\Header\bibli.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int a,b,c,x;
    a=1;
    b=0;
    c=7;
    x = tot_solucoes( a , b, c);
    printf("\n\n\n");
    printf("   Total de soluções: %d" , x);
    printf("   Delta = %d" , delta(a,b,c)   );
    getch();
}
