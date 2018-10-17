#include<stdio.h>

//A basic program to find Transpose of a 3x3 matrix using C

int main()
{
	int mat[3][3],i,j,col,row,mat2[3][3];
	printf("\nEnter matrix elements : ");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
			scanf("%d",&mat[i][j]);
	}

	printf("\nThe matrix is :\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
			printf("%d ",mat[i][j]);
		printf("\n");
	}

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
			mat2[j][i]=mat[i][j];
	}

	printf("\nThe final matrix is : \n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
			printf("%d ",mat2[i][j]);
		printf("\n");
	}

	return 0;
}
