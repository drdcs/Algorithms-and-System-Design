## System Design for Million User - Application
## --------------------------------------------

For an Application to scale for million Users need some specific design principle. We are going to discuss a generic system design principle.

## System Design:

![alt text](https://github.com/drdcs/simple_algo/blob/main/images/scaleWebsite.png?raw=true)

### 1

Internet protocol (IP) address is returned to the browser/app, while user access the website through domain names.Usually Domain Name System (DNS) is the 3rd party service which is not hosted in our server.Once IP address is obtained , HTTP request directly sent to the webserver.


### 2

Web Application - Desktop or Mobile Applications have 2 parts. Server side language and client side language. Client side is basically HTML, JS which shows the page layout, structure of website or more of a presentation layer.


### 3

Web Servers -  All the client request sent to the Web Server. All Web Servers return HTML pages or JSON response for rendering.The Server side is the actual logic which powers the application fundamentals, like APIs.
/GET /users, /POST /users etc .. 

Response Lokks Something Like below:
```json
{
    "cityId": 1,
    "cityName": "San Francisco",
    "address":{
        "streetName": "1001 National Ave",
        "postalCode": "600032"
    }
}
```

