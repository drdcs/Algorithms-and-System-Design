### Build a Facebook messenger like product , which supports - 

* Real time messaging
* Groups messaging
* Online Status
* Media Uploads 
* Read Receipts
* Notifications

### Technical Goals: 

* Low Latency
* High Volume
* Reliable
* Secure

#### -------------------------------------------------------

1. Users request to the API server for the chats. To have consistent connection we can have http polling - where instead of a connection the user polls requests consistently to see if there are any new messages. The downside is we are calling multiple api calls which is not necessary.

2. Long Polling: This is also a https request but instead of resolving the poll quickly it establishes a connection and holds on to the request, until it sees a new message comes in, then it sends the request and opens another connection. Solves latency problems but if a lot of messages comes then it behaves like http polling. The long polling is better for the notification system.

3. **WebSockets** : it opens a connection with the server but instead of one way connection , it establishes a duplex connection.We can send data to the server and the server sends data back to us. It maintains the connection till the session is open. This is the one I recommend.


4. If there are millions of request then we need to maintain a lot of chat api servers and the connection to those servers  happens through the load balancer.
Now we have another problem , because before we needed to connect one user with another through API servers, but now we have entered into the distributed systems. we need to connect from one api server to another. we can adopt the Pub-Sub message queue. That helps in interacting between api servers in a distributed way.

5. So we introduce the message service layer, the intent is the api servers sends messages to the message queue and any api server listening to the message reads the message from that queue and forwards the message to that user.


### Question is How to persist the message ? 

6. The database we need to choose that persists the data and obey cap theorem and maintains a trade off between consistency and partition vs availability vs partition. For chat app the availability is more important than consistency , so we need to choose a database like cassandra or Hbase (built in sharding and replication).


7. Database schema details below, it's like users table, messages table, conversation groups and conversation to user link.

8. An object store to store the media files like audio, video or image. To Cache those media files there may be CDN (content delivery network)

9. To cache the message for faster retrieval , we can have a cache mechanism to reduce the cost of database hits for messages.

10. Notify Users for offline messages they have missed, we can have a message service forward the message to the notification service and it then forward to the user as an alert.

### Flow diagram

![alt text](https://github.com/drdcs/simple_algo/blob/main/images/FM.png?raw=true)


### database models ?
                              
| users | #1 |
| :---: | :---: |
| id | int |
| username | string |
| lastActive | timestamp |
               
| messages | #1 |
| :---: | :---: |
| id | int |
| user | int |
| conversation | int |
| text | int |
| conversation | string |

| conversation | #1 |
| :---: | :---: |
| id | int |
| name | string |


| conversation user | #1 |
| :---: | :---: |
| conversation | int |
| user | int |


