#include<stdio.h>
int get_array_sum(int number[])
{
     int sum;
     for (int i = 0; i < 5; i++)
     {
        sum+=number[i];
     }
     return sum;
 }
int main() 
{
    int numbers[5];
    for (int i = 0; i < 5; i++)
    {
        printf("input %d array element:",i+1);
        scanf("%d",&numbers[i]);
    }
    //calculate and returns the sum
   int total= get_array_sum(numbers);
   printf("the sum is:%d",total);
}