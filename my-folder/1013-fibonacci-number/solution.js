/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    let series = [0,1];
    let i = 0
        for (i = 2; i <= n; i++ ){
            series.push(series[i-1] + series[i-2])
        }
        return series[n]
    };
