// Team ASCIIResort
// Hasif Ahmed and Alesandra Koroza
// SoftDev1 pd8
// K #29: Sequential Progression II: Electric Boogaloo...
// 2018-12-19


var fibonacci = function(n){
    if(n == 0 || n == 1){
	return n;
    } else {
	return fibonacci(n-1) + fibonacci(n-2);
    }
}

var gcd = function(a,b){
  if (b > a){
    var c = a;
    a = b;
    b = c;
  }
  var rem = a % b;
  if(rem == 0){
    return b;
  }
  return gcd(b,rem);
}


var students = ['Aaron', 'Emma', 'Bo'];

var randomStudent = function(){
    var randint = Math.floor(Math.random() * 10) % students.length;
    return students[randint];
}


var fibbut = document.getElementById("fib");
fibbut.addEventListener("click", function(){
    console.log(fibonacci(4))
});
var gcdbut = document.getElementById("gcd");
gcdbut.addEventListener('click', function(){
  console.log(gcd(100,10));
});
var studentbut = document.getElementById("student");
studentbut.addEventListener('click', function(){
  console.log(randomStudent());
});
