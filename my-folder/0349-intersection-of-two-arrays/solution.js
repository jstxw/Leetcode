/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const flat = [...nums1, ...nums2]
    let newFlat = [... new Set(flat.filter((val, i) => flat.indexOf(val) != i))].filter(val => nums1.includes(val) && nums2.includes(val))

    return newFlat
    
};
