[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/ca)


# Code Challenge

This is a proposed solution to the problem described at [Test.md](Test.md)

## To run, develop, test...

1. Clone the repo
2. Create a virtualenv with Python 3.9.6
3. Activate the virtualenv
4. Install project dependencies
5. Configure the app instance with the .env
6. Execute database migrations   
7. Execute the tests
8. Run the application server

```console
git clone git@github.com:berrondo/ca.git ca

cd ca
python -m venv env
source env/bin/activate

pip install -r requirements-dev.txt
cp contrib/env_sample .env

python manage.py migrate
python manage.py createsuperuser --username admin --email a@a.com --no-input

python manage.py test

python manage.py runserver
```

## **Modeling the User Interaction Event**

The model to represent the user behavior **Event** could be like:

```
Event
   Application (?)
   session_id (UUID) [index]
   category [index]
   name
   data* (Json)
   timestamp (Date) [index] [ordering]
```

- all fields are required!
- appropriate fields are indexed for query performance
- ordered by the time they are generated  
- (*) *data* format varies according to the **Event** *type*
  - each *data* format should have its specific validator
  - each **Event** *type* is identified by *category*+*name*
- the "Application" field will not be modeled given the lack of information.
  - can it possibly came from "trusted clients"?...
  - or maybe it can be inferred from the request (referrer), 
  - or the *data* payload (host? host+path?)

Example **Event** *category*:
 - page interaction
 - form interaction

Example **Event** *name*:
 - pageview
 - cta click
 - submit

So, "*form interaction submit*" is an **Event**  *type* which has its own *data* format which has its specific validator

## **Validations**

how to do it?

## **"Trusted Applications"**

how to do it?

## **Performance Constraints**

To deal with a foresee average of 100 events/second, combined with queries demand, there are some possibilities:

 - use a NoSQL database, like mongodb,
 - to consider Event Sourcing and CQRS technics, segregating queries from commands as the acronym suggests,
 - use some stack to implement queues, i.e.: Celery combined with Redis or RabbitMQ,
 - use some cloud queue technology, like AWS SQS, GCP Cloud Tasks or Azure ASQ,
 - use Kafka!
 - implement kind of a CQRS strategy by receiving all the **Event** requests for register in a dedicated database (or table) and, at another moment, asynchronously processes (parse/validate) the data to another database (or table) optimized for querie (the analytics!)

We suggest to start with the most simple proposed implementation, the last one, i.e,  register the complete **Event** request in a non-blocking manner, leaving the processing (parsing/validation) to be made asynchronously later. This queue of **Event** can be done with the same application database and some cron/command code.

### Race Condition

Seems like there is no need to edit (update) Event records. They need to be collected "as is", "as they happen", to be queried to produce aggregated numbers that answer the questions like:

- which feature is more used? which is rarely used?
- in what order are some features used?

So the strategy of segregating register, parse/validation and consulting seems not only to address the issue of responsiveness, but also that of race condition.

## **The Development Strategy**

### **Python, Django, DRF**

The solution will be presented in **Python** (as demanded) and making use of the **Django** web framework and the **Django Rest Framework** for the API construction

### **V0**

Fairly naive implementation with only a model, an admin site (so analytics personal can perform queries), and a view/serializer for creation/retrieve through a ReSTful API.

- default serializer validations
- indexed fields to speed up queries
- read only admin fields
- basic tests

### **V1**

- better validations
- read only model
- no update via API

### **V2**

The **Event** is received and registered. After that, the parsing/validation is performed.

- segregation between registering. processing, and consulting events

### **Future Versions**

- 

## **The Reusable Client (Python)**

Possible clients could be developed in server or client side languages, i.e., python, javascript...
