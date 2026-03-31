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

# Data Retrieval Architecture

## Request Flow with Pagination

Client Request
→ Query Parameters (page, filters)
→ Backend Logic
→ Database Query (LIMIT, OFFSET)
→ Serializer
→ Response

---

## Filtering Flow

Client Request with filters
→ Backend extracts parameters
→ Query modified dynamically
→ Database returns filtered data

---

## System Layers Involved

1. Request Layer

   * receives query params

2. Backend Layer

   * builds query

3. Database Layer

   * executes optimized query

4. Response Layer

   * returns paginated data
