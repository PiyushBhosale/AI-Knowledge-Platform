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

# Day 3 — Serializers, Validation & Scalable API Design

---

## 🎯 Goal

Understand how to build clean, secure, and scalable APIs using proper backend architecture.

---

# 🔹 1. Role of Serializer

A serializer acts as a bridge between:

* incoming request data
* database models

It is responsible for:

* validating input data
* transforming data
* controlling what is exposed in API responses

---

# 🔹 2. Why Not Use Direct Query Output

Directly returning database query results:

* lacks validation
* exposes risk of sensitive data leakage
* makes API hard to maintain and extend

Using a structured layer improves:

* security
* flexibility
* readability

---

# 🔹 3. Separation of Responsibilities

Backend should be divided into layers:

* Query Layer → fetches data from database
* Serializer Layer → validates and transforms data
* Response Layer → controls output and structure

Each layer has a separate responsibility.

---

# 🔹 4. Validation Concept

Validation ensures:

* only correct and meaningful data enters the system
* system remains stable and predictable

Types of validation:

* field-level → checks individual fields
* object-level → checks relationship between fields

---

# 🔹 5. Why Validation Layer is Important

Without validation:

* incorrect data enters database
* system behavior becomes unpredictable
* debugging becomes difficult

Validation acts as a **defensive shield**.

---

# 🔹 6. Handling Invalid Data

When invalid data is received:

* it should not be saved
* system should return structured error messages

This prevents corruption of data.

---

# 🔹 7. Security Principles Learned

* never expose sensitive fields like passwords
* always store passwords in hashed form
* never trust incoming data blindly

Security must be enforced at multiple layers.

---

# 🔹 8. Scalability Insight

Fetching all data at once:

* increases memory usage
* slows down system
* leads to poor performance

Scalable systems:

* limit data per request
* use pagination
* optimize queries

---

# 🔹 9. Key Misconception Cleared

Serializer improves:

* structure
* validation

But does NOT solve:

* performance issues
* large data loading

Performance must be handled at the query level.

---

# 🔹 10. Engineering Thinking Developed

Always ask:

* what happens if data grows 100x?
* where is the bottleneck?
* what will fail first?

---

# 🔹 11. Common Mistakes

* returning raw query data
* skipping validation
* exposing sensitive information
* loading all data without limits

---

# 🔹 12. Final Understanding

A well-designed backend system:

* separates concerns
* validates data properly
* protects sensitive information
* plans for scalability from early stage

---

# 🔹 13. One-Line Summary

Serializer improves data handling and security, while scalability must be handled separately through efficient querying and pagination.


# Day 4

## What I Learned

* Authentication vs Authorization
* Token-based authentication system
* Login flow in backend
* Serializer validation pipeline
* Difference between serializer.data and validated_data
* Request lifecycle in Django (authentication before view)

## What I Built

* Login API using serializer
* Token generation system
* Protected API using TokenAuthentication
* User access control using permission classes

## Issues Faced

* Incorrect serializer type (used ModelSerializer instead of Serializer)
* Token installation confusion
* Understanding authentication flow

## Fixes Applied

* Used Serializer for login instead of ModelSerializer
* Added authtoken correctly from DRF
* Understood authentication pipeline

## Key Learnings

* Authentication happens before the view layer
* Serializer is responsible for validation and transformation
* Tokens act as identity proof instead of sending passwords repeatedly
* Proper abstraction layers are critical in backend systems

## Security Learnings

* Never send password in every request
* Tokens must be protected like passwords
* Token leakage = full account compromise

## System Thinking

* Authentication is part of request lifecycle
* System bottlenecks propagate from database → backend → network
