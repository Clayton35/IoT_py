#include<stdio.h>

int main()
{
	int numCount = 0;
	int input;
	int itrCount;
	float sum = 0;
	
	printf("How many numbers will you enter? ");
	scanf("%d", &itrCount);
	
	while (numCount < itrCount)
	{
		printf("\nPlease enter a number: ");
		scanf("%d", &input);
		
		(sum += input);
		printf("Your current sum: %.2f\n", sum);
		
		numCount++;
	}
	
	float average = (sum / itrCount);
	
	printf("\nYour total sum: %f\n", sum);
	printf("Your average: %.2f\n", average);
	
	return 0;
}
