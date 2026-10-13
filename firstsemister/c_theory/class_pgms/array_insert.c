#include<stdio.h>
int main()
{
    int numbers[5];
    int newData,index;
    for (int i = 0; i < 4; i++)
    {
        printf("input %d array element:",i+1);
        scanf("%d",&numbers[i]);
    }
    printf("enter the new element:");
    scanf("%d",&newData);
    printf("enter index value:");
    scanf("%d",&index);
    //insertion process to insert 'new data' at index 'index'
    numbers[4]=numbers[3];
    numbers[3]=numbers[2];
    numbers[2]=newData;
    for (int i = 0; i < 5; i++)
    {
      printf("%d",numbers[i]);
    }
}