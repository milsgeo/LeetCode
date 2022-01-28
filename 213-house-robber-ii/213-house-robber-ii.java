class Solution {
    public int rob(int[] nums) {
        //base cases
        if(nums==null || nums.length==0)return 0;
        
        if(nums.length==1){
            return nums[0];
        }
//          if(nums.length==2){
//             return Math.max(nums[0], nums[1]);
//         }
        
//         //initializing dp array
        
//         int []dp = new int[nums.length];
//         dp[0]=nums[0];
//         dp[1]=Math.max(nums[0],nums[1]);
        
//         for(int i=2;i<nums.length;i++){
//             dp[i]=Math.max(nums[i]+dp[i-2],dp[i-1]);
//         }
//         return dp[nums.length-1];
        int max1=robCircle(nums,0,nums.length-2);
        int max2=robCircle(nums,1,nums.length-1);
        
        return Math.max(max1,max2);
    }
    
    public int robCircle(int[] nums,int init,int fin){
        int t1=0;
        int t2=0;
        
        for(int i=init;i<=fin;i++){
            int temp=t1;
            int curr = nums[i];
            t1=Math.max(curr+t2,t1);
            t2=temp;
        }
        return t1;
    }  
    
}