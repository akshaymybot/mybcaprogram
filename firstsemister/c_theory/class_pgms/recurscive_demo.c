#include<stdio.h> 
int factorial(int number) 
{
    if (number == 0)
        return 1;
    return number * factorial(number - 1);
}
 
int main() 
{
    int number;
    int numbers[number];
    printf("enter the number:");
    scanf("%d",&number);
    for (int i = 0; i < number; i++)
    {
        printf("input %d array element:",i+1);
        scanf("%d",&numbers[i]);
    }
    
    printf("%d! = %d\n", number, factorial(number));
    return 0;
}