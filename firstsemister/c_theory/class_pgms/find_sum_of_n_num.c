#include<stdio.h>
int main()
{
    int n,sum,num,ns;
    printf("enter the value of n");
    scanf("%d",n);
if (n>5)
{
    for (int i = 0; i < n ; i++)
    {
        ns=i;
        sum=i+1;
        num=ns+sum;

    }
    printf("%d",num);
}
else
{
    printf("invalid input");
}
    }
    
