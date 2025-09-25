Title: Inheritance in Object-Oriented Programming  
Date: 2025-09-16  
Category: Object-Oriented Programming  
Tags: Inheritance, OOP, System Design, C#  
Slug: inheritance-oop  
Author: Priyanshu Bishnoi  
Summary: A deep dive into inheritance in object-oriented programming, explained with real-world analogies, C# examples, and architectural insights. 

## Understanding Inheritance in Object-Oriented Programming

We’ve all heard the word **inheritance** in daily life. For example, we inherit traits from our parents — eye color, height, or even habits. 

Similarly, in programming, inheritance allows a class (child/derived) to **inherit properties and behaviors** from another class (parent/base). These features may include methods, properties, and fields.

But what does that really mean at a deeper level? Let’s explore step by step.

## 🧩 1. What is Inheritance (Layman’s View)?

Inheritance simply means getting something from someone you’re related to.

In OOP: A class can “get” methods, properties, and fields from another class.

Example:

`Engineer` (base class, general)

`CivilEngineer`, `MechanicalEngineer`, `SoftwareEngineer` (derived classes, specialized)

Here, “Engineer” is the **general category**, and the specialized ones are inheritors.

👉 This is called the **generalization principle**:

* Base classes = generalized
* Derived classes = specialized

## 🧩 2. The “Is-A” Relationship

Inheritance is **valid** only when there is a **logical relationship**.

* ✅ “`Car` is a `Vehicle`” → makes sense → Car inherits Vehicle.
* ✅ “A `Dog` is an `Animal`”
* ❌ “`Car` is a `Driver`” → illogical → should not be inheritance.

This is why OOP stresses:

👉 Use inheritance only when **Derived class _is a type of_ Base class**.

## 🧩 3. One-to-Many Inheritance

In most mainstream languages (like C#, Java):

* One **base class** can have **multiple derived classes**.

* But one **derived class** can usually only inherit from **a single base class** 
* C# doesn’t support multiple inheritance of classes (only via interfaces).

Example:

```csharp 
class Vehicle { }
class Car : Vehicle { }  
class Bike : Vehicle { } 
```
Here, `Car` and `Bike` both inherit from `Vehicle`.

## 🧩 4. How Does It Work Internally?

Now, here’s the interesting part.
When you create an **object of the derived class**, two things happen internally:

* The **base class constructor** is called **first**.
* Then, the **derived class constructor** is executed.

So in memory, the object of the **derived class contains an implicit base part** inside it.

```csharp
class Base
{
    public Base() => Console.WriteLine("Base constructor");
    public void BaseMethod() => Console.WriteLine("Base method");
}

class Derived : Base
{
    public Derived() => Console.WriteLine("Derived constructor");
    public void DerivedMethod() => Console.WriteLine("Derived method");
}

class Program
{
    public static void Main()
    {
        Derived d = new Derived();
        d.BaseMethod();   // Works! Even though we never created a Base object
        d.DerivedMethod();
    }
}
```
**Output:**
```csharp
Base constructor
Derived constructor
Base method
Derived method
```
Here, even though we only created an object of **Derived**, the **Base constructor** ran first. That’s why we can call **BaseMethod()** from the derived object—it already has the base part inside it.

You don’t explicitly create a base object—C# handles it internally.

Covariance in inheritance: 

* C# also allows treating a more derived type as its base type.

Example:

```csharp
Base b = new Derived(); // Valid due to covariance
```
This shows that a derived object can always be referred to as its base type.

This is fundamental in polymorphism and is what allows derived classes to be passed where base classes are expected (e.g., in method parameters).

## 🧩 5. The Real Value of Inheritance

Yes, code can be reused without inheritance (through composition, libraries, or utility classes). Inheritance Offers deeper architectural benefits:

* **Abstraction** of common logic across related classes.

* **Polymorphism** that allows flexible, extensible design.

* **Hierarchical architecture**, where specialized entities extend generalized ones.

## ✅ 6. Final Takeaway

So, in essence:

* The **derived class encapsulates** the base class.

* The base part of the object is always created first even before the derived.

* Inheritance enables access to base methods, properties, and fields.

* With **covariance**, we can treat derived classes as base types, **unlocking polymorphism**.

Inheritance is not just about **sharing code** — it’s about building a **logical, extensible architecture.**