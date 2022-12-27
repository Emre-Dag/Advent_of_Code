#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LINES 2000
#define MAX_LEN   50
int main()
{
	FILE* fp=NULL;
	fp = fopen ("aoc_input_day2.txt", "r");
	
	char input[ MAX_LEN ];                                                      
    char *line[ MAX_LINES ];
	int depth=0;
	int horizontal=0;
	int i;  
	

    for ( i=0; i<MAX_LINES && fgets(input, sizeof(input), fp ); ++i ) 
	{
		int lineLen=strlen(input) + 1;
		line[i] = strncpy( malloc( lineLen ), input, lineLen ); 
		char lastvalue = input[lineLen];
		
		if(input[0]=='f')
		{
			horizontal += atoi(&lastvalue);
			printf("Forward = %d\n",atoi(&lastvalue));
		}
		else if(input[0]=='d')
		{
			depth += atoi(&lastvalue);
			printf("Down = %d\n",atoi(&lastvalue));
		}
		else if(input[0]=='u')
		{
			depth -= atoi(&lastvalue); 
			printf("Up = %d\n",atoi(&lastvalue));
		}
		
		free(line[i]); 
	}     
	
	
	printf("\n#horizontal = %d",horizontal);
	printf("\n#depth = %d\n",depth);
	fclose(fp);
	return 0;
}
