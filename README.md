# Abierto
Automated door opening system for your phone


# Functionality Use Cases

Use case: User wants to open the door
    1. User sends a command requesting the door to be opened to the API
    2. Cloud server recived the request and sets the database state to "activate door"

Use case: Raspberry Pi checks into server 
    1. Raspberry Pi polls the behaviour API on the cloud server. The database state is "do nothing"
    2. Cloud server responds that the database state is "do nothing"
    3. Raspberry pi waits 1 or 2 seconds
    4. repeat forever

    1a. The database state is "activate door"
        1a.1. Cloud server responds that the database state is "open door"
        1a.2. Cloud server sets the database state to "do nothing"
        1a.2. Raspberry Pi commands the arduino to "open door"
        
    1b.1 There has been a delay of more than 10 seconds since the previous Raspberry Pi check in
        Cloud server sets the database state to "do nothing"


Agents: 
Cloud server
Database
Raspberry Pi
Arduino

