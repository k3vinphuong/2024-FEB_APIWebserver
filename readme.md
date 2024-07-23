# T2A2 - Protein & Calorie Tracker API - Kevin Phuong

---

## How to use

1. Clone the API to your machine from the Github repo
2. Open the 'src' folder in your terminal
3. Run 'python3 -m venv .venv'
4. Run 'source venv/bin/activate'
5. Run 'pip3 install -r requirements.txt' to install the required python libraries

---

## Explain the problem that this app will solve, and explain how this app solves or addresses this problem.

This API application is meant to give users the ability to keep track of the amount of protein and calories that they intake per meal per food item in the meal. There are many protein trackers that are available to use that track protein however there are not many that can track both calories and protein for each meal per item. 

This application is meant to be used so that users have a lot of free rein in which they wish to track whether that is one full meal or individual pieces of food items in their meal. For example, users can track 1 banana that is present in their home made smoothie and how many calories it provides in comparison to the rest of your meal to be able to know whether to readjust the amount of bananas needed or not needed anymore.

---

## Explain the benefits and drawbacks of this app's underlying database system

The app's database that was chosen is PostgreSQL or Postgres. Using Postgres as the database for my API webserver offers many benefits some of which include:

**Extensibility** - postgres is highly extensible making it super easy to add extra features yourself. What that allows users to do is to come up with functions, data types, languages, all manner of different changes and that can be all installed into the database server just by saying create extension and postgres completes the rest. 

**Security Features** - postgres has inbuilt security, however, it also has extra extensions that allow users to further enhance its security. Postgres provides users with not only parameter security but also app security, meaning if users what to lock down the database system, postgres provides the configurations at the OS level to help configure the process of locking down the environment around the database. 

**ACID Complicance** - Postgres is fully ACID(Atomicity, Consistency, Isolation, Durability) compliant, ensuring that there is realiable transaction and data integrity. 

Postgres despite having numerous amounts of benefits for its use also comes with some drawbacks some of which include the following:

**Open Source** - Postgres is an open source database application therefore meaning it is not owned by one company which could lead it to have many issues in being popularised as opposed to other database softwares that have full control and copyright over their products. This in turn leads to having no warranty and no liability or indemnity protection. 

**Slower Performance** - Postgres due to its relational database structure, when finding a query, has to start from the first row and read through the entire table to find the relevant data which can cause it to perform slower when there is a large number of data that is being stored in the row and columns.

## Explain the features, purposes and functionalities of the object-relational mapping system (ORM) used in this app.

Object relational mapping or ORM is a way to align database structures. It uses metadata secriptors to create a layer between the progrmaming language and relational database by connecting object oriented program code with the database and simplifying the interaction between relational databases and OOP language. ORM also allows developers to perform various data creating, reading, updating and deleting (CRUD) operations in relational databses without using SQL. 

Benefits of using an ORM allow developers to connect the application with the SQL code without rewriting the code therefore increasing the productivity and speeding up development time. ORM also make it easier to maintain applications over time as it automates the object-to-table and table-to-object conversion and requres less code to do so compared to other SQL and procedures. 
