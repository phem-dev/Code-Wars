/*Instructions:
Complete the solution so that it reverses the string passed into it.
e.g
'world'  =>  'dlrow'
'word'   =>  'drow'
*/

//Solution:

function solution(str) {
  let splitString = str.split(""); //split string into array
  let reverseArray = splitString.reverse(); //reverse array
  let joinArray = reverseArray.join(""); //join array to form string

  return joinArray;
}
