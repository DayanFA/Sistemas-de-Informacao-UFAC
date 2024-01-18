pchisq(q=3,df=9)
amostra= rnorm(n=20,mean=100,sd=15)
amostra
s2 = var(amostra)
s2
xinf=qchisq(p=0.025,df=19)
xinf
xsup=qchisq(p=0.975,df=19)
xsup
n=length(amostra)
n
LI=(n-1)*s2/xsup
LS=(n-1)*s2/xinf
LI;LS
sqrt(LI);sqrt(LS)
