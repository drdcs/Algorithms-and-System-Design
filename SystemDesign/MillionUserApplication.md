## System Design for Million User - Application
## --------------------------------------------

For an Application to scale for million Users need some specific design principle. We are going to discuss a generic system design principle.

## System Design:

![alt text](https://github.com/drdcs/simple_algo/blob/main/images/scaleWebsite.png?raw=true)

### 1

*Internet protocol (IP) address is returned to the browser/app, while user access the website through domain names.Usually Domain Name System (DNS) is the 3rd party service which is not hosted in our server.Once IP address is obtained , HTTP request directly sent to the webserver.*


### 2

*Web Application - Desktop or Mobile Applications have 2 parts. Server side language and client side language. Client side is basically HTML, JS which shows the page layout, structure of website or more of a presentation layer.*


### 3

*Web Servers -  All the client request sent to the Web Server. All Web Servers return HTML pages or JSON response for rendering.The Server side is the actual logic which powers the application fundamentals, like APIs.*
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
### 4

*Databases persist the data. There are broadly 2 choices for persistance SQL/NO SQL.*
*SQL: Relational databases represent and store data in tables and rows. You can perform join operations using SQL across different database tables.*
*NoSQL:Non-Relational databases are also called NoSQL databases.These databases are grouped into four categories: **key-value stores, graph stores, column stores, and document stores**.*

***Database Replication: ***

### 5

*Before Load Balancer, let's Understand Horizontal Scaling vs Vertical Scaling. **Vertical Scaling** is scale-up which means increase the hardware(Like increase CPU, Memory etc.) to handle larger requests. But, It has a limit we can't infinitely add cpus to a server.Secondly, the Vertical Scaling for a single server does not have **failOver and Redundancy**, which means if sever goes down then Application Goes Down.*

*To mitigate issues of Vertical Scaling, Horizontal Scaling is great Choice.Unless having a single sever, we can have multiple severs where app being hosted.Instead connecting to ther server directly, we can connect it via **Load Balancer***

*Load Balancer - redirects the traffic among web Servers. Users connects to the IP(public ip) of Loadbalancer and load balancer connect to server using private Ips. If Server-1 goes offline then traffic redirects to Server-2.We can add n number of Servers to Load Balancer.*


