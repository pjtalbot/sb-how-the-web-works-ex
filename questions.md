What is HTTP?
    Http is a protocol for communication between two parties, the client (usually a browser) and the server. The Client sends a request and the server usually responds with the requested data. 


What is a URL?
    A url is a string representing the adress of a particular server.
What is DNS?
    DNS translates the URL which is usually a human readable string, into IP addresses, computer readable destinations for sendthing the HTTP requests and/or responses
What is a query string?
    A query string is a variable passed through the url beginning with the character ?. the variable is often name something like "search" or filter. for example. something.com/browse?search=funny_videos?limit=10

    the above example goes to the /browse endpoint, and passes two queries to the server, "search" which evaluates to "funny_videos", and "limit" which is 10.
What are two HTTP verbs and how are they different?
    The http verbs are common methods used to make a request to a server.
    GET requests a response with data, but cannot change or add any data to the server
    POST sends a request with data that might be added to a database for example
    PATCH updates an existing dataset or object
What is an HTTP request?
    A request is an object sent from the client to the server
What is an HTTP response?
    A response is an object sent from the server to the client
What is an HTTP header? Give a couple examples of request and response headers you have seen.
    An HTTP header is part of a request that contains aditional information about the request, like the method, possibly user information, auth tokens, or cookies
What are the processes that happen when you type “http://somesite.com/some/page.html” into a browser?
    The browser sends a request to the that endpoint at the server. If it's a valid request, the server serves up the html, which is received by the server and then the browser renders that html into the DOM and displays the page to the user. 