#### What is distributed DataStore ?

A distributed data store is a computer network where information is stored on more than one node, often in a replicated fashion.

**Distributed databases** are usually non-relational databases that make a quick access to data over a large number of nodes possible. 


As a data distributed storage system make use of multiple computers, **load balancing** comes very naturally. Tasks are fashioned in the most coordinated manner. They make use of such distributed data storage techniques that can never be imagined with a single system setup. 

#### How Distributed Data Store Works ?

The Distributed Data stored in One Primary Node and rest replicated to Secondary Nodes.(InSync Replicas). The Primary Node for the data is being decided on basis of **PartitioHashing or Hashing Technique**.

The Hashed Key + Data comes to the cluster where nodes are in **Consistent Hashing** pattern. So, the data comes to Server based on **"serverIndex = hashValue % n"**.

The Nodes in a cluster have primary responsibility and Secondary responsibilty. The nodes in a cluster have each others information based on **gossip protocol**. So, When a node goes down the primary responsibilty(of storing data) is being shifted to new node.

Above we have discussed about consistent hashing. Now Let's discuss why we need consistent hashing.

#### Why Consistent Hashing ?

Let's say on a cluster we have 4 nodes and each have certain ranges.

CLUSTER -- Node A ( 1 - 2)
        -- Node B ( 2 - 4)
        -- Node C ( 4 - 6)
        -- Node D ( 6 - 8)

Now, In the process of Scaling we need to add two more nodes to the cluster. so, the **hashKeyRange** is being disturbed and primary Data an secondary Data need to be shifted to adjust with the serverIdx. That means There would be a lot of data shuffle , eventually make the Network Traffic lot Busy. Secondly, There may be uneven distribution that may create **HotSpot**.

**Now Consistent hashing helps in bringing down the N/W related shuffle. Let's see How ?**

Consistent hashing facilitates the distribution of data across a set of nodes in such a way that minimizes the re-mapping/ reorganization of data when nodes are added or removed. 

1. **Creating the Hash Key Space**: Consider we have a hash function that generates integer hash values in the range [0,  2^32-1).We can represent this as an array of integers with 2^32 -1 slots. We'll call the first slot x0 and the last slot xn – 1.

2. **Representing the hashSpace as a Ring**: Imagine that these integers generated is placed on a ring such that the last value wraps around.(1st value -- last value close together in a ring.)

3. **Placing DB Servers in Key Space (HashRing)**: We're given a list of database servers to start with. Using the hash function, we map each db server to a specific place on the ring. For example, if we have 4 servers, we can use a hash of their IP addressed to map them to different integers using the hash function. This simulates placing the four servers into a different place on the ring as shown below.

4. **Determining Placement of Keys on Servers**: To find which database server an incoming key resides on (either to insert it or query for it ), we do the following:
    > Run the key through the same hash function we used to determine db server placement on the ring.​
    > After hashing the key, we'll get an integer value which will be contained in the hash space, i.e., it can be    mapped to some postion in the hash ring. There can be two cases:
         > The hash value maps to a place on the ring which does not have a db server. In this case, we travel clockwise on the ring from the point where the key mapped to untill we find the first db server. Once we find the first db server travelling clockwise on the ring, we insert the key there. The same logic would apply while trying to find a key in the ring.
         > The hash value of the key maps directly onto the same hash vale of a db server – in which case we place it on that server.
    <<Example: Example: Assume we have 4 incoming keys : key0, key1, key2, key3 and none of them directly maps to the hash value of any of the 4 servers on our hash ring. So we travel clockwise from the point these keys maps to in our ring till we find the first db server and insert the key there. >>

5. **Adding a server to the Ring**: If we add another server to the hash Ring, server 4, we'll need to remap the keys. However, ONLY the keys that reside between server 3 and server 0 needs to be remapped to server 4. On an average , we'll need to remap only k/n keys , where k is the number of keys and n is the number of servers. This is in sharp contrast to our modulo based placement approach where we needed to remap nearly all the keys.
