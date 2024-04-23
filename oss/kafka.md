# Apache Kafka
https://kafka.apache.org/ <br>
https://github.com/apache/kafka

## Overview
Apache Kafka is an event streaming platform.
- Publish (write) / Subscribe (read) to streams events
- Store streams of event
- Processing Streams

## Architecture
### Topic
- Topic is a unit of message group, consisted of more than one partition

### Partition
- Partition is a unit for storing message
- Message will be store in partition orderly
- Kafka realize distributed processing and redundancy by dividing topic into multi partition

### Producer
- Producer sends message to kafka cluster
- Message will be allocated to partition by round robin or custom logic

### Consumer
- Consumer reads messages from kafka cluster
- One or more consumers form a consumer group, where they collectively consume partitions in parallel

### Broker
- Broker is server process that make up kafka cluster, responsible for receiving, persisting, and replicating messages