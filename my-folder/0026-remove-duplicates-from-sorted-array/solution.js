/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let x = removeDuplicates.length
    if (x === 0) {
        return 0
    }

    let i = 0 
    for (let j = 1; j < nums.length; j ++ ) {
        if (nums[i] != nums[j]) {
            i ++
        nums[i] = nums[j]
    }
    }
return i + 1 
    
};
