class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int total = 0;

        while(left < right){
            int present_height = Math.min(height[left], height[right]);
            int present_width = right - left;
            int present_area =  present_height * present_width;

            total = Math.max(total, present_area);

            if(height[left] < height[right]){
                left += 1;
           
            }
             else{
                right -= 1;
            }
        }
        return total;

        
    }
}