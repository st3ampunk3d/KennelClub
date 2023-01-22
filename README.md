# Overview
This software integrates python (using SQLite3) and and SQL relational Database to display membership information for a kennel club.
On startup the software checks for the existence of "kennelClub.db". If the database is missing a new one is created and populated with generic values for demonstration purposes.
There is a tree list view that lists all of the members of the kennelclub and their corrosponding dogs. Double clicking on an item in tree will display the ID card for the member and or dog that was selected.
Clicking the trash can icon will delete the related member or dog from the relational database and update the user interface.
Clicking the green plus icon on the member ID card will add a new row to the Dogs table in the relational database. This dog is a hard-coded entity currently due to time constraints.
Clicking The blue swap arrow icon on the dog ID card will allow you to transfer ownership of the dog to the member currently displayed.
There are other icons on the screen that at current are disfunctional.

The purpose for writing this software was to expand my knowledge of relational databases. I also wanted to learn more about perpetuating user data after an application is closed. A database is a good way to accomplish this as it is easily read from and written to.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

See a demo of the program here: https://www.youtube.com/watch?v=I3uAnUCmXzs

# Relational Database

The database holds information about the members of a Kennel Club and their dogs. It also contains generic information about the dog breeds found within the club.

Tables
- Members -- one to many -- < Dogs > -- Many to One -- Breeds

Members               Dogs                Breeds
    ID                  ID                    ID
    Name                Name                  Name
    Address             Owner ID              Size
    Phone number        Breed ID              Life Expectance
    Email               color                 Energy Level
    Date joined         Date of Birth         tendencey to bark
    photo               photo                 Trainability
                                              Amount of shedding
                                              General description

# Development Environment

The database was diagramed and the script to create the database was made using mySQLworkbenck

The main application was made with
Python 3.11
PyQt5 - framework for creating user interfaces
SQlite3 - python package to connect to databases and pass SQL queries from within pythong

# Useful Websites

{Make a list of websites that you found helpful in this project}

- Python https://www.python.org/
- PyQt https://doc.qt.io/qtforpython/
- SQLite3 https://www.sqlitetutorial.net/

# Future Work

- Make all buttons funcional.
- Create forms and functions to add new Members and dogs instead of using hard-coded test cases.
- Create forms to update existing members and dogs.
- Cleanup the interface
- Figure out why adding a new dog adds 2 dot ID cards to the gui.