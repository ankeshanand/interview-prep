
//#define DEBUG       //comment when you have to disable all debug macros.
#include <bits/stdc++.h>
using namespace std;

// Input macros
#define s(n)    scanf("%d",&n)
#define sc(n)   scanf("%c",&n)
#define sl(n)   scanf("%lld",&n)
#define sf(n)   scanf("%lf",&n)
#define ss(n)   scanf("%s",n)

//Pair macros
#define mp make_pair // useful for working with pairs
#define fi first
#define se second

#define ll long long int//data types used often, but you don't want to type them time by time_t

// Useful container manipulation / traversal macros
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back

#ifdef DEBUG
     #define debug(args...)            {cerr << #args << ": ";dbg,args; cerr<<endl;}
#else
    #define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> ii;
typedef vector<ii> vii;

vector<vii> adj;

vector<vi> AdjList;
/* DFS Implementation */
#define DFS_WHITE -1 // normal DFS, do not change this with other values (other than 0), because we usually use memset with conjunction with DFS_WHITE
#define DFS_BLACK 1
vi dfs_num;     // this variable has to be global, we cannot put it in recursion
void dfs(int u) {          // DFS for normal usage: as graph traversal algorithm
    printf(" %d", u);                                    // this vertex is visited
    dfs_num[u] = DFS_BLACK;      // important step: we mark this vertex as visited
    for (int j = 0; j < (int)AdjList[u].size(); j++) {
        int v = AdjList[u][j];                      // v is a (neighbor, weight) pair
        if (dfs_num[v] == DFS_WHITE)         // important check to avoid cycle
            dfs(v);      // recursively visits unvisited neighbors v of vertex u
    }
}

/* Djikstra Implementation */
vector<bool> mark;
vl d;
ll fast_dijkstra(int v, int target){
	fill(d.begin(),d.end(), INT_MAX);
	fill(mark.begin(), mark.end(), false);
	d[v] = 0;
	int u;
	priority_queue<pair<ll,int>,vector<pair<ll,int> >, greater<pair<ll,int> > > pq;
	pq.push({d[v], v});
	while(!pq.empty()){
		u = pq.top().second;
		pq.pop();
		if(mark[u])
			continue;
		mark[u] = true;
        if(u == target){
            return d[u];
        }
		for(auto p : adj[u]) //adj[v][i] = pair(vertex, weight)
			if(d[p.first] > d[u] + p.second){
				d[p.first] = d[u] + p.second;
				pq.push({d[p.first], p.first});
			}
	}
}



int main()
{
    
}

