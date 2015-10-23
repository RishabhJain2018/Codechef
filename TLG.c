#include <stdio.h>
int main()
{
	int n,flag,i;
	int a,b,lead,c,d;
	scanf("%d",&n);
	a=0;
	b=0;
	lead=0;
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&c,&d);
		a+=c;
		b+=d;
		if(a>b && a-b>lead)
		{
			flag=1;
			lead=a-b;
		}
		else if (b>a && b-a>lead)
		{
			flag=2;
			lead=b-a;
		}
	}
	printf("%d %d",flag,lead);
	return 0;

}
