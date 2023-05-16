int maior ( int a , int b)
{
    if( a >= b)
        return(a);
    else
        return(b);
}

int modulo( int x   )
{
    if( x < 0 )
        return(x*(-1));
    else
        return(x);
}

int delta( int a , int b , int c)
{   int delta;
    delta = ( b*b) - (4*a*c);
    return(delta);
}

int tot_solucoes( int a , int b ,int c)
{   int wdelta;

    wdelta = delta( a , b , c );
    if ( wdelta > 0)
        return(2);
    if ( wdelta == 0)
        return(1);
    if ( wdelta <0)
        return(0);
}

int menor( int a , int b)
{
    if( a<b)
        return(a);
    if(a==b  )
        return(a);
    if( b<a)
        return(b);
}
