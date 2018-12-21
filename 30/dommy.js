//Team: ASCIIresort
//<Frist> <Lsat>
//SoftDev1 pd8
//K #30: Sequential Progression III: Season of the Witch
//2018-12-20


/*
PHASE III
Upon button push, add an element to the list.
When the mouse goes over an item in the list, change the heading at the top to contain the text of the item.
When the mouse is no longer over an item in the list, change the heading back to "Hello World!".
When an item on the list is clicked, remove it from the DOM.
*/

//adding element to list upon button push
var but0 = document.getElementById("b");
//console.log(fibbut);
but0.addEventListener('click', function(x){
  console.log(x);
  var elem = document.createElement("LI");
  //used to append some text to a newly created list element
  var text = document.createTextNode("NEWNODE!!!");
  elem.appendChild(text);
  document.getElementById("thelist").appendChild(elem);
  }
);

var but1 = document.getElementById("fb");
//console.log(fibbut);
but1.addEventListener('click', function(e){
  console.log(e);}
);

var lst = document.getElementById("thelist");
//console.log(fibbut);
lst.addEventListener('mouseover', function(e){
  //console.log(e);
  var lst= this.innerHTML;
  //console.log(lst.children);
  //document.getElementById("h").innerHTML = str;
});

lst.addEventListener('mouseout', function(e){
  console.log(e);
  //var str= lst.innerHTML;
  document.getElementById("h").innerHTML = "Hello World";
});
