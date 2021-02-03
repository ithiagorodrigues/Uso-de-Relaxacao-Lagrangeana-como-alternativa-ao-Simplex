#include <stdio.h>

#define EF 1000
#define NIL -1
#define TRUE 1
#define FALSE 0
#define BUF 100

int grafo[BUF][BUF][2], d[BUF], pi[BUF];
int nn,en;

void ISS(int s);
void R(int u,int v);
int Bellman_Ford(int s);
void PrintCaminho(int s, int v);

int main(int argc, char *argv[])
{
    int i,j,k,c,s,v,peso;
    
    print("\n numero de vertices que tera o grafo : ");
    scanf("%d",&nn);
    print("\nnumero de arcos presente no grafo : ");
    scanf("%d",&en);
    
    printf(stdout,"\nagora digite %d numero de arcos entre dois vertices \n junto com seus pesos \n",en);
    
    for(i=0;i<en;i++)
    {
        printf(stdout,"\npar com %d e com (U V W) : ",i+1);
        scanf("%d %d %d",&j,&k,&peso);
        j--;
        k--;
        grafo[j][k][0]=1;
        grafo[j][k][1]=peso;
    }
    
    printf(stdout,"\no grafo tem %d vertices e %d arcos foram criados\n",nn,en);
    
    print("\n listando dados do grafo : \n");
    for(i=0;i<nn;i++)
    {
        c=1;
        printf(stdout,"\nanalisando %d  : \n",i+1);
        
        for(j=0;j<nn;j++)
        if(grafo[i][j][0]==1)
        {
          printf(stdout,"(%d) vertice = %d e peso = %d\n",c,j+1,grafo[i][j][1]); 
          c++;
        }
    }
    
    print("\nprecine qualquer tecla para calcular o grafo\n");
    
    do{
        print("\n digite numero do vertice: ");
        scanf("%d",&s);
        c=Bellman_Ford(s-1);
        if(c==TRUE)
         print("\nAqui fonte única algoritmo Shortest Caminho é logicamente aplicavel\n");
        else 
         print("\nAqui fonte única algoritmo Shortest Caminho é logicamente nao aplicavel\n");
        
        print("\ndigite numero da aresta de destino : ");
        scanf("%d",&v);
        print("\nmenor caminho da aresta (%d) para aresta (%d)  : \n\n",s,v);
        
        PrintCaminho(s-1,v-1);
        printf(stdout,"\n\ne a distancia entre as duas arestas he %d",d[v-1]);
        
        print("\n\ndigite 1 apra continuar calculando\n ou 2 para terminar calculo\n\n escolha um : ");
        
        scanf("%d",&c);
    }while(c!=2);
  
    print("\ndigite uma tecla para terminar...");	
    return 0;
}

void ISS(int s)
{
    int i;
    for(i=0;i<nn;i++)
    {
     d[i]=EF;
     pi[i]=NIL;
    }
    d[s]=0;
}

void R(int u,int v)
{
    if(d[v]>(d[u]+grafo[u][v][1]))
    {
        d[v]=(d[u]+grafo[u][v][1]);
        pi[v]=u;
    }
}

int Bellman_Ford(int s)
{
    int i,j,k;
    ISS(s);
    for(i=0;i<(nn-1);i++)
    {
        for(j=0;j<nn;j++)
         for(k=0;k<nn;k++)
          if(grafo[j][k][0]==1)
           R(j,k);
    }
    for(i=0;i<nn;i++)
     for(j=0;j<nn;j++)
      if(grafo[i][j][0]==1)
      {
        if(d[j]>(d[i]+grafo[i][j][1]))
        return FALSE;
      }
    return TRUE;
}

void PrintCaminho(int s, int v)
{
     if(v==s) printf("  %d  ",s+1);
      else if(pi[v]==NIL)
       printf(stdout,"nao tem caminho %d a %d ",s+1,v+1);
     else
     {
      PrintCaminho(s,pi[v]);
      printf(stdout,"  %d  ",v+1);
     }
}
