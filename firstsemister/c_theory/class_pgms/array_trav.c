#include<stdio.h>
int main()
{
    int arraysize=read_array_size();    //calling method and stores returned value
    int isvalid=validate_array_size(arraysize);    //passing 'arraysize',int array_size=arraysize
    if(isvalid==0)
}
int read_array_size()
{
    int size;
    printf("enter the size[>4]:");
    scanf("%d",size);
    return size;
}
int validate_array_size(int array_size)
{
 do
  {
    if (array_size>4)
    {
        return 1;
    }
    return 0;
  }
    while (array_size<5);
}
