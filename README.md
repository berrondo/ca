[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/ca)


# Code Challenge

This is a proposed solution to the problem described at [Test.md](Test.md)

## **Modeling the User Interation Event**

The model to represent the user behavior **Event** could be like:

```
Event
   Application (?)
   session_id (UUID) [index]
   category [index]
   name
   *data (Json)
   timestamp (Date) [index]
```

Where *data* format varies according to the **Event** type, and each *data* format should have its specific validator

Each **Event** type is identified by *category*+*name*

Some **Event** *category*:
 - page interaction
 - form interaction

Some **Event** *name*:
 - pageview
 - cta click
 - submit

So, *form interaction submit* is an **Event**  type which has its own *data* format which has its specific validator

## **Load Performance**

To deal with a foresee average of 100 events/second combined with queries demand, there are some possibilities:

 - use a NoSQL database, like mongodb,
 - to consider Event Sourcing and CQRS technology, segregating queries from commands as the acronym suggests,
 - use some stack to implement queues, perhaps Celery combined with Redis or RabbitMQ,
 - use some cloud queue technology, like AWS SQS, GCP Cloud Tasks or Azure ASQ, or even Kafka.
 - implement kind of a CQRS strategy by receiving all the **Event** requests for register in a dedicated database (or table) and, at another moment, asynchronously, process (parse/validate) the data to another database (or table) optimized for queries (the analytics!)

We suggest start with the most simple implementation of the last one, i.e,  register the complete **Event** request in a non-blocking manner, leaving the processing (parsing/validation) to be made asynchronously later. This queue of **Event** can be done with the same application database and some cron/command code.

## **The Development Strategy**

### **Python, Django, DRF**

The solution will be presented in **Python** (as demanded) and making use of the **Django** web framework and the **Django Rest Framework** for the API construction

### **V0**

For the first development iteration, a simple Django application consisting of a single model, the **Event**, and (proposed) "Django Admin" forms to query the registered events

### **V1**

In a second row, two steps will be introduced: first, the **Event** is received and registered. After that, the parsing/validation is performed.

## **The Client**

Possible clients could be developed in server or client side languages, i.e., python, javascript...
