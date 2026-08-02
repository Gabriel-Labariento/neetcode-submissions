class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!hashMap.containsKey(nums[i])) {
                hashMap.put(nums[i], 1);
            } else {
                hashMap.replace(nums[i], hashMap.get(nums[i]) + 1);
            }
        }

        List<Integer> sorted = new ArrayList<>(hashMap.keySet());
        Collections.sort(sorted, (a, b) -> hashMap.get(b) - hashMap.get(a));

        int[] arr = new int[k];
        for (int i = 0; i < k; i++){
            arr[i] = sorted.get(i);
        }

        return arr;
    }
}
