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

var but0 = document.getElementById("b"); //button for adding items to the first list
var children = document.getElementById("thelist").children; //gets the terms in the first list

var update = function(){
  for (var i=0; i<children.length; i++){ //loops through all the terms of the first list
    children[i].addEventListener('mouseover', function(){
      document.getElementById("h").innerHTML = this.innerHTML; //puts the innerHTML of whats in the term into the heading
    });
    children[i].addEventListener('mouseout', function(){
      document.getElementById("h").innerHTML = "Hello World"; //puts the default value if the mouse moves off the list
    });
    children[i].addEventListener('click', function(){this.remove();} // click to remove a list
  );};
};

update() //activates the mouse over functionality before button is pressed. NECESSARY FOR IT TO WORK

/*adding element to list upon button push*/
but0.addEventListener('click', function(){ //looks for a button click
  var elem = document.createElement("LI");
  //used to append some text to a newly created li element
  var text = document.createTextNode("NEWNODE!!!");
  elem.appendChild(text);

  document.getElementById("thelist").appendChild(elem); //puts the new term into the list

  update(); //updates the mouseover functionality
  }
);

/*
PHASE IV:
Add a second list to the html page. Do not add elements to it.
Create a second button.
When the second button is pressed,
add a new item to your list, showing the next Fibonacci number.
Beyond!: add more lists that generate other sequences…
*/

var fibNum = 1; // numbers for the fib
var fibBefore = 0;

var but1 = document.getElementById("fb"); //button for the fib function
but1.addEventListener('click', function(e){
  var elem = document.createElement("li");

  var text = document.createTextNode(fibNum); //creates the next term of fib
  elem.appendChild(text);

  document.getElementById("fiblist").appendChild(elem); //adds the new term

  var holdNum = fibNum; //updates fibNum
  fibNum+=fibBefore;
  fibBefore = holdNum;
}
);
