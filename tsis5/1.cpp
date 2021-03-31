#include <bits/stdc++.h>
#define pb push_back
#define sz size()

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <long long> vll;

const int MOD = 1e9 + 7;
const int maxn = 2e5 + 7;
bool dp[maxn][7];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    string s, t;
    cin >> s >> t;
    dp[n][0] = true;
    dp[n][((int)s[n - 1] - 0) % 7] = true;
    for(int i = n - 2; i >= 0; i--){
        // int r = 1 * pow(10, (n - 1 - i) % 6) % 7;
        int r = ((int)s[i] - '0') * (int)pow(10, (n - 1 - i) % 6) % 7;
        for(int j = 0; j < 7; j++){
            if(t[i] == 'T'){
                dp[i + 1][j] = (dp[i + 2][(7 + j - 10 * r % 7) % 7] || dp[i + 2][j]);
                // dp[i][j] = dp[i + 1][j];
            }
            else{
                dp[i + 1][j] = (dp[i + 2][(7 + j - 10 * r % 7) % 7] && dp[i + 2][j]);
            }
        }
    }
    if(dp[1][0])cout << "Takahashi\n";
    else cout << "Aoki\n";
    return 0;
}