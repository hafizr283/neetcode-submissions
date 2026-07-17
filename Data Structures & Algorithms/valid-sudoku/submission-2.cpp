class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n=9;
        int rows[10]={0},cols[10]={},squares[10]={};
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]=='.') continue;
                int value = board[i][j]-'0';
               
                if((1<<value)&rows[i] or (1<<value)&cols[j] or (1<<value)&squares[i/3*3+j/3]) return false;
                rows[i]|=(1<<value);
                cols[j]|=(1<<value);
                squares[i/3*3+j/3]|=(1<<value);

            }
        }
      
        return true;
    }
};
