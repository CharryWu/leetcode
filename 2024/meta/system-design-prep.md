How to answer in a system design interview?
1. For a Read-Heavy System - Consider using a Cache.
2. For a Write-Heavy System - Use Message Queues for async processing
3. For a Low Latency Requirement - Consider using a Cache and CDN.
4. Need Atomicity, Consistency, Isolation, Durability Compliant DB - Go for RDBMS/SQL Database.
5. Have unstructured data - Go for NoSQL Database.
6. Have Complex Data (Videos, Images, Files) - Go for Blob/Object storage.
7. Complex Pre-computation - Use Message Queue & Cache.
8. High-Volume Data Search - Consider search index, tries or search engine.
9. Scaling SQL Database - Implement Database Sharding..google  и
10. High AvaPilability, Performance, & Throughput - Use a Load Balancer.
11. Global Data Delivery - Consider using a CDN.
12. Graph Data (data with nodes, edges, and relationships) - Utilize Graph Database.
13. Scaling Various Components - Implement Horizontal Scaling.
14. High-Performing Database Queries - Use Database Indexes.. 1point 3acres
15. Bulk Job Processing - Consider Batch Processing & Message Queues.
16. Server Load Management & Preventing DOS Attacks- Use a Rate Limiter.
17. Microservices Architecture - Use an API Gateway.
18. For Single Point of Failure - Implement Redundancy.
19. For Fault-Tolerance and Durability - Implement Data Replication.
20. For User-to-User fast communication - Use Websockets..--
21. Failure Detection in Distributed Systems - Implement a Heartbeat.
22. Data Integrity - Use Checksum Algorithm.
23. Efficient Server Scaling - Implement Consistent Hashing.. ----
24. Decentralized Data Transfer - Consider Gossip Protocol.
25. Location-Based Functionality - Use Quadtree, Geohash, etc.
26. Avoid Specific Technology Names - Use generic terms.
27. High Availability and Consistency Trade-Off - Eventual Consistency.
28. For IP resolution & Domain Name Query - Mention DNS (Domain Name System).. From 1point 3acres bbs
29. Handling Large Data in Network Requests - Implement Pagination..1point3acres
30. Cache Eviction Policy - Preferred is LRU (Least Recently Used) Cache.
