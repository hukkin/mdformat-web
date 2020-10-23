import mdformat


def test_js():
    unformatted_md = """~~~js

function myFunction()
{    // Declare a function
document.getElementById("demo").innerHTML = "Hello World!";}

myFunction();             // Call the function


~~~
"""
    formatted_md = """```js
function myFunction() { // Declare a function
    document.getElementById("demo").innerHTML = "Hello World!";
}

myFunction(); // Call the function
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"js"}) == formatted_md


def test_css():
    unformatted_md = """~~~css
body {background-color: powderblue;
}
h1
{
  color: blue;
}
p{
\t\tcolor: red;}


~~~
"""
    formatted_md = """```css
body {
    background-color: powderblue;
}

h1 {
    color: blue;
}

p {
    color: red;
}
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"css"}) == formatted_md


def test_html():
    unformatted_md = """~~~html
<ul>
<li>foo</li>
</ul>
<hr />
<ul>
<li>bar</li>
</ul>
~~~
"""
    formatted_md = """```html
<html>
 <body>
  <ul>
   <li>
    foo
   </li>
  </ul>
  <hr/>
  <ul>
   <li>
    bar
   </li>
  </ul>
 </body>
</html>
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"html"}) == formatted_md


def test_xml():
    unformatted_md = """~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to><from>Jani</from>
<heading>Reminder</heading><body>Don't forget me this weekend!</body>
</note>
~~~
"""
    formatted_md = """```xml
<?xml version="1.0" encoding="utf-8"?>
<note>
 <to>
  Tove
 </to>
 <from>
  Jani
 </from>
 <heading>
  Reminder
 </heading>
 <body>
  Don\'t forget me this weekend!
 </body>
</note>
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"xml"}) == formatted_md
