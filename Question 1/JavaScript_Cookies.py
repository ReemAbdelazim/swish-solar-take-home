'''
# Question 1: What are JavaScript Cookies

To be honest, I didn't know what cookies were until I did some research and read some documentation.
Cookies are small pieces of data that are stored on the user's computer by the web browser while browsing a website. 
They are used to remember information about the user, such as login status, preferences, and other session-related data.

For example, when you log into a website, a cookie may be created to remember that you are logged in.
This way, you don't have to log in again every time you visit the site.
I also learned that cookies can be set to expire after a certain period, or they can be deleted by the user or the website.
Cookies can also be used for tracking purposes, such as remembering items in a shopping cart or tracking. 

I also found it intersting that cookies can be set with different attributes, such as `Secure`, `HttpOnly`, and `SameSite`, which control how the cookie is sent and accessed by the browser.
They also have limitations, such as size limits (typically around 4KB per cookie) and the number of cookies that can be stored per domain. Also the fact that they are automatically sent with every HTTP request to the domain that set them, which can affecr performance if overused.
It made me understand why developers might choose localStorage or sessionStorage for certain use cases, as they can store larger amounts of data without the same limitations as cookies.
'''