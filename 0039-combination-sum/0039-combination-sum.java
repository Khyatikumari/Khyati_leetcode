class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> rez = new ArrayList<>();

        sum(0, target, new ArrayList<Integer>(), rez, candidates);

        return rez;
    }

    private void sum(int startIdx, int remaining, List<Integer> current, List<List<Integer>> rez, int[] candidates) {

        if (remaining == 0) {
            rez.add(new ArrayList<>(current));
            return;
        } else if (remaining < 0) {
            return;
        }

        for (int i = startIdx; i < candidates.length; i++) {
            int num = candidates[i];
            current.add(num);
            sum(i, remaining - num, current, rez, candidates);
            current.remove(current.size() - 1);
        }
    }
}