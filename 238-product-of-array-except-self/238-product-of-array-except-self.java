class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N= nums.length;
        int []leftProd=new int [N];
        int []rightProd=new int [N];
        
        int []outputArr=new int[N];
        leftProd[0]=1;
        rightProd[N-1]=1;
        
        for(int i=1;i<N;i++){
            leftProd[i]=nums[i-1]*leftProd[i-1];
        }
        for(int i=N-2; i>=0;i--){
            rightProd[i]=nums[i+1]*rightProd[i+1];
        }
        for(int i=0; i<N;i++){
            outputArr[i]=leftProd[i]*rightProd[i];
        }
        return outputArr;
    }
}