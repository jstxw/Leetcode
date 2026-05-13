/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    let i, j; 

    i = Number(Math.abs(x-z))
    j = Number(Math.abs(y-z))

    if (i<j) {
        return 1
    } else if (i >j) {
        return 2 
    } else if (i == j) {
        return 0
    }
};
