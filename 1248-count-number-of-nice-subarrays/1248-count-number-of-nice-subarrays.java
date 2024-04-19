class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
      int eo[] = new int[nums.length];          //Array for storing even occurrences
      int oI[] = new int[nums.length];          //Array for the odd index positions
      int ec = 0,e = 0,o = 0;
      for(int x = 0; x < nums.length; x++){
        if(nums[x]%2 == 0){                     //For even numbers, we store -1
           eo[e++] = -1;
           ec++;                                //count the even elements
        }
       if(nums[x]%2 != 0){                      //For odd numbers, store the even occurrences before it's index
          eo[e++] = ec;
          oI[o++] = x;
          ec = 0;                               //set as 0
       }
     }
     int r = 0,ans = 0;
     for(r = 0; r+k <= o; r++ ){                   //sliding with value "k"
        ans++;                                 
        ans += eo[oI[r]];                      // pre element scenario
        if(r+k < o) {
            if(eo[oI[r]]!=0){
                ans += (eo[oI[r]] * eo[oI[r+k]]);    // combination scenario
            }
          ans += eo[oI[r+k]];                 // post-element scenario
        }
     }
     if(o >= k) {                             
        int ll = oI[o-1];
        int lf = k > 1 && o > 1 ? oI[o-k] : ll;
        int leftOver = nums.length-(ll+1);    //if there are further even elements after the last odd element
        ans += leftOver;                      //post scenario
       if(eo[lf] != 0)
          ans+=eo[lf]*leftOver;               //combination scenario 
   }
  
  return ans;                                 //return answer
}
}
