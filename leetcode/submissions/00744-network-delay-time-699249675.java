// Submission title: Network Delay Time
// Submission url  : https://leetcode.com/problems/network-delay-time/description/
// Submission url  : https://leetcode.com/submissions/detail/699249675/
// Submission json : {"id":699249675,"status_display":"Accepted","lang":"java","question_id":744,"title_slug":"network-delay-time","code":"class Solution {\n   private final Map<Integer, List<Node>> connected = new HashMap<>();\n\n    public int networkDelayTime(int[][] times, int n, int k) {\n        for (int[] time : times) {\n            connected.putIfAbsent(time[0], new ArrayList<>());\n            connected.get(time[0]).add(new Node(time[2], time[1]));\n        }\n        connected.forEach((source, nodes) -> nodes.sort(Comparator.comparing(Node::travelTime)));\n        int[] receivedTime = new int[n + 1]; Arrays.fill(receivedTime, 1, receivedTime.length, Integer.MAX_VALUE);\n        dfs(receivedTime, 0, k);\n        \n        int max = Arrays.stream(receivedTime).max().orElseThrow(RuntimeException::new);\n        return max == Integer.MAX_VALUE ? -1 : max;\n    }\n\n    private void dfs(int[] receivedTime, int currentTime, int currentNode) {\n        if (receivedTime[currentNode] <= currentTime) return;\n        receivedTime[currentNode] = currentTime;\n        if (connected.containsKey(currentNode))\n            connected.get(currentNode).forEach(node -> dfs(receivedTime, currentTime + node.travelTime(), node.destination()));\n    }\n\n    public record Node(int travelTime, int destination) {}\n}","title":"Network Delay Time","url":"/submissions/detail/699249675/","lang_name":"Java","time":"1 year, 8 months","timestamp":1652531316,"status":10,"runtime":"43 ms","is_pending":"Not Pending","memory":"44.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
   private final Map<Integer, List<Node>> connected = new HashMap<>();

    public int networkDelayTime(int[][] times, int n, int k) {
        for (int[] time : times) {
            connected.putIfAbsent(time[0], new ArrayList<>());
            connected.get(time[0]).add(new Node(time[2], time[1]));
        }
        connected.forEach((source, nodes) -> nodes.sort(Comparator.comparing(Node::travelTime)));
        int[] receivedTime = new int[n + 1]; Arrays.fill(receivedTime, 1, receivedTime.length, Integer.MAX_VALUE);
        dfs(receivedTime, 0, k);

        int max = Arrays.stream(receivedTime).max().orElseThrow(RuntimeException::new);
        return max == Integer.MAX_VALUE ? -1 : max;
    }

    private void dfs(int[] receivedTime, int currentTime, int currentNode) {
        if (receivedTime[currentNode] <= currentTime) return;
        receivedTime[currentNode] = currentTime;
        if (connected.containsKey(currentNode))
            connected.get(currentNode).forEach(node -> dfs(receivedTime, currentTime + node.travelTime(), node.destination()));
    }

    public record Node(int travelTime, int destination) {}
}
