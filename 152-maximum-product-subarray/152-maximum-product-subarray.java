class Solution {
    public int maxProduct(int[] nums) {
        // len=nums.length;
//         int maxProd=nums[0];
//         int prod=1;
//         for(int i:nums){
//             int cur=nums[i];
//             prod =Math.max(prod,prod*cur);
//             maxProd=Math.max(maxProd,prod);
            
//         }
//         return maxProd;
        if(nums.length==0)return 0;
    int result=nums[0];
        for(int i=0;i<nums.length;i++){
            int acc=1;
            for(int j=i;j<nums.length;j++){
                acc*=nums[j];
                result=Math.max(result,acc);
            }
        }
        return result;
    }
}