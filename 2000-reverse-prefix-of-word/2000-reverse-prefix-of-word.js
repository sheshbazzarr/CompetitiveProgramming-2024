/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    
    let chrindex=word.indexOf(ch)
    if (chrindex<0) return word
    
    let result= ''
    for (let i=chrindex;i>=0;i--){
        result+=word[i]
    }
    for (let j=chrindex+1;j<word.length;j++){
        result+=word[j]
    }
    
    return result
};

