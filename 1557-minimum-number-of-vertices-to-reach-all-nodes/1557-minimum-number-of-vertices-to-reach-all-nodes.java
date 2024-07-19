class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        int[] in = new int[n]; // record the number of incoming edges for each node
        for(List<Integer> edge : edges) {
            in[edge.get(1)]++;
        }
        
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < in.length; i++) {
            if(in[i] == 0) {
                res.add(i);
            }
        }

        return res;
    }
}