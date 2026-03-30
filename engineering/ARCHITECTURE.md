# Authentication Architecture

## Request Flow

Client Request
→ Authentication Layer
→ Permission Check
→ View
→ Serializer
→ Database
→ Response

---

## Login Flow

User sends credentials
→ Serializer validates input
→ authenticate() verifies credentials
→ Token generated or retrieved
→ Token returned to client

---

## Protected API Flow

Client sends request with token
→ Authentication class verifies token
→ User identified
→ Permission class checks access
→ Request processed

---

## System Layers

1. Authentication Layer

   * identifies user

2. Permission Layer

   * checks access rights

3. View Layer

   * handles request

4. Serializer Layer

   * validates and transforms data

5. Database Layer

   * stores data
