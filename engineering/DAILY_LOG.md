# Day 1

## Learned
REST API basics

## Built
Django project
First API

## Issues
-

## Improvements
-

# Day 2

## What I Learned

* Django Models = database tables
* Migrations = version control for database
* Custom User Model importance
* Password hashing mechanism
* Difference between create() vs create_user()

## What I Built

* Custom User model
* Admin integration
* User listing API

## Issues Faced

* Passwords stored in plain text for some users
* Password exposed in API response

## Root Cause

* Used wrong user creation method (create instead of create_user)
* Used default admin instead of UserAdmin earlier
* Included password field in API

## Fixes Applied

* Used set_password() to hash existing users
* Switched to proper UserAdmin
* Removed password from API response

## Key Learnings

* Frameworks don’t enforce correctness — developer must use them properly
* Security mistakes are easy and dangerous
* Always validate how data is stored and exposed

## What Can Break in Future

* Large number of users → API will become slow
* No pagination → memory issue
* No authentication → security risk
