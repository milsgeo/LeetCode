class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i=0;
        int j=0;
        int k=0;      

        int l1=nums1.length;
        int l2=nums2.length;
        
        int []arr3 = new int[l1+l2];
        
        while(i<l1 && j<l2){
            if(nums1[i]<nums2[j]){
                arr3[k++]=nums1[i++];
            }else{
                arr3[k++]=nums2[j++];
            }
        }
        
        while(i<l1){
            arr3[k++]=nums1[i++];
        }
        while(j<l2){
            arr3[k++]=nums2[j++];
        }
        
        int l3=arr3.length;
        
        if(l3%2!=0){
            return (double)arr3[l3/2];
        }
        return (double)(arr3[(l3 - 1) / 2] + arr3[l3 / 2]) / 2.0;
    }
}