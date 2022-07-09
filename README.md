# Spark
Spark is a general-purpose distributed data processing engine that is suitable for use in a wide range of circumstances. On top of the Spark core data processing engine, there are libraries for SQL, machine learning, graph computation, and stream processing, which can be used together in an application. Programming languages supported by Spark include: Java, Python, Scala, and R. Application developers and data scientists incorporate Spark into their applications to rapidly query, analyze, and transform data at scale. Tasks most frequently associated with Spark include ETL and SQL batch jobs across large data sets, processing of streaming data from sensors, IoT, or financial systems, and machine learning tasks.

## Resilient Distributed Dataset (RDD)
RDD was the primary user-facing API in Spark since its inception. At the core, an RDD is an immutable distributed collection of elements of your data, partitioned across nodes in your cluster that can be operated in parallel with a low-level API that offers transformations and actions.


### Kafka 
A distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

### Stream Processing
Stream processing is the practice of taking action on a series of data at the time the data is created. Historically, data practitioners used “real-time processing” to talk generally about data that was processed as frequently as necessary for a particular use case. Stream processing often entails multiple tasks on the incoming series of data (the “data stream”), which can be performed serially, in parallel, or both. This workflow is referred to as a stream processing pipeline, which includes the generation of the stream data, the processing of the data, and the delivery of the data to a final location.

Stream Processing is the act of continuously incorporating new data to compute a result， and is a golden key if you want ananlytics results in real time。


### Batch Processing
Batch processing is where the processing happens of blocks of data that have already been stored over a period of time.