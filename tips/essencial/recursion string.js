const str = "hello";
//base
function solution(str) {

if(str.length === 0) return "";
//recursion
return str[str.length-1] +
solution(str.slice(0, str.length-1))
}
console.log(solution(str));


//const str = "hello";

function solution(str) {
  let reversed = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  return reversed;
}

console.log(solution(str));