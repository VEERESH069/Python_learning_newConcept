class Solution {
    public:
        int trap(vector<int>& height) {
            long long ans =0;
            int n = height.size();
            for(int i=0;i<n-1;i++){
                int left = height[i];
                for(int j=0;j<i;j++){
                    left = max(left, height[j]);
                }
                int right = height[i];
                for(int j=i+1;j<n;j++){
                    right = max(right, height[j]);
                }
                ans+=(min(left, right)- height[i]);
            }
            return ans;
        }
    };