#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE 256
 
int main(int argc, char **argv)
{
    FILE *fp, *out;
    char sLine[MAX_LINE];
    int lineno = 0, flag = 0;
 
    if ((fp = fopen("bbb.txt", "r")) == NULL)
    {
        fprintf(stderr, 
            "Unable to open file %s, maybe it's not exist!\n", "bbb.txt");
        exit(-1);
    }
    if ((out = fopen("output.txt", "w")) == NULL)
    {
        fprintf(stderr, 
            "Unable to open file outfile.txt!\n");
        exit(-2);
    }
 
    while (fgets(sLine, MAX_LINE, fp))
    {
        ++lineno;
        if (strstr(sLine, "ben"))
        {
            //在终端显示
            printf( "%d: %s\n", lineno, sLine );
 
            //输出到outfile.txt
            fprintf( out, "%d: %s\n", lineno, sLine );
 
            flag = 1;
        }
    }
     
    if (0 == flag)
    {
        fprintf(stderr, "Unable to find \"%s\" in %s\n", "ben", "bbb.txt");
        rewind(fp);
    }
 
    return 0;
}
