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
