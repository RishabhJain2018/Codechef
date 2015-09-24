#include<stdio.h>
int main()
{
int x;
float y;
scanf("%d%f",&x,&y);
if(x%5==0)
{
if((y-x-.5)>0)
printf("%f",(y-x-.5));
else
printf("%f",y);
}else
printf("%f",y);
return 0;
}
