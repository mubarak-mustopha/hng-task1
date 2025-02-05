## HNG Intership Task 1

### Number Classification API Built Flask
This is a simple API which returns interesting properties and facts about any given number


### API DOCUMENTION

#### Base URL
`https://hngtask1.vercel.api`

#### Endpoint
GET `/classify_number`

#### Parameters

| Name    | Type | Required | Description |
|---------|------|----------|-------------|
| number  | int  | Yes      | The number to classify (must be passed as a query parameter). |

#### Example Request
GET `/classify_number?number=371`

#### Successful Response (`200 OK`)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)

```json
{
"number": "alphabet",
    "error": true
}
```
