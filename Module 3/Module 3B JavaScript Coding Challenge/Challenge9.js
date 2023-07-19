
// Return the number of vowels in a string

function vowelCount(str) {
    var count = 0;
    var vowels = 'aeiou';

for (var i = 0; i < str.length; i++){
    if(vowels.indexOf(str[i].toLowerCase()) > -1){
        count++;
    }
    
}
return "This string contains " + count + " vowels in it";

}
console.log(vowelCount("We are automation test engineers"));
