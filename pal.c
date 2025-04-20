#include<stdio.h>
#include<string.h>

char pal(char str, int len)
{
     char temp[20];
     for(int i=0, j=len-1; i<len, j>=0; i++, j--)
     {
         temp[i] = str[j]
     }
     
     if(str == temp)
     {
         printf("pallindrome\n");
     }
     else
     printf("not pallindrome\n");
}
int main()
{
    int len=0;
     char str[20];
     printf("Enter the string : ");
     scanf("%[^\n]", str);
     
     len=strlen(str);
     
     pal(str,len);
     
}