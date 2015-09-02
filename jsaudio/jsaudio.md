class: center, middle

#Javascript Basics
---
#A quick introduction
    var javascript = "cool";

JavaScript is a lightweight, interpreted, .blue[object-oriented] 
language with first-class functions, most known as the scripting language for Web pages... It is a .red[prototype-based], 
multi-paradigm scripting language that is .green[dynamic], and supports object-oriented, imperative, and 
functional programming styles.

---
class: center, middle
#What does that mean?
---
#.blue[Object-Oriented]
Almost everything in Javascript is an object. Functions, objects, arrays, and variables all are objects.

```javascript
var foo = function() {
  return "foo";
}

foo.bar = function() {
  return "bar";
}

document.write(foo(), foo.bar());
//Prints 'foobar'
```

---
#.red[Prototype-based]
A fruit bowl serves as one example. A "fruit" object would represent the properties and functionality of fruit 
in general. A "banana" object would be cloned from the "fruit" object, and would also be extended to include 
general properties specific to bananas. Each individual "banana" object would be cloned from the generic "banana" object.

---
class: middle
```javascript
var Fruit = function(name) {
  this.name = name;
  document.write("New "+name+" created<br />");
}

var Banana = function(peeled) {
  Fruit.call(this, "banana");
  this.peeled = peeled;
}

var banana = new Banana(true);
var banana2 = new Banana(false);

document.write(banana.name +" "+ banana.peeled);
document.write(banana2.name +" "+ banana2.peeled);
//Prints:
//"New banana created"
//"New banana created"
//"banana true"
//"banana false"
```
---
#.green[Dynamic]

