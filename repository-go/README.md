# common-coding-problems


## Repository pattern

Repository pattern: is to seperate database from application logic. It abstract database implementation by defining interaction with it by the **interface**. The interface is key here which allows developers to implement any database. 

## Design

- Define a repository interface 
- The server only use the repository interface so that actual repository implementation is abstracted.
- The server contruct method has to able to take actual repository aka dependency injection.
- The actual implementation can be in-memory repository, static file or database.
- The main has to instantiate actual repository implementation and pass it as parameter to create new server.
