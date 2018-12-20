var but0 = document.getElementById("b");
//console.log(fibbut);
but0.addEventListener('click', function(x){
  console.log(x);}
);

var but1 = document.getElementById("fb");
//console.log(fibbut);
but1.addEventListener('click', function(e){
  console.log(e);}
);

var lst = document.getElementById("thelist");
//console.log(fibbut);
lst.addEventListener('mouseover', function(e){
  console.log(e);
  document.getElementById("h").innerHTML = "Paragraph changed!";
});
