class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> dup = new HashMap<Integer, Integer>();
        for(int i: nums)
        {
            if(dup.get(i) != null)
            {
                return true;
            }
            dup.put(i, 1);
        }
        return false;
    }
}