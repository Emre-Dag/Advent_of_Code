#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LINES 2000
#define MAX_LEN   10
int main()
{
	FILE* fp=NULL;
	fp = fopen ("aoc_input_day1.txt", "r");
	
	char input[ MAX_LEN ];                                                      
    char *line[ MAX_LINES ];
	int i,j,z;  
	int count=0;
	int count2=0;
	int count3=0;
	int buffer[MAX_LINES];
	
	for ( i=0; i<MAX_LINES && fgets(input, sizeof(input), fp ); ++i ) {     
        int lineLen=strlen(input) + 1;                                          
        line[i] = strncpy( malloc( lineLen ), input, lineLen );                 
    }                                                                           

    for ( j=0; j<i; ++j ) 
	{ 
		count++;
		if(count>=2)
		{
			buffer[j]=atoi(line[j]) + atoi(line[j-1]) + atoi(line[j-2]);
			printf( "Line %d:%d\n", j+1, buffer[j]);
		}
		free(line[j]); 
	}     
	for ( z=0; z<i; ++z ) 
	{ 
		count2++;
		if(count2>=1)
		{
			if(buffer[z]>buffer[z-1])
			{
				count3++;
			}
		}
	}   
	
	printf("count = %d",count3);
	fclose(fp);
	return 0;
}
