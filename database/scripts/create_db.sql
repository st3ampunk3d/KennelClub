-- Enable Foreign Key support
PRAGMA foreign_keys = ON;

-- -----------------------------------------------------
-- Table Members
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS "Members" (
  "Member_id" INTEGER PRIMARY KEY NOT NULL,
  "name" VARCHAR(45) NOT NULL,
  "City" VARCHAR(45) NOT NULL,
  "Email" VARCHAR(45) NOT NULL,
  "Phone" VARCHAR(45) NOT NULL,
  "membershipDate" DATE NOT NULL,
  "photo" VARCHAR(45));
CREATE UNIQUE INDEX IF NOT EXISTS "Owner_id_UNIQUE" on "Members" ("Member_id");
CREATE UNIQUE INDEX IF NOT EXISTS "name_UNIQUE" on "Members" ("name");;

-- -----------------------------------------------------
-- Table Breeds
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Breeds (
  "Breed_id" INTEGER PRIMARY KEY NOT NULL,
  "name" VARCHAR(45) NOT NULL,
  "size" INTEGER NOT NULL,
  "lifeExpectancy" INTEGER NOT NULL,
  "energyLevel" INTEGER NOT NULL,
  "barkingLevel" INTEGER NOT NULL,
  "trainable" INTEGER NOT NULL,
  "shedding" INTEGER NOT NULL,
  "description" VARCHAR(100) NOT NULL);
CREATE UNIQUE INDEX IF NOT EXISTS "Breed_id_UNIQUE" on "Breeds" ("Breed_id");
CREATE UNIQUE INDEX IF NOT EXISTS "name_UNIQUE" on "Breeds" ("name");;

-- -----------------------------------------------------
-- Table Dogs
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Dogs (
  "Dog_id" INTEGER PRIMARY KEY NOT NULL,
  "name" VARCHAR(45) NOT NULL,
  "Breed_id" INTEGER NOT NULL,
  "Owner_id" INTEGER NOT NULL,
  "color" VARCHAR(15) NOT NULL,
  "dob" DATE NOT NULL,
  "photo" VARCHAR(45),
  FOREIGN KEY ("Breed_id") REFERENCES "Breeds" ("Breed_id"),
  FOREIGN KEY ("Owner_id") REFERENCES "Members" ("Member_id"));
CREATE INDEX IF NOT EXISTS "fk_Dog_Breed1_idx" on "Dogs" ("Breed_id");
CREATE INDEX IF NOT EXISTS "fk_Dogs_Members1_idx" on "Dogs" ("Owner_id");
CREATE UNIQUE INDEX IF NOT EXISTS "Dog_id_UNIQUE" on "Dogs" ("Dog_id");;

-- -----------------------------------------------------
-- Populate the Breeds Table
-- -----------------------------------------------------
Insert Into breeds
VALUES
	/*ID  Name                  size    L   E  B  T  S  description*/
	(1,           "Doberman",  "Large", 11, 5, 3, 5, 4, "Description"),
  (2,             "Beagle",  "Small", 10, 3, 1, 4, 3, "Description"),
  (3, "Labrador Retriever",  "Large", 10, 3, 1, 5, 4, "Description"),
  (4,         "Great Dane",  "Giant",  7, 5, 3, 5, 4, "Description"),
  (5,            "Bulldog", "Medium", 10, 4, 4, 5, 1, "Description"),
  (6,          "Dachshund",  "Small",  8, 3, 2, 4, 3, "Description");

-- -----------------------------------------------------
-- Populate the Members table
-- ----------------------------------------------------- 
Insert Into members
VALUES
  /*ID  Name                City               Email                          Phone          Date Joined*/
  ( 1,      "Blue Falcon",        "Big City", "radley.crown@bluefalcon.com", "258-332-5266", "2012-05-20", "blue_falcon.png"),
  ( 2,    "Charles Brown",     "Minneapolis",   "charlie.brown@peanuts.com", "426-563-2665", "2015-06-09", "charlie_brown.png"),
  ( 3, "Emily Elizableth", "Birdwell Island",      "e.elizabeth@bigred.com", "484-373-3364", "2015-09-07", "emily_elizabeth.png"),
  ( 4,    "George Jetson",      "Orbit City",  "george@spacelysprokets.net", "526-353-8766", "2018-01-30", "george_jetson.png"),
  ( 5,      "Jonny Quest",    "Florida Keys",         "jonny@questlabs.org", "566-697-8378", "2018-04-10", "jonny_quest.png"),
  ( 6,     "Jon Arbuckle",          "Munice", "jonarbuckle@thatdarncat.com", "664-273-4353", "2019-08-02", "job_arbuckle.png"),
  ( 7,     "Muriel Bagge",         "Nowhere",      "muriel@havecourage.com", "268-724-3364", "2019-11-13", "muriel_bagge.png"),    
  ( 8,  "Norville Rogers",      "Coolsville",       "shaggy@mysteryinc.org", "726-629-3662", "2020-06-14", "norville_rogers.png"),
  ( 9,             "Rick",        "New York",            "just_rick@tj.net", "866-263-5379", "2021-12-15", "rick.png"),
  (10,  "Sherman Peabody",       "Manhattan",        "mr.peabody@WABAC.edu", "732-263-9269", "2023-01-11", "sherman_peabody.png");

-- -----------------------------------------------------
-- Populate the Dogs table
-- -----------------------------------------------------
Insert Into dogs
VALUES
 /*ID  Name          BreedID  OwnerID  Color    DOB*/
  ( 1,    "Dynomutt", 1,        1,     "grey", "2015-09-10", "dynomutt.png"),
  ( 2,      "Snoopy", 2,        2,    "white", "2015-10-02", "snoopy.png"), 
  ( 3,    "Clifford", 3,        3,      "red", "2021-11-10", "clifford.png"),   
  ( 4,       "Astro", 4,        4,     "grey", "2016-09-23", "astro.png"),
  ( 5,      "Bandit", 5,        5,    "white", "2018-09-18", "bandit.png"),
  ( 6,        "Odie", 6,        6,   "yellow", "2017-06-19", "odie.png"),
  ( 7,     "Courage", 2,        7,     "pink", "2020-02-18", "courage.png"),
  ( 8,  "Scooby-Doo", 4,        8,    "brown", "2015-09-13", "scooby_doo.png"),
  ( 9,       "Spike", 5,        9,     "grey", "2013-02-10", "spike.png"),
  (10, "Mr. Peabody", 2,       10,    "white", "2014-03-07", "mr_peabody.png"),
  (11, "Scrappy-Doo", 4,        8,    "brown", "2022-09-22", "scrappy_doo.png");