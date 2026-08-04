# Class-Notez

## 04-08-2026

### Data

    Data - It is raw unprocessed facts or figures , It has no context or meaning on its own.
        Example - A list of transaction amount ; 100 ,200 ,300 ,500 etc.

### Information

    Information - It is the data that has been processed, organised or structured to make it meaninigful.
        Example - Avg marks of students in class is 86.6 , and topper scored 92.

### Database

    Database - A database is an organised collection of structured information, or data, typically stored electronically in a computer system, that can be easily accessed managed and updated.
    It represents data in a structured way to reduce redundancy and is easy to retrieve, retrieve, inser, update and delete the data / information.
    A database is usually controlled by a database management system (DBMS).
    Example of a database : Customer details, Product information, Sales records etc.
        A schools database stores information about students,teachers, courses, and grades in organized interlinked way.

    Advantages: 
        1. Searching is made easier by using only queries instead of the alr used program in file-based systems, i.e. file handling.
        2. Data is easily accessible, manageable, and updated.

### DBMS

    DBMS - A Database Management System (DBMS) is a software application that allows users to create and manage databases.
    It provides a user-friendly interface between database and its users for performing various database operations such as creating tables, inserting, updating, deleting, and retrieving data.
    It allows users to create, read, update and delete teh Data in the Database.
    DBMS also provides features such as security, concurrency control, backup and recovery, and data integrity.
    Example of a DBMS : MySQL, Oracle, SQL Server, PostgreSQL, etc.
    Its what IDE is to programming in this case what database is to DBMS.

### File system

    Before DBMS came into use traditional File processing system were in use, where each application had its own separate file and its version to store data and access them , updation became a headache.
    Disadvantage:
         1. Data redundancy and Inconsistency (Incorrect Version, Updation Issues)
            Different application maintaining their own files , same data eg student name or address , often they got duplicated across multiple files . This wasteed stograe space leads to 'Inconsistency' . If data was updated for one file and not other , conflicting values would exist.
        2. Difficulty in Accessing Data
            To retrieve data in a file system , you had to write custom code (Program) for each type of query.
            If you needed student marks , you wrote a program. If you needed course info , another program.Makign it very Time consuming.
        3. Data Isolation
            Data is Scattered in differnet files, often different formats, making it hard to retrieve data from multipel sources.
        4. Integrity Problems (Validation Not Performed)
            Data values have to satisty certain 'Consistency Constraints' eg: account balance must not go below zero, Enforcing these constraints was difficult.Enforcing these contrains require additional coding to every application program, especially when constraint change.
        5. Atomicity Problems
            A computer system like an device is subject to failute , If a failure occures duing a transaction 
            e.g. bank transfer, it must be ensures that either `all` operations are completeed, or `none` are , to keep data consistent. File systems couldn't guarantee this.

            Transaction Between A and B 
            if A has initial 1000 . it debits 500 then its balance is not 500 but i wont `Commit` it as A doesnt have enough balance.Creating a failure situation thus i wouldnt be able to follow with the situation where B which has 0 iniital balance would be Credited 500 balance from A  and increase it Balance to 500 thus i cant commit it.
            In this case for A `Rollback` and for B `No Change` would happen.
            Atomicity in DBMS ensures that even if failure occurs, the data remains consistent by either completing all operations or none at all.

        6. Concurrent Access Anomalies 
            Multiple Users accessing same data simultaneously leads to uncontrolled overwrites and irratic results, and inconsistent data eg two people booking the same seat at same time.
        