#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

void swap( int *i , int *j)
{
    int temp;
    temp = *i;
    *i = *j;
    *j = temp;
}

int main (void)
{
    int a=5, b= 10;
    printf("\n\n\n");
    printf ("   a= %d   b=%d ", a ,b );
    printf("\n\n\n");
    swap( &a , &b);
    printf ("   a= %d   b=%d ", a ,b );
    printf("\n\n\n");
    return(0);
}
