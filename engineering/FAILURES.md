# Failures

## Plain Text Password Issue

### Problem

Some users stored password as plain text

### Cause

Used incorrect method to create users

### Impact

* Security vulnerability
* Sensitive data exposure risk

### Fix

* Used set_password() for existing users
* Updated API to not expose password

### Learning

Security is not automatic — must be enforced explicitly

# Failures

## Wrong Serializer Type

### Problem

Used ModelSerializer for login

### Cause

Incorrect abstraction choice

### Impact

System error (missing Meta class)

### Fix

Used normal Serializer

---

## Token Installation Error

### Problem

Tried installing authtoken separately

### Cause

Misunderstanding of package structure

### Fix

Used DRF built-in authtoken module

---

## Authentication Misunderstanding

### Problem

Assumed authentication happens in view

### Cause

Lack of understanding of request lifecycle

### Fix

Learned authentication happens before view


# Failures

## No Pagination Issue

### Problem

API returned all users at once

### Cause

Used .all() without limiting results

### Impact

* high memory usage
* slow response time
* poor scalability

### Fix

Implemented pagination

---

## Large Page Size Issue

### Problem

Large data returned in single request

### Impact

* slow API
* network latency
* frontend lag

### Learning

Page size must be controlled carefully
