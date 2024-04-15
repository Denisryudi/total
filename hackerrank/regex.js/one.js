var Regex_Pattern = "hackerrank";

function processData(Test_String) {
    //Enter your code here
    var Regex = new RegExp(Regex_Pattern, "g");
    var Array = Test_String.match(Regex);
    console.log("Number of matches :", Array.length);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});



//ruby

// Regex_Pattern = 'hackerrank'

// Test_String = gets
// regex = Test_String.scan /#{Regex_Pattern}/
// print "Number of matches : ",regex.length


//python

// import re

// Test_String = input()

// match = re.findall(Regex_Pattern, Test_String)

// print("Number of matches :", len(match))