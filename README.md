# Spark
Spark is a general-purpose distributed data 
processing engine. On top of the Spark core data processing engine, there are libraries for SQL, machine learning, graph computation, and stream processing, which can be used together in an application. Application developers and data scientists incorporate Spark into their applications to rapidly query, analyze, and transform data at scale. Tasks most frequently associated with Spark include ETL and SQL batch jobs across large data sets, processing of streaming data from sensors, IoT, or financial systems, and machine learning tasks.
Spark supports multiple workloads through a
unified engine comprised of Spark components as libraries accessible
via unified APIs in popular programing languages, including Scala,
Java, Python, and R. And finally, it can be deployed in different
environments, read data from various data sources, and interact with
myriad applications

## Resilient Distributed Dataset (RDD)
RDD was the primary user-facing API in Spark since its inception. At the core, an RDD is an immutable distributed collection of elements of your data, partitioned across nodes in your cluster that can be operated in parallel with a low-level API that offers transformations and actions.


# Kafka 
A distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

## Glossary

- Kafka Message: In one line, Message in Kafka is an information which travels from the producer to a consumer through Apache Kafka.
- Kafka Topics: like a table in a database. Basically, Kafka maintains feeds of messages in categories. And, messages are stored as well as published in a category/feed name that is what we call a topic. In addition, all Kafka messages are generally organized into Kafka topics.
- Kafka Producers: You cannot query topics, instead use Kakfa producers to send data and kafka consumers to read the data. 
- Kafka Partitions: Topics are split in partitions

### Stream Processing
Stream processing is the practice of taking action on a series of data at the time the data is created. Historically, data practitioners used “real-time processing” to talk generally about data that was processed as frequently as necessary for a particular use case. Stream processing often entails multiple tasks on the incoming series of data (the “data stream”), which can be performed serially, in parallel, or both. This workflow is referred to as a stream processing pipeline, which includes the generation of the stream data, the processing of the data, and the delivery of the data to a final location.

Stream Processing is the act of continuously incorporating new data to compute a result， and is a golden key if you want an anlytics results in real time。

### Batch Processing
Batch processing is where the processing happens of blocks of data that have already been stored over a period of time.

Under the batch processing model, a set of data is collected over time, then fed into an analytics system. In other words, you collect a batch of information, then send it in for processing.
Under the streaming model, data is fed into analytics tools piece-by-piece. The processing is usually done in real time.

