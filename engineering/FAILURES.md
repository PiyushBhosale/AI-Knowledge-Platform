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
