/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums) {
    const map=new Map()
    let max=-1;
    for (let i of nums){
        if(map.has(i*-1)){
            max=Math.max(max,Math.abs(i))
        }
        map.set(i,0)
    }
    return max
};

