//Team: ASCIIresort
//Aleksandra K, Derek C
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

/*adding element to list upon button push*/
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

var lst = document.getElementsByTagName("li");
for (var i=0; i<lst.length; i++){
  lst[i].setAttribute('val', i);
  lst[i].addEventListener('mouseover', function(){document.getElementById("h").innerHTML = "Item " + this.getAttribute("val");});
  lst[i].addEventListener('mouseout', function(){document.getElementById("h").innerHTML = "Hello World"});
  lst[i].addEventListener('click', function(){this.remove()});
}

//var lst = document.getElementById("thelist");
//children = lst.children
//for (i in members) {


//}

/*
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

/* when item clicked, remove from DOM
lst.addEventListener('click', function(e){
  console.log(e);

});
*/
/*
PHASE IV:
Add a second list to the html page. Do not add elements to it.
Create a second button.
When the second button is pressed,
add a new item to your list, showing the next Fibonacci number.
Beyond!: add more lists that generate other sequences…
*/
var but1 = document.getElementById("fb");
//console.log(fibbut);
but1.addEventListener('click', function(e){
  console.log(e);}
);
