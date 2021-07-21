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

## **Thinking About The Problem**

Recording how large numbers of users interact with a variety of systems can be challenging.

On the client side, the cost of sending these events should not impact the user experience.

To do so, the server side of this monitoring application must expect a large concurrent flood of these events and to be able to receive and process them without letting the client side and its users experiencing unpleasantness delays, i.e., latency.

The knowledge-base under the names "Event Sourcing" / "CQRS" come to rescue!

Simply put, we will be using the basic "Event Sourcing"'s premise of indefinitely register a stream of events, capable of "to tell a history", and only register them without ever update or delete them, and - by the "CQRS" side,  as the acronym says - the premise of segregation of the responsibility of doing "commands" and "queries" with the data.

## **So, The Assumptions**

Thinking "Event Sourcing / CQRS", we are assuming that:

- The Event record will never change! So the application will not provide the means to do so: no PUT/UPDATE or DELETE.

- The Event will be recorded as is, in raw manner, at a specific backend optimized for that. And this is the sole responsibility of that backend.

- The processing - parsing, validation - of the Event will happen later, **commanded** by a scheduled task.

- The result of that processing will be available in another specific backend optimized for **queries**.

- To facilitate validations, all fields will be considered required.

- This is a toy (naive) implementation, aimed only to demonstrate these assumptions.

## **Modeling the User Interaction Event**

The model to represent the received user behavior **"RawEvent"** would be like:

```
RawEvent
   event_payload (Json)
   status(received, processed, invalid) [index]
```

After processing, the model to represent the user behavior **Event** could be like:

```
Event
   Application (?)
   session_id (UUID) [index] [ordering 1]
   category [index]
   name
   data* (Json)
   timestamp (Date) [index] [ordering 2]
```

- all fields are required!
- appropriate fields are indexed for query performance
- ordered by the time they are generated in a session  

### **Validations**

- (*) **Event**.*data* format varies according to the **Event** *type*
  - each *data* format should have its specific validator
  - each **Event** *type* is identified by *category*+*name*

- Example **Event** *category*:
  - page interaction
  - form interaction

- Example **Event** *name*:
  - pageview
  - cta click
  - submit

- So, "*form_interaction.submit*" is an **Event**  *type* which has its own *data* format which has its specific validator

### **"Trusted Applications"**

- the **Event**."Application" field will not be modeled given the lack of information.
  - can it possibly came from "trusted clients"?...
  - or maybe it can be inferred from the request (referrer), 
  - or the *data* payload (host? host+path?)
  
There are various ways to allow only "trusted applications" to send their events to the system (but none will be implemented):

- Register applications as users of the system,

- Basic authentication token,

- List of trusted IPs

## **Performance Constraints**

As stated by our Assumptions, to deal with foresee average of 100 events/second, we are using an "Event Sourcing / CQRS" approach. We believe it also address the Race Condition issue.

Otherwise, there are other possibilities:

 - use some stack to implement queues, i.e.: Celery + Redis,
 - use some cloud queue technology, like AWS SQS, GCP Cloud Tasks or Azure ASQ,
 - use a NoSQL database, like mongodb,
 - use ElasticSearch,   
 - use Kafka!

## **The Development Strategy**

### **Python, Django, DRF**

The solution will be presented in **Python** (as demanded) and making use of the **Django** web framework and the **Django Rest Framework** for the API construction

### **V0, the MVP**

Fairly naive implementation with only a model, an admin site (so analytics personal can perform queries), and a view/serializer for creation/retrieve through a ReSTful API.

- default serializer validations
- indexed fields to speed up queries
- read only admin fields
- basic tests

### **V1**

- segregation between receiving, processing, and querying events
- scheduled processing task  
- read only models
- no delete/update via API or admin site

### **V2**

- better validations
- better filtering (search)
- an example client

### **Future Versions**

- 

## **The Reusable Client (Python)**

Possible clients could be developed in server or client side languages, i.e., python, javascript...
