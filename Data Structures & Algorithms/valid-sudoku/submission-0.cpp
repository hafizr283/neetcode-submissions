class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n=9;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cout<<board[i][j]<<' ';
            }
            cout<<endl;
        }
        for(int i=0;i<n;i++){
            unordered_map<char,int>mp1;
            unordered_map<char,int>mp2;
            
            for(int j=0;j<n;j++){
                mp1[board[i][j]]++;
                mp2[board[j][i]]++;
                if(board[i][j]!='.' and mp1[board[i][j]]>1) return false;
                if(board[j][i]!='.' and mp2[board[j][i]]>1) return false;
            }
            
        }
        for(int i=0;i<n;i+=3){
            for(int j=0;j<n;j+=3){
                unordered_map<char,int>mp;
                for(int ii=i;ii<i+3;ii++){
                    for(int jj=j;jj<j+3;jj++){
                        mp[board[ii][jj]]++;
                        if(board[ii][jj]!='.' and mp[board[ii][jj]]>1) return false;
                    }
                }
            }
        }
        return true;
    }
};
