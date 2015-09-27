
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
typedef pair<int, int> ii;


int n_sols = 0;

bool is_safe(vector<vector<int> > board, int row, int col, int N){
    //check horizontal row
    REP(i, col){
        if(board[row][i])
            return false;
    }
    // check upper diagonal
    int a = row-1, b = col-1;
    while(a >=0 && b >=0){
        if(board[a][b])
            return false;
        a--;b--;
    }

    // check lower diagonal
    a = row+1, b = col-1;
    while(a < N && b >= 0){
        if(board[a][b])
            return false;
        a++;b--;
    }
    return true;
}

void solveNQUtil(vector<vector<int> > board, int col, int N){
    if(col == N){
        n_sols += 1;
        return;
    }
    REP(i, N){
        if(is_safe(board, i, col, N)){
            board[i][col] = 1;
            solveNQUtil(board, col+1, N);
            board[i][col] = 0; // backtrack
        }
    }
    return;
}

void solveNQ(int N){
    vector<vector<int> > board(N, vector<int> (N,0));
    solveNQUtil(board, 0, N);
}

int main()
{
    int N = 8;
    solveNQ(N);
    cout << n_sols << endl;
}

