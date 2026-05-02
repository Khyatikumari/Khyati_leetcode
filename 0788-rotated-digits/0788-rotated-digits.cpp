class Solution {
public:
    int memo[12][2][2];
    string S;
    int dp(int pos,bool tight,bool is_diff)
    {
        if(pos==S.size())return is_diff; 
        if(memo[pos][tight][is_diff] != -1)return memo[pos][tight][is_diff];

        int res=0;
        int limit=tight ? S[pos]-'0' : 9;

        for(int d=0;d<=limit; d++) {
            if(d==3 || d == 4 || d == 7)continue;
            bool next_diff=is_diff ||(d == 2 || d == 5 || d == 6 || d == 9);
            res+=dp(pos+1, tight && (d==limit), next_diff);
        }
        return memo[pos][tight][is_diff] = res;
    }
    int rotatedDigits(int n){
        S=to_string(n);
        memset(memo, -1, sizeof(memo));
        return dp(0,true,false);
    }
};