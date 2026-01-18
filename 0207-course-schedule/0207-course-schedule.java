class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Queue<Integer> q = new LinkedList<>();
        ArrayList<ArrayList<Integer>> AdjList = new ArrayList<>();
        int[] indeg = new int[numCourses];
        int[] p = new int[numCourses];
        Arrays.fill(p, -1);
        
        for (int i = 0; i < numCourses; i++) {
            AdjList.add(new ArrayList<Integer>());
        }
        
        for (int[] edge : prerequisites) {
            indeg[edge[0]] += 1;
            AdjList.get(edge[1]).add(edge[0]);
            if (edge[0] == edge[1]) {
                return false;
            }
        }
        
        for (int i = 0; i < numCourses; i++) {
            AdjList.get(i).sort(null);
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (indeg[i] == 0) {
                q.add(i);
            }
        }
        
        while (q.size() > 0) {
            int course = q.poll();
            for (int neighbour : AdjList.get(course)) {
                indeg[neighbour] -= 1;
                if (indeg[neighbour] == 0) {
                    q.add(neighbour);
                    p[neighbour] = course;
                }
            }
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (p[i] == -1 && indeg[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
}