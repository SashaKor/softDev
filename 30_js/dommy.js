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
var lst = document.getElementById("thelist");
var children= lst.children
//var lst = document.getElementsByTagName("li");
//console.log(fibbut);
but0.addEventListener('click', function(x){
  console.log(x);
  var elem = document.createElement("LI");
  //used to append some text to a newly created li element
  var text = document.createTextNode("NEWNODE!!!");
  elem.appendChild(text);
  document.getElementById("thelist").appendChild(elem);
  }
);

for (var i=0; i<children.length; i++){
  children[i].addEventListener('mouseover', function(e){
    console.log(e);
    document.getElementById("h").innerHTML = this.innerHTML;
  });
  children[i].addEventListener('mouseout', function(){
    document.getElementById("h").innerHTML = "Hello World";
  });
  children[i].addEventListener('click', function(){this.remove();}
);
};


/*
PHASE IV:
Add a second list to the html page. Do not add elements to it.
Create a second button.
When the second button is pressed,
add a new item to your list, showing the next Fibonacci number.
Beyond!: add more lists that generate other sequences…
*/
var fibNum = 1;

var fib = function(n){
    if (n == 0)
        return 0;
    else if (n<3)
        return 1;
    else
        return fib(n -1) + fib(n -2);
};

var but1 = document.getElementById("fb");
but1.addEventListener('click', function(e){
  console.log(e);
  var elem = document.createElement("LI");
  //used to append some text to a newly created list element
  var text = document.createTextNode(fib(fibNum++));
  elem.appendChild(text);
  document.getElementById("fiblist").appendChild(elem);
}
);
