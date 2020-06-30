class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> perm;
        for (int i = 0; i < n; i++) perm.push_back(i+1);
        while (k-- > 1) next_permutation(perm.begin(), perm.end());
        string ans;
        for (int i = 0; i < n; i++) ans += to_string(perm[i]);
        return ans;
    }
};