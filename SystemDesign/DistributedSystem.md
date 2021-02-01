### Distributed System - 

Group of commodity computers comes together to achieve a common task / Work.

### Why do I need a DS ?

A service that serves tinyURL converters and is hosted on a single server. (8GB RAM , 100GB HD)

Approach 1: 
1st Month : 1000 requests / second .. 
2nd Month : 100000 requests / second .. slowness => (128GB RAM , 1TB HD)
3rd Month : 1M requests / second .. Vertical Scaling .. not efficient as cost is high.


Approach 2: (8GB RAM , 100GB HD)
1st Month : 1000 requests / second .. 
2nd Month : 100000 requests / second .. slowness => (8GB RAM , 100 HD - Server 1 ) + (8GB RAM , 100 HD -  Server 2) 
3rd Month : 1M requests / second .. Horizontal Scaling. cluster of machines grouped together to solve the perpose.
 _
|_| 
|_|  ⇒    
|_|
|_|

DS benefits :

1. Though initial investment is high but after break even it is more profitable.
2. Fault Tolerant. Server down for maintenance.
3. Low Latency.




**Distributed Datastores** -

Let's say a master - slave architecture where the server user request has been written to a master DB and Master DB asynchronously writes the data into the slave DB. When the user response is accepted, data read from the slave DB.

Now, what if the asynchronous data written to Slave DB fails and the user while reading the data is either not available or not updated, that means the DB is not consistent from (CAP theorem).

So, to eradicate the above possibility there is a process called **data Sharding**. That means every DB has the same responsibility of both data read and Write.

The **definition of Sharding** is a method for distributing data across multiple machines. Database systems with large data sets or high throughput applications can challenge the capacity of a single server. For example, high query rates can exhaust the CPU capacity of the server. Working set sizes larger than the system’s RAM stress the I/O capacity of disk drives.

To route the request to a different Shared Server is based on the **Shared Key**. The shard key is either an indexed field or indexed compound fields that determines the distribution of the collection’s documents among the cluster’s shards.

**Hot Spot** : What if the shared key is not efficiently routing the data and one instance got high throughput. the server is overwhelmed with requests and that causes the hotspot.

#### CAP Theorem : Consistency, Availability and Partition.

**Consistency** - When a user writes/reads the data in DB, it always gives the information we expected.This condition states that all nodes see the same data at the same time. Simply put, performing a read operation will return the value of the most recent write operation causing all nodes to return the same data. A system has consistency if a transaction starts with the system in a consistent state, and ends with the system in a consistent state.

**Availability** : Even if some/few machines go down still the system works.This condition states that every request gets a response on success/failure. Achieving availability in a distributed system requires that the system remains operational 100% of the time. Every client gets a response, regardless of the state of any individual node in the system. This metric is trivial to measure: either you can submit read/write commands, or you cannot. 

**Partition** : This condition states that the system continues to run, despite the number of messages being delayed by the network between nodes. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data records are sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages. 

When dealing with modern distributed systems, Partition Tolerance is not an option. It’s a necessity. 
Hence, we have to trade between Consistency and Availability.

BASE - basically Available Soft State and Eventual Consistency.

