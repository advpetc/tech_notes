## Vending Machine

1. no need to talk about how **many** user using (distribute system design)

### Data

1. item
2. vending machine

### Action

- buy/purchase: input (item id, money) and output (item, remain money)
  - input and return type: int, Item
  - exceptions (could talk later in details): if there is no more items remaining, or there is not enough money
  - could talk about use case: assumption (money for change is efficient), **use the most familiar one for your use case.**

### Class

- Item (first design the most fundmental class)
  - price: int
  - name/id: int/string
  - **type**
- Vending Machine
  - money remaining: int
  - colllection of Item: unordered_map<Item, count> -> unordered_map<type, count>
    - Item: should represent type of item instead of specific item -> add a field in item for **type**
  - buy/purchase API
  - more: if there are multiple tracks

## Elevator Simulator

start from use case (discuss with the interviewer):
1. show level button or just up and down then select inside the elevator
2. swipe card to validate or not
3. support for multiple elevator -> design elevator system
4. how to schedule (it could be discussed later): support different types of requests
5. What is elevator's state in each "iteration" **(per floor)**

### State to determine attribute

- which floor
  - first floor: up or down (outstanding request to go up or down), open or close door (people load or unload from the elevator) -> next iteration is on second floor (if go up) -> do the same thing for 1st floor
- move up or move down
- weight/headcount and capacity -> if overload
- what to do when reach a floor
  - what to determine to open or not: depends on the request (from outside or inside people)
  - after open door: get in and get out -> next requests
  - determine whether to change the direction

### Data

- maxCapacity
- maxFloor
- load
- location

### Action

- open/close door
- floor
- going up or down

### Class

- System Management (Building)
  - how many elevator
  - going up or down
  - map<Elevator, vector<Request>>
- Elevator
  - vector<Request>: good for encapsulation
- User (no need -> too detailed)
- Floor (no need -> too detailed and not relate to action)
- Request
  - up and down
  - from which floor make the request

### Scheduling (Final Step)

- Each elevator makes its own decision
  - check Up/Down requests
  - the 1st elevator arriving at the floor takes the request with the same direction
  - the elevator loads ppl at the floor and handles their requests

