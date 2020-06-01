#define MAX_VERTICES 100

typedef struct {
	int y;
	int yWeight;
	int weight;
	struct edgenode *next;
} edgenode;

typedef struct {
	edgenode *edges[MAX_VERTICES];
	int degree[MAX_VERTICES + 1];
	int nVertices;
	int nEdges;
} graph;