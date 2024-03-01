/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const reslt=[]
    for(const i in arr){
        reslt.push(fn(arr[i],Number(i)));
    } 
    return reslt
};