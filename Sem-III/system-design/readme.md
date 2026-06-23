# System Design: Architecture, Distributed Systems, and Reference Manual

This document serves as a comprehensive reference guide for system design, distributed systems architecture, scaling paradigms, and reliability engineering.

---

## 1. Core System Design Fundamentals

Building modern, distributed software systems requires balancing multiple competing requirements. Before diving into architectural components, we must understand the fundamental metrics and trade-offs that govern system behavior.

### 1.1 Scalability
Scalability is the measure of a system's ability to handle growing amounts of work or its potential to be enlarged to accommodate that growth.

*   **Vertical Scaling (Scaling Up)**: Adding resources (CPU, RAM, Storage) to a single server node.
    *   *Pros*: Simple to implement; no changes to application architecture; zero network latency between components.
    *   *Cons*: Hard hardware limits; single point of failure (SPOF); exponential costs as server capacities reach premium limits.
*   **Horizontal Scaling (Scaling Out)**: Adding more machine nodes to the system pool.
    *   *Pros*: Virtually limitless scaling capability; built-in redundancy and high availability.
    *   *Cons*: Requires a load balancer; introduces network latency and synchronization issues; requires applications to be stateless.

### 1.2 Latency vs. Throughput
*   **Latency**: The time taken for a single unit of work to be processed and return a result (often measured in milliseconds).
*   **Throughput**: The number of units of work processed by the system within a given time interval (e.g., requests per second (RPS), queries per second (QPS), or data transfer rate).
*   *Key Relationship*: Lowering latency often helps increase throughput, but a system optimized for high throughput may sacrifice latency by processing requests in batches to reduce overhead.

### 1.3 Availability and SLAs
Availability is the percentage of time a system remains operational and accessible to perform its required functions. It is typically expressed in "nines":

| Availability | Downtime per Year | Downtime per Month |
| :--- | :--- | :--- |
| **99% (Two Nines)** | 3.65 days | 7.31 hours |
| **99.9% (Three Nines)** | 8.77 hours | 43.83 minutes |
| **99.99% (Four Nines)** | 52.56 minutes | 4.38 minutes |
| **99.999% (Five Nines)** | 5.26 minutes | 26.30 seconds |

*   **Service Level Agreement (SLA)**: A formal contract between a service provider and client specifying the guaranteed level of service (e.g., 99.9% availability) and penalties for failure.
*   **Service Level Objective (SLO)**: An internal target for service performance (e.g., latency < 200ms for 99% of requests).
*   **Service Level Indicator (SLI)**: A real-time metric measuring compliance with an SLO (e.g., actual request latency).

### 1.4 Reliability and Fault Tolerance
*   **Reliability**: The probability that a system performs its intended function without failure under specified conditions for a specified period.
*   **Fault Tolerance**: A system design characteristic that enables it to continue operating properly in the event of the failure of one or more of its components.
*   *Mechanism*: Realized through redundancy, graceful degradation, and eliminating Single Points of Failure (SPOF).

---

## 2. Load Balancing

Load balancers distribute incoming network traffic across multiple backend servers to prevent overload, optimize utilization, and ensure high availability.

### 2.1 Layer 4 (L4) vs. Layer 7 (L7) Load Balancing
Load balancers operate at different layers of the OSI model:

```mermaid
graph TD
    A[Client Request] --> B[Load Balancer]
    B -->|L4: Transport Layer TCP/UDP| C[IP:Port Routing]
    B -->|L7: Application Layer HTTP/HTTPS| D[Content-Based Routing]
```

*   **Layer 4 Load Balancing**:
    *   Operates at the Transport layer (TCP/UDP).
    *   Routes traffic based on IP address and port numbers without inspecting the packet payload.
    *   *Characteristics*: Fast, low CPU overhead, protocol agnostic, unable to perform smart routing based on request parameters (like cookies or HTTP headers).
*   **Layer 7 Load Balancing**:
    *   Operates at the Application layer (HTTP/HTTPS/gRPC).
    *   Inspects packet payloads to make routing decisions based on cookies, HTTP headers, URLs, or query parameters.
    *   *Characteristics*: Higher CPU overhead due to SSL termination and header parsing; enables features like session stickiness, path-based routing (e.g., `/api` vs `/static`), and web application firewalls (WAF).

### 2.2 Load Balancing Algorithms
1.  **Round Robin**: Sequentially routes requests to each server in the pool. Best when servers have identical capacity.
2.  **Weighted Round Robin**: Assigns a weight to each server based on capacity; higher-weighted servers receive proportionately more requests.
3.  **Least Connections**: Routes requests to the server with the fewest active connections. Ideal for long-lived transactions.
4.  **IP Hash**: Hashes the client's IP address to select a server. Useful for basic session persistence.
5.  **Consistent Hashing**: A hashing scheme where servers and keys are mapped onto a circular ring.
    *   *Core Benefit*: Minimizes key relocation when servers are added or removed (only $K/N$ keys need to be remapped, where $K$ is the number of keys and $N$ is the number of servers).

---

## 3. Database Scaling and Distributed Storage

As application demand grows, the database often becomes the primary system bottleneck. Scaling storage requires choosing the right paradigms and partitioning schemas.

### 3.1 SQL vs. NoSQL
Distributed systems require selecting databases that match query patterns and consistency requirements:

| Dimension | Relational (SQL) | Non-Relational (NoSQL) |
| :--- | :--- | :--- |
| **Schema** | Rigid, predefined tabular schemas. | Flexible (Document, Key-Value, Columnar, Graph). |
| **Scaling** | Typically vertical (can scale horizontally via read replicas/sharding). | Built to scale horizontally across commodity clusters. |
| **Transactions** | Strong ACID guarantees. | BASE properties (Eventual consistency prioritized). |
| **Examples** | PostgreSQL, MySQL, Oracle. | MongoDB, Cassandra, Redis, Neo4j. |

### 3.2 ACID vs. BASE
*   **ACID (Traditional SQL)**:
    *   **Atomicity**: All operations in a transaction succeed or all fail.
    *   **Consistency**: A transaction takes the database from one valid state to another.
    *   **Isolation**: Concurrent execution of transactions leaves the database in the same state as if they executed sequentially.
    *   **Durability**: Committed data survives system crashes.
*   **BASE (Modern NoSQL)**:
    *   **Basically Available**: The system is guaranteed to respond, but responses may fail or contain stale data.
    *   **Soft State**: The state of the system can change over time without explicit write operations due to propagation lag.
    *   **Eventual Consistency**: Data converges to a consistent state across all nodes given enough time without new updates.

### 3.3 CAP Theorem
In a distributed data store, you can guarantee at most two of the following three properties simultaneously:

```mermaid
graph TD
    C[Consistency] --- A[Availability]
    A --- P[Partition Tolerance]
    P --- C
    style P fill:#f9f,stroke:#333,stroke-width:2px
```

1.  **Consistency (C)**: Every read receives the most recent write or an error.
2.  **Availability (A)**: Every non-failing node returns a non-error response (without guarantee that it contains the most recent write).
3.  **Partition Tolerance (P)**: The system continues to operate despite arbitrary message loss or network partitions.
*   *Real-world trade-off*: In a network partition, you must choose between **CP** (cancel the operation to ensure consistency, sacrificing availability) and **AP** (proceed with the operation using local data, sacrificing consistency).

### 3.4 Scaling Storage: Replication, Partitioning, and Sharding
*   **Replication**: Copying data across multiple database nodes.
    *   *Single-Leader (Master-Slave)*: All writes go to the leader; reads can be served by followers. Good for read-heavy workloads. Introduces replication lag.
    *   *Multi-Leader (Master-Master)*: Multiple nodes accept writes. Requires complex conflict resolution.
    *   *Leaderless*: Clients write to and read from multiple nodes (e.g., Cassandra). Relies on quorums ($W + R > N$) to ensure consistency.
*   **Partitioning**: Dividing a large database into smaller, independent parts (partitions) within the same node to optimize query processing.
*   **Sharding**: Distributing database partitions across separate physical server nodes.
    *   *Horizontal Partitioning*: Storing different rows of the same table on different database servers.
    *   *Sharding Strategies*:
        *   **Range-Based**: Sharding based on a range of values (e.g., IDs 1–10,000 go to Shard A). Can cause hot-spotting.
        *   **Hash-Based**: Applying a hash function to a shard key to determine the target shard. Distributes data evenly but makes range queries expensive.
        *   **Directory-Based**: Using a lookup service to track which shard holds specific records. Introduces an extra network hop.

### 3.5 Storage Engines: B-Trees vs. LSM Trees
Storage engines manage how data is structured on disk:
*   **B-Trees**:
    *   Organize data into fixed-size pages (usually 4KB) structured as a balanced search tree.
    *   *Characteristics*: Fast random reads ($O(\log N)$); slower writes because updates modify pages in place, requiring disk head movement and write amplification.
*   **LSM Trees (Log-Structured Merge-Trees)**:
    *   Appends writes sequentially to an in-memory buffer (MemTable) and a sequential log on disk (Commit Log). When the MemTable fills up, it is flushed to disk as an immutable Sorted String Table (SSTable).
    *   *Characteristics*: High write throughput (since writes are sequential appends); reads are slower because they may need to search multiple SSTables, mitigated by Bloom Filters and Compaction.

---

## 4. Caching and Content Delivery

Caching stores frequently accessed data in high-speed, temporary memory (RAM) to serve requests faster and reduce the load on databases and backend application servers.

### 4.1 Caching Patterns
1.  **Cache-Aside (Lazy Loading)**:
    *   The application queries the cache first. If a cache miss occurs, it queries the database, writes the result to the cache, and returns it.
    *   *Pros*: Resilient to cache failures; cache only contains requested data.
    *   *Cons*: First request is slow (cache miss); data inconsistency can occur if the database is updated directly.
2.  **Read-Through**:
    *   The application treats the cache as the main data store. On a cache miss, the cache library/middleware reads from the database and updates itself transparently.
    *   *Pros*: Separates caching logic from application code.
    *   *Cons*: Requires a library/database driver supporting this integration.
3.  **Write-Through**:
    *   Writes go directly to the cache first, and the cache writes immediately to the database before confirming success.
    *   *Pros*: High data consistency; reads never experience cache misses for newly written data.
    *   *Cons*: High write latency (writes require two network hops).
4.  **Write-Behind (Write-Back)**:
    *   Writes update the cache first and immediately return success. The cache asynchronously batches updates and writes them to the database later.
    *   *Pros*: High write throughput; reduces direct database write pressure.
    *   *Cons*: Risk of data loss if the cache server crashes before data is persisted to disk.

### 4.2 Cache Eviction Policies
When the cache reaches memory limits, old or unused keys must be removed:
*   **LRU (Least Recently Used)**: Discards the least recently accessed items first.
*   **LFU (Least Frequently Used)**: Discards items with the lowest access frequency.
*   **FIFO (First In, First Out)**: Discards items in the order they were inserted.
*   **TTL (Time To Live)**: Automatically invalidates cache items after a set time duration.

### 4.3 Content Delivery Networks (CDNs)
A CDN is a geographically distributed network of proxy servers (Edge Nodes) designed to deliver content (images, video, JS, CSS, and dynamic APIs) to users from the closest physical location.
*   **Static Caching**: Edge servers store static files cached from the origin server based on cache-control headers.
*   **Dynamic Acceleration**: Minimizes round-trip times for API endpoints by optimizing network routing paths and TCP handshakes from the edge to the origin server.

---

## 5. API and Communication Protocols

Communication interfaces allow client-server interactions and inter-service connectivity in distributed architectures.

### 5.1 Communication Paradigms

1.  **REST (Representational State Transfer)**:
    *   Uses standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
    *   Stateless, resource-oriented, typically returns JSON or XML.
    *   *Pros*: Highly cacheable, universally supported, easy to understand.
    *   *Cons*: Over-fetching (receiving unneeded fields) or under-fetching (requiring multiple API calls for related data).
2.  **GraphQL**:
    *   A query language for APIs. The client defines the exact shape of the response needed.
    *   Uses a single endpoint (typically `/graphql` via `POST`).
    *   *Pros*: Solves over/under-fetching; strongly typed schema.
    *   *Cons*: Complex caching (cannot easily use HTTP GET cache headers); resource-intensive query validation.
3.  **gRPC (Remote Procedure Call)**:
    *   High-performance framework utilizing HTTP/2 transport and Protocol Buffers (protobuf) interface definition.
    *   *Pros*: Compact binary serialization; bidirectional streaming; compile-time code generation for client/server stubs.
    *   *Cons*: Limited browser support (requires gRPC-Web proxy); human-unreadable binary payloads make debugging complex.
4.  **WebSockets**:
    *   Provides full-duplex communication channels over a single, long-lived TCP connection.
    *   Starts with an HTTP handshake, then upgrades to WebSocket protocol.
    *   *Pros*: Low latency real-time events (real-time chat, stocks feeds).
    *   *Cons*: Hard to scale load-balancer connections; requires connection state management.

### 5.2 Protocol Comparison Matrix

| Protocol | Transport | Serialization | Type System | Flow Model | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REST** | HTTP/1.1 or 2 | JSON / XML | Weak / OpenAPIs | Request-Response | Public APIs, CRUD |
| **GraphQL** | HTTP | JSON | Strong Schema | Request-Response / Subscriptions | Complex UI queries |
| **gRPC** | HTTP/2 | Protobuf (Binary) | Strong Proto files | Bidirectional Streaming | Inter-microservice |
| **WebSockets**| TCP | Text / Binary | Custom | Full-Duplex Events | Chat, Live Dashboards |

---

## 6. Messaging and Event Streaming

Distributed systems use asynchronous communication to decouple services, absorb traffic spikes, and improve system availability.

```mermaid
graph LR
    Publisher[Publisher Service] --> Broker[Message Broker / Log Store]
    Broker --> ConsumerA[Consumer Service A]
    Broker --> ConsumerB[Consumer Service B]
```

### 6.1 Message Brokers vs. Log-Based Event Streaming

*   **Message Brokers (e.g., RabbitMQ, ActiveMQ)**:
    *   Operate on transient storage. Messages are deleted immediately or shortly after they are successfully acknowledged by a consumer.
    *   Supports complex routing keys, wildcards, and queues.
    *   *Use Case*: Point-to-point task queues, asynchronous transactional emails, decoupled job distribution.
*   **Log-Based Event Streaming (e.g., Apache Kafka, AWS Kinesis)**:
    *   Operates as a persistent, append-only log on disk. Messages (events) are not deleted after consumption; they persist based on time or size limits.
    *   Multiple consumers can read from different offsets of the same partition.
    *   *Use Case*: Event sourcing, log aggregation, real-time analytics pipelines, system telemetry.

### 6.2 Eventual Consistency and Idempotency
*   **Eventual Consistency**: Decoupled database states across microservices synchronize asynchronously through event broadcasts, eventual convergence matching the source of truth.
*   **Idempotency**: An operation is idempotent if it can be performed multiple times with the same output, leaving the system in the same state.
    *   *Why it is critical*: Network failures can lead to duplicate message deliveries (At-Least-Once delivery model). Consumers must be idempotent (e.g., using unique transaction IDs or deduping databases) to avoid processing the same event twice.

---

## 7. System Resiliency

Distributed systems must be designed for failure. Resiliency patterns prevent local failures from cascading across the entire cluster.

### 7.1 Rate Limiting Algorithms
Rate limiters restrict the number of requests a client can make in a given timeframe.

1.  **Token Bucket**:
    *   A bucket holds up to a maximum number of tokens. Tokens are added at a constant rate. Each request consumes a token. If the bucket is empty, the request is dropped.
    *   *Pros*: Allows brief bursts of traffic; simple to configure.
2.  **Leaking Bucket**:
    *   Requests enter a queue (the bucket) and leave it at a constant, smooth rate. If the queue is full, incoming requests overflow and are rejected.
    *   *Pros*: Guarantees a smooth output rate.
    *   *Cons*: Bursts are delayed rather than processed immediately.
3.  **Fixed Window Counter**:
    *   Divides time into windows (e.g., 1 minute) and increments a counter for each window.
    *   *Cons*: Traffic spikes at the window boundaries can allow up to twice the rate limit within a short period.
4.  **Sliding Window Log**:
    *   Tracks timestamp records for every single request in a sorted set (like Redis sorted sets). Invalid old timestamps are pruned.
    *   *Pros*: Highly accurate.
    *   *Cons*: High memory usage because every request timestamp must be stored in memory.
5.  **Sliding Window Counter**:
    *   Combines the fixed window algorithm with request rates of the previous window to estimate the current request rate dynamically. Low memory, highly performant approximation.

### 7.2 Circuit Breaker Pattern
Prevents a service from repeatedly trying to execute an operation that is highly likely to fail, saving network resources and thread pools.

```mermaid
stateDiagram-v2
    [*] --> Closed
    Closed --> Open : Failure count threshold exceeded
    Open --> HalfOpen : Cool-down timeout expires
    HalfOpen --> Closed : Test requests succeed
    HalfOpen --> Open : Test request fails
```

*   **Closed**: The circuit is healthy. Requests flow through normally.
*   **Open**: The circuit is failing. Requests fail immediately (fail-fast) without hitting the backend service.
*   **Half-Open**: A cool-down period expires; the system lets a limited number of test requests through. If they succeed, the circuit closes. If they fail, the circuit returns to the Open state.

### 7.3 Retries, Exponential Backoff, and Jitter
When a transient network error occurs, clients should retry, but retrying immediately can overload the target server (Thundering Herd Problem).
*   **Exponential Backoff**: Multiplies the delay time between consecutive retries exponentially (e.g., 1s, 2s, 4s, 8s).
*   **Jitter**: Adds a random variance to the retry delay to prevent all failing clients from retrying at the exact same millisecond.
    $$\text{Sleep Time} = \text{random}(0, \min(\text{MaxBackoff}, \text{Base} \times 2^{\text{attempt}}))$$

---

## 8. Case Study: Distributed URL Shortener (TinyURL)

Let us apply distributed system design concepts to build a scalable URL shortening service.

### 8.1 Requirements
*   **Functional**:
    *   Given a long URL, generate a shorter alias.
    *   Given a short URL, redirect to the original long URL with minimum latency.
    *   Optionally specify a custom expiration date.
*   **Non-Functional**:
    *   Highly available (99.999% availability).
    *   Low latency redirection (< 100ms response time).
    *   Short URLs should be unpredictable.

### 8.2 Back-of-the-Envelope Estimation
*   **Traffic Scale**: 100 Million writes per month.
*   **Read-to-Write Ratio**: 10:1 (Read-heavy service).
*   **Write QPS**:
    $$100,000,000 \text{ URLs} / (30 \text{ days} \times 24 \text{ hours} \times 3600 \text{ seconds}) \approx 40 \text{ writes/sec}$$
*   **Read QPS**:
    $$40 \times 10 = 400 \text{ reads/sec}$$
*   **Storage Estimation**:
    *   Assume 500 bytes per URL mapping record (long URL, short hash, user ID, expiration timestamp).
    *   5-year storage requirements:
        $$100,000,000 \text{ writes/month} \times 12 \text{ months} \times 5 \text{ years} \times 500 \text{ bytes} \approx 3 \text{ Terabytes}$$

### 8.3 System APIs
```http
POST /api/v1/shorten
Content-Type: application/json
{
  "longUrl": "https://example.com/very-long-path-name/info",
  "customAlias": "my-custom-alias", (optional)
  "expireAt": "2026-12-31T23:59:59Z" (optional)
}

Returns:
{
  "shortUrl": "https://tiny.ly/a7B9cd"
}
```

```http
GET /:shortKey -> HTTP 302 Redirect (Location: longUrl)
```

### 8.4 High-Level Architecture

```mermaid
graph TD
    Client[Client Browser] --> LB[Load Balancer]
    LB --> Web[App Servers]
    Web --> Cache[Redis Cache]
    Web --> DB[(NoSQL Database)]
    Web --> KGS[Key Generation Service]
```

### 8.5 Engineering the Key Generation Service (KGS)
To create a short URL, we need to convert a unique ID to Base62 (characters `[a-z, A-Z, 0-9]`). A 7-character Base62 string provides:
$$62^7 \approx 3.5 \text{ Trillion unique keys}$$
This is more than sufficient for our 5-year storage target.

*   **Hashing Collision Problem**: Using MD5/SHA256 of the long URL and truncating to 7 characters causes hash collisions.
*   **KGS Solution**:
    *   A dedicated, lightweight microservice that pre-generates unique 7-character keys and stores them in a Database table (`KeyStore`).
    *   App servers query the KGS to get a new key whenever a write occurs.
    *   To prevent KGS from being a bottleneck, App Servers fetch keys in batches (e.g., 2,000 keys at a time) and buffer them in local memory.
    *   *Concurrency Handling*: Active keys in memory are marked as "allocated" in KGS db to prevent multi-node duplication.

### 8.6 Data Model & Storage Choice
Since we store trillions of independent, unstructured records with simple Key-Value queries (Mapping `shortKey` $\to$ `longUrl`), a relational database (SQL) is not strictly necessary.
*   **NoSQL choice**: Cassandra or DynamoDB offers horizontal scale, low lookup latency, and partition-friendly structures.
*   **Database Schema (DynamoDB / Cassandra style)**:
    *   Primary Partition Key: `shortKey` (String)
    *   Attributes: `longUrl` (String), `userId` (String), `createdAt` (Timestamp), `expireAt` (Timestamp)

### 8.7 Caching & Load Balancing
*   **Caching**: Store the top 20% most active redirect mappings in a Redis Cluster (80/20 Pareto rule). When redirections occur, check Redis first.
*   **Load Balancing**: Use Layer 7 Load Balancer to route based on path (`/api/v1/shorten` routes to write-optimized servers; `/*` short-keys routes to read-optimized redirect servers).

---

## 9. References and Key Literature

1.  **Kleppmann, M.** (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly Media.
2.  **Xu, A.** (2020). *System Design Interview – An insider's guide*. Volume 1 & 2.
3.  **Martin, D.** (2023). *The System Design Primer*. [GitHub Repository](https://github.com/donnemartin/system-design-primer).
4.  **Google Engineering**. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media.
