# Object Oriented Design

## Design Pattern

> https://github.com/JakubVojvoda/design-patterns-cpp

### Builder

1. if there are a lot of fields in a class, cannot put them all in as parameters in the constructor.
2. solution 0: define `final` and optional data fields in the class (no need to initialize in the constructor => bad because it could generate a lot of dfferent types of constructors.
3. solution 1: use setter and getter => bad because if want to create an object, user has to call all the setters and getters (constructor isn't doing what it is supposed to do: dangerous in multi-threading) => encapsulation is destroyed => e.g. setters' member field might not want to be changed OR setters are not changed in the desire way 
4. solution 2: encapsulate the related fields into a single function, use an abstract class to manage the top level abstraction and some concrete subclasses to manage the specific constructions.

* Core: create a builder class for top level abstraction and subclasses for specific constructions. When implementing, don't forget to `#include "builder.hpp"`.

```c
/*
 * C++ Design Patterns: Builder
 * Author: Jakub Vojvoda [github.com/JakubVojvoda]
 * 2016
 *
 * Source code is licensed under MIT License
 * (for more details see LICENSE)
 *
 */

#include <iostream>
#include <string>

/*
 * Product
 * the final object that will be created using Builder
 */
class Product
{
public:
  void makeA( const std::string &part )
  {
    partA = part;
  }
  void makeB( const std::string &part )
  {
    partB = part;
  }
  void makeC( const std::string &part )
  {
    partC = part;
  }
  std::string get()
  {
    return (partA + " " + partB + " " + partC);
  }
  // ...
  
private:
  std::string partA;
  std::string partB;
  std::string partC;
  // ...
};

/*
 * Builder
 * abstract interface for creating products
 */
class Builder
{
public:
  virtual ~Builder() {}
  
  Product get()
  {
    return product;
  }
  
  virtual void buildPartA() = 0;
  virtual void buildPartB() = 0;
  virtual void buildPartC() = 0;
  // ...

protected:
  Product product;
};

/*
 * Concrete Builder X and Y
 * create real products and stores them in the composite structure
 */
class ConcreteBuilderX : public Builder
{
public:
  void buildPartA()
  {
    product.makeA( "A-X" );
  }
  void buildPartB()
  {
    product.makeB( "B-X" );
  }
  void buildPartC()
  {
    product.makeC( "C-X" );
  }
  // ...
};

class ConcreteBuilderY : public Builder
{
public:
  void buildPartA()
  {
    product.makeA( "A-Y" );
  }
  void buildPartB()
  {
    product.makeB( "B-Y" );
  }
  void buildPartC()
  {
    product.makeC( "C-Y" );
  }
  // ...
};

/*
 * Director
 * responsible for managing the correct sequence of object creation
 */
class Director {
public:
  Director() : builder() {}
  
  ~Director()
  {
    if ( builder )
    {
      delete builder;
    }
  }
  
  void set( Builder *b )
  {
    if ( builder )
    {
      delete builder;
    }
    builder = b;
  }
  
  Product get()
  {
    return builder->get();
  }
  
  void construct()
  {
    builder->buildPartA();
    builder->buildPartB();
    builder->buildPartC();
    // ...
  }
  // ...

private:
  Builder *builder;
};


int main()
{
  Director director;
  director.set( new ConcreteBuilderX );
  director.construct();
  
  Product product1 = director.get();
  std::cout << "1st product parts: " << product1.get() << std::endl;
  
  director.set( new ConcreteBuilderY );
  director.construct();
  
  Product product2 = director.get();
  std::cout << "2nd product parts: " << product2.get() << std::endl;
  
  return 0;
}
```

### Abstract Factory

1. polymorphism: use an abstract class to include the shared method `getName()` 
2. multiple different classes create the same type of object with the shared method for creations, update and other _CRUD_ operations.
3. it's a easy to extend: if you want to add a new type and add its creation and other _CURD_, just create a new method in the abstract factory class (implement the details in the subclass).
4. example usage: when designing an application on different platforms, methods themselves don't need to change the logic when running on different platform => create a factory class for initialize different object on different platform

```c
/*
 * C++ Design Patterns: Abstract Factory
 * Author: Jakub Vojvoda [github.com/JakubVojvoda]
 * 2016
 *
 * Source code is licensed under MIT License
 * (for more details see LICENSE)
 *
 */

#include <iostream>

/*
 * Product A
 * products implement the same interface so that the classes can refer
 * to the interface not the concrete product
 */
class ProductA
{
public:
  virtual ~ProductA() {}
  
  virtual const char* getName() = 0;
  // ...
};

/*
 * ConcreteProductAX and ConcreteProductAY
 * define objects to be created by concrete factory
 */
class ConcreteProductAX : public ProductA
{
public:
  ~ConcreteProductAX() {}
  
  const char* getName()
  {
    return "A-X";
  }
  // ...
};

class ConcreteProductAY : public ProductA
{
public:
  ~ConcreteProductAY() {}
  
  const char* getName()
  {
    return "A-Y";
  }
  // ...
};

/*
 * Product B
 * same as Product A, Product B declares interface for concrete products
 * where each can produce an entire set of products
 */
class ProductB
{
public:
  virtual ~ProductB() {}
  
  virtual const char* getName() = 0;
  // ...
};

/*
 * ConcreteProductBX and ConcreteProductBY
 * same as previous concrete product classes
 */
class ConcreteProductBX : public ProductB
{
public:
  ~ConcreteProductBX() {}
  
  const char* getName()
  {
    return "B-X";
  }
  // ...
};

class ConcreteProductBY : public ProductB
{
public:
  ~ConcreteProductBY() {}
  
  const char* getName()
  {
    return "B-Y";
  }
  // ...
};

/*
 * Abstract Factory
 * provides an abstract interface for creating a family of products
 */
class AbstractFactory
{
public:
  virtual ~AbstractFactory() {}
  
  virtual ProductA *createProductA() = 0;
  virtual ProductB *createProductB() = 0;
};

/*
 * Concrete Factory X and Y
 * each concrete factory create a family of products and client uses
 * one of these factories so it never has to instantiate a product object
 */
class ConcreteFactoryX : public AbstractFactory
{
public:
  ~ConcreteFactoryX() {}
  
  ProductA *createProductA()
  {
    return new ConcreteProductAX();
  }
  ProductB *createProductB()
  {
    return new ConcreteProductBX();
  }
  // ...
};

class ConcreteFactoryY : public AbstractFactory
{
public:
  ~ConcreteFactoryY() {}

  ProductA *createProductA()
  {
    return new ConcreteProductAY();
  }
  ProductB *createProductB()
  {
    return new ConcreteProductBY();
  }
  // ...
};


int main()
{
  ConcreteFactoryX *factoryX = new ConcreteFactoryX();
  ConcreteFactoryY *factoryY = new ConcreteFactoryY();

  ProductA *p1 = factoryX->createProductA();
  std::cout << "Product: " << p1->getName() << std::endl;
  
  ProductA *p2 = factoryY->createProductA();
  std::cout << "Product: " << p2->getName() << std::endl;
  
  delete p1;
  delete p2;
  
  delete factoryX;
  delete factoryY;
  
  return 0;
}
```

### Factory Method

When to use
* a class cant anticipate the class of objects it must create
* a class wants its subclasses to specify the objects it creates
* classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

```c
/*
 * C++ Design Patterns: Factory Method
 * Author: Jakub Vojvoda [github.com/JakubVojvoda]
 * 2016
 *
 * Source code is licensed under MIT License
 * (for more details see LICENSE)
 *
 */

#include <iostream>
#include <string>

/*
 * Product
 * products implement the same interface so that the classes can refer
 * to the interface not the concrete product
 */
class Product
{
public:
  virtual ~Product() {}
  
  virtual std::string getName() = 0;
  // ...
};

/*
 * Concrete Product
 * define product to be created
 */
class ConcreteProductA : public Product
{
public:
  ~ConcreteProductA() {}
  
  std::string getName()
  {
    return "type A";
  }
  // ...
};

/*
 * Concrete Product
 * define product to be created
 */
class ConcreteProductB : public Product
{
public:
  ~ConcreteProductB() {}
  
  std::string getName()
  {
    return "type B";
  }
  // ...
};

/*
 * Creator
 * contains the implementation for all of the methods
 * to manipulate products except for the factory method
 */
class Creator
{
public:
  virtual ~Creator() {}
  
  virtual Product* createProductA() = 0;
  virtual Product* createProductB() = 0;
  
  virtual void removeProduct( Product *product ) = 0;
  
  // ...
};

/*
 * Concrete Creator
 * implements factory method that is responsible for creating
 * one or more concrete products ie. it is class that has
 * the knowledge of how to create the products
 */
class ConcreteCreator : public Creator
{
public:
  ~ConcreteCreator() {}
  
  Product* createProductA()
  {
    return new ConcreteProductA();
  }
  
  Product* createProductB()
  {
    return new ConcreteProductB();
  }
  
  void removeProduct( Product *product )
  {
    delete product;
  }
  // ...
};


int main()
{
  Creator *creator = new ConcreteCreator();
  
  Product *p1 = creator->createProductA();
  std::cout << "Product: " << p1->getName() << std::endl;
  creator->removeProduct( p1 );
  
  Product *p2 = creator->createProductB();
  std::cout << "Product: " << p2->getName() << std::endl;
  creator->removeProduct( p2 );
  
  delete creator;
  return 0;
}
```

## Game Play Style OOD: BlackJack or 21 points

OOD: what is the process of playing the game?
What if System Design: how to make it be able to be played by multiple users?

### Data and Action

Based on data and action to design class. 

What is the **state** of the game: total points -> state machine <= action will determine what state it is currently on.

**Simulator Class** for controlling all the data flow

### Class

Card, Deck, Player/Hand, Dealer, Game (**has** Player[], Deck, Dealer)

start with Card, since it's the easiest class to be designed.

1. Card

- Assumption: standard 52-card set
- Card: 1) Value, 2) Suit (Club, Diamond, Heart, Spade)
- Deck: 1) List<Card>

```java
public enum Suit {
  Club, Diamond, Heart, Spade
}

public class Card {
    private int faceValue; // 1 for A, 11 for J, 12 for Q, 13 for K. Or we can use Enum here.
    private Suit suit;
    
    public Card(int c, Suit s) {
        faceValue = c;
        suit = s;
    }
    
    public int value() {
        return faceValue;
    }
    
    public Suit suit() {
        return suit;
    }
}

public class Deck {
    private static final Random random = new Random(); // action
    private final List<Card> cards = new ArrayList<>(); // or Card[]
    private int dealtIndex = 0;
    
    public Deck() {
        for (int i = 1; i <= 13; ++i) {
            for (Suit suit : Suit.values()) {
                cards.add(new Card(i, suit));
            }
        }
    }
    
    public void shuffle() {
        for (int i = 0; i < cards.size() - 1; ++i) {
            int j = random.nextInt(cards.size() - i) + i;
            Card card1 = cards.get(i);
            Card card2 = cards.get(j);
            cards.set(i, card2);
            cards.set(j, card1);
        }
    }
    
    private int remainingCards() {
        return cards.size() - dealtIndex;
    }
    
    public Card[] dealHand(int number) {
        if (remainingCards() < number) return null;
        Card[] cards = new Card[number];
        for (int i = 0; i < number; ++i) card[i] = dealCard();
        return cards;
    }
    
    public Card dealCard() {
        return remainingCards() == 0 ? null : cards.get(dealIndex++);
    }
}

public class Hand {
    protected final List<Card> cards = new ArrayList<>();
    
    public int score() { // or design as an abstract class => more extenable: can be used by other game
        int score = 0;
        for (Card card : cards) {
            score += card.value();
        }
        return score;
    }
    
    public void addCards(Card[] c) {
        Collections.addAll(cards, c);
    }
    
    public int size() {
        return cards.size();
    }
}
```

### Functionality

How to extend the Card design to support Black Jack?

Black Jack score rules:
- 2 ~ 10 scores its face value
- J, Q, and K score 10
- A score either 1 or 11 (store both, make decision later)

```java
public class BlackJackHand extends Hand {
    @Override
    public final int score() {
        List<Integer> scores = possibleScores();
        int maxUnder = Integer.MIN_VALUE; // max score <= 21
        int minUnder = Integer.MAX_VALUE; // max score <= 21
        for (int score : scores) {
            if (score > 21 && score < minOver) {
                minOver = score;
            } else if (score <= 21 && score > maxUnder) {
                maxUnder = score;
            }
        }
        return maxUnder == Integer.MIN_VALUE ? minOver : maxUnder;
    }
    
    private List<Integer> possibleScores() {
        List<Integer> scores = new ArrayList<>();
        for (Card card : cards) {
            updateScores(card, scores);
        }
        return scores;
    }
    
    private void udpateScores(Card card, List<Integer> scores) {
        final int[] toAdd = getScore(card);
        if (scores.isEmpty()) {
            for (int score : toAdd) {
                scores.add(score);
            }
        } else {
            final int length = scores.size();
            for (int i = 0; i < length; ++i) {
                int oldScore = scores.get(i);
                scores.set(i, oldScore + toAdd[0]);
                for (int j = 1; j < toAdd.length; ++j) {
                    scores.add(oldScore + to)
                }
            }
        }
    }
}
```



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

## Parking Lot

Steps:

- understand/analyze the functionality and its use case
  - use case -> functionality -> APIs
  - one level or multiple levels?
  - parking-spot / vehicle sizes?
  - track the location of each vehicle?

Drive in: input is a car, and output could be number of spot, boolean for if possible to be parked, ticket, etc. Why it has some many solutions? Because of use case.

Drive out: input is a ticket (money), car object, and output could be a boolean for if car actually exited, or a number for spots left

- APIs
  - input
  - output
  - specific / important components
- Design Classes
  - input / output
  - **DATA** -> physical entities
    - Parking Lot: CORE class -> store the main functionalities
    - Car: physical entity
    - Ticket: physical entity (depends on use case)
    - Parking Spot (optional): track different sized car, visited only, clean energy, etc.
    - level? no need, just a member field in parking lot; need, each level has many different attributes to be considered
  - Class relationships
    - association: a general binary relationship that describes an activity between **two classes**
      - vehicle -- parking spot: a vehicle can park at a specific parking spot
    - aggregation/composition: has-a
    - inheritance
      - vehicle -- car, truck

### Member fields and Methods of Class 

No need to have specific implementation **at first**

- Functionality
  - Basic Functionality: for a given vehicle, tell whether there is avaliable spot in the parking lot
  - possible extensions: provide avaliable spot locations, assign spot to the vehicle, ...
  - _assume there are multiple levels_
- ENUM
  - hard to be wrong used
  - e.g. : weekday using int -> 8? doesn't exist

```c
class ParkingLot {
    private:
        vector<Level> levels; // what if no level class? -> 2d array to represent the spot in different level
    public:
        bool hasSpot(Vehicle v) {
            // check each level, for each level, call Level#hasSpot(Vehicle)
        }
}

class Level {
    /*
    public:
        bool hasSpot(Vehicle v) {
            // check current level, if has spot
        }
    */
}

enum SIZE{suv, truck, eco}
class ParkingSpot {
    private:
        enum SIZE size;
    // bool fit(Vehice): check size and avaliability
}

class Vehicle {
    public:
        // data field
        virtual int getSize() = 0;
}
```

### Implementation

no need to complete the entire implementation during the interview, just finish the core functions

Exception Handler, Comparator (for enum?)

