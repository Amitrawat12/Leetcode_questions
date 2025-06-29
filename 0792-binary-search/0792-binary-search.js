/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;
    while(r>=l){
        let mid = Math.floor((l+r)/2);

        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] < target){
            l = mid + 1;
        } 
        else{
            r = mid - 1;
        }
    }
    return -1;
};

