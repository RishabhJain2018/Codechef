#include <stdio.h>
int main()
{
	int n,k,i,l=0;
	long int j;
	scanf("%d %d",&n,&k);
	for(i=0;i<n;i++)
	{
		scanf("%ld",&j);
		if(j%k == 0)
		l++;

	}
	printf("%d",l);
	return 0;
}