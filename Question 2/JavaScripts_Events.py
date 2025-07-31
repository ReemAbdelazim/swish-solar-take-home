'''
# Question 2: Give some examples of JavaScript Events in HTML.

I didn't know where to start, so I decided to focu on the top 10 common examples of JavaScript events in HTML:
1. **Click Event**: Triggered when an element is clicked.
   ```html
   <button onclick="alert('Button clicked!')">Click Me</button>
   ```
2. **Mouseover Event**: Triggered when the mouse pointer moves over an element.
   ```html
    <div onmouseover="this.style.backgroundColor='yellow';" onmouseout="this.style.backgroundColor='white';">
         Hover over me!
    </div>
    ```
3. **Keydown Event**: Triggered when a key is pressed down.
    ```html
    <input type="text" onkeydown="console.log('Key pressed: ' + event.key)">
    ```
4. **Change Event**: Triggered when the value of an input element changes.
    ```html
    <input type="text" onchange="console.log('Input changed to: ' + this.value)">
    ```
5. **Submit Event**: Triggered when a form is submitted.
    ```html
    <form onsubmit="alert('Form submitted!'); return false;">
        <input type="text" required>
        <button type="submit">Submit</button>
    </form>
    ```
6. **Load Event**: Triggered when the page or an element finishes loading.
    ```html
    <body onload="console.log('Page loaded!')">
        <h1>Welcome to my page!</h1>
    </body>
    ```
7. **Focus Event**: Triggered when an element gains focus.
    ```html
    <input type="text" onfocus="this.style.border='2px solid blue';" onblur="this.style.border='1px solid black';">
    ```
8. **Resize Event**: Triggered when the browser window is resized.
    ```html
    <script>
        window.onresize = function() {
            console.log('Window resized to: ' + window.innerWidth + 'x' + window.innerHeight);
        };
    </script>
    ```
9. **Scroll Event**: Triggered when the user scrolls the page.
    ```html
    <script>
        window.onscroll = function() {
            console.log('Page scrolled to: ' + window.scrollY);
        };
    </script>
    ```
10. **Context Menu Event**: Triggered when the right mouse button is clicked.
    ```html
    <div oncontextmenu="alert('Right-click menu opened!'); return false;">
        Right-click on me!
    </div>
    ```
These examples illustrate how JavaScript events can be used to enhance user interaction and provide dynamic functionality in web applications. By attaching event handlers to HTML elements, developers can create efficient and interactive user experiences.
These events can be handled using inline event attributes, as shown above, or by using JavaScript event listeners for more complex requirments. For example:
```javascript
document.getElementById('myButton').addEventListener('click', function() {
    alert('Button clicked using event listener!');
});
```
This approach allows for better separation of concerns and makes the code more maintainable, especially in larger applications.
When I am trying to get a sense of what events are available or if I feel like there might be a better option I have nott considered, I usually refer to the MDN Web Docs page on GlobalEventHandlers. 
It gives a clean list of all supported HTML events with examples, which I find really helpful when experimenting or troubleshooting.
Here is the link  for reference: https://developer.mozilla.org/en-US/search?q=GlobalEventHandlers
'''