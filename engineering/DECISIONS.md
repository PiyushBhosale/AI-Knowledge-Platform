# Decisions

## Custom User Model

### Decision

Use custom User model from Day 2

### Reason

* Flexibility for future features
* Avoid migration issues later

### Tradeoff

* Slight complexity at start
* But prevents major issues later

---

## Password Handling

### Decision

Use create_user() and set_password()

### Reason

* Ensures password hashing
* Follows Django security standards

### Tradeoff

* Requires awareness from developer

# Decisions

## Authentication Method

### Decision

Use Token Authentication (DRF)

### Reason

* Simple to implement
* Good for learning authentication flow
* Easy to manage and revoke

### Tradeoff

* Requires DB lookup on every request
* Not ideal for very large-scale systems

---

## Serializer for Login

### Decision

Use normal Serializer instead of ModelSerializer

### Reason

* Login does not directly map to database model creation
* Only validates credentials

### Tradeoff

* Requires manual validation logic

---

## Token Storage Design

### Decision

Store tokens in separate table

### Reason

* Separation of concerns
* Flexibility (multiple tokens, revocation)
* Cleaner user model

### Tradeoff

* Additional DB query required
