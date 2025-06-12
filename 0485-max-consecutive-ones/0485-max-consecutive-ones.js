/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let currentcount = 0;
    let maxcount = 0;
    for(let i = 0; i<nums.length; i++){
        if(nums[i]==1){
            currentcount++;
        }
        else{
            maxcount = Math.max(maxcount,currentcount)
            currentcount = 0;
        }
    }
    
    return Math.max(maxcount,currentcount)
};