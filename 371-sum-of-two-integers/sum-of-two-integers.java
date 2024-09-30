class Solution {
    public int getSum(int a, int b) {
        int res=a^b;
        int carry=a&b;
        int temp;
        while(carry!=0){
            carry=carry<<1;
            temp=res;
            res=res^carry;
            carry=temp&carry;
        }
        return res;
    }
}