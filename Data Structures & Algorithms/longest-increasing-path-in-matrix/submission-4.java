class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        
        return longestI(matrix);
    }
    private int longestI(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int[][] out = new int[row][col];
        int[][] dir = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                for (int[] x : dir) {
                    int xi = i + x[0];
                    int xj = j + x[1];
                    if (xi < row && xi >= 0 && xj < col && xj >= 0 && matrix[xi][xj] > matrix[i][j])
                        out[i][j]++;
                }
            }
        }
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (out[i][j] == 0)
                    q.offer(new int[] {i, j});
            }
        }
        int len = 0;
        while (!q.isEmpty()) {
            len++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] x = q.peek();
                q.poll();

                for (int[] dx : dir) {
                    int xi = x[0] + dx[0];
                    int xj = x[1] + dx[1];
                    if (xi < row && xi >= 0 && xj < col && xj >= 0
                        && matrix[xi][xj] < matrix[x[0]][x[1]]) {
                        out[xi][xj]--;
                        if (out[xi][xj] == 0)
                            q.offer(new int[] {xi, xj});
                    }
                }
            }
        }
        return len;
    }
}
