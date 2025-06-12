/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let currentcount = 0;
    let maxcount = 0;
    for(let i = 0; i<nums.length; i++){
        if(nums[i]!=0 ){
            currentcount++;
        }
        else{
            if(maxcount<currentcount){
                maxcount=currentcount
            }
            currentcount = 0;
        }
    }
    if(maxcount<currentcount){
        maxcount=currentcount
    }
    return maxcount
};