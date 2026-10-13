#include<stdio.h>
int main(void)
{
  char name[30]="ravi kumar";
  char word[]="program";
  printf("hello ");
  printf("%s",name,"\n");
  for (int i = 0;word[i]!='\0'; i++)
  {
    printf("word[%d]=%c\n",i,word[i]);
  }
  

}