#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define maxn 16000

int main(int argc, char *argv[]){

	int index = atoi(argv[1]);
	int modo = atoi(argv[2]);
	static double mat[maxn][maxn];
	static double veten[maxn];
	static double vetas[maxn];
	clock_t start, stop;
	double totaltime;


	srand(time(NULL));




	int i,j;
	for (i=0; i<index;i++){
		veten[i]=(double)rand();
		for (j=0;j<index; j++){
			mat[i][j]=(double)rand();
		}
	}


	if (modo == 0){
		start = clock();
		for (i=0; i<index;i++){
	                vetas[i]=0;
        	        for (j=0;j<index; j++){
                	        vetas[i]+=veten[j]*mat[i][j];
			}
		}
		stop = clock();
		totaltime = (double)(stop - start) / CLOCKS_PER_SEC;
		printf("%d : %f \n", index, totaltime);
	}

	if (modo == 1){
		start = clock();
		for (i=0; i<index;i++){
			vetas[i]=veten[0]*mat[i][0];
		}
                for (j=1; j<index;j++){
                        for (i=0;i<index; i++){
                                vetas[i]+=veten[j]*mat[i][j];
                        }
                }
                stop = clock();
                totaltime = (double)(stop - start) / CLOCKS_PER_SEC;
		printf("%d : %f \n", index, totaltime);

        }



//int row, columns;
//for (row=0; row<index; row++)
//{
//    for(columns=0; columns<index; columns++)
//    {
//         printf("%f     ", mat[row][columns]);
//    }
//    printf("\n");
//}
//
//    for(columns=0; columns<index; columns++)
//    {
//         printf("%f     ", veten[columns]);
//    }
//
//    for(columns=0; columns<index; columns++)
//    {
//         printf("%f     ", vetas[columns]);
//    }

	return 0;
}

