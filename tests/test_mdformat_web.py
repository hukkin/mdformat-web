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
