Title: DLLs - The Hidden System Design Boundaries
Date: 2025-09-16
Category: System Design Principles
Tags: DLL, System Design, Software Architecture, Modular Monolith
Slug: dll-system-design
Author: Priyanshu Bishnoi
Summary: Exploring DLLs beyond dependencies — how they embody encapsulation, reusability, and modularity, making them the building blocks of maintainable monoliths.

## Understanding DLLs Beyond the File Extension

Most developers encounter **.dlls (Dynamic Link Libraries)** as “dependencies” — files that contain compiled code their applications need.

But from a **system design perspective**, a .dll is much more than just a technical necessity. It embodies key architectural principles that we also apply at higher levels, like in microservice design.

## 🧩 What is a DLL in Simple Terms?

A **.dll is a compiled, reusable module** that contains code and resources. Multiple applications can load and use it at runtime.

* In **.NET**, a .dll is an assembly with IL (Intermediate Language) + metadata.

* In **native systems**, it’s a binary library with exported functions.

## 🧩 Why DLLs Matter in System Design

### 🔹 Encapsulation & Abstraction

DLLs expose a public API while hiding their internal implementation. This enforces boundaries, similar to how 
microservices expose endpoints but hide their internals.

### 🔹 Reusability

A DLL can serve multiple applications, just like a shared service.
E.g., a `Payments.dll` can be reused by multiple internal tools instead of duplicating code.

### 🔹 Maintainability

DLLs can be **updated independently**, without rebuilding the entire system. This is parallel to independently deployable microservices.

### 🔹 Separation of Concerns

Different DLLs handle different , aligning with system design principles like **single responsibility and loose 
coupling**. Example: `Auth.dll`, `DataAccess.dll`, `Logging.dll`.

## 🧩 DLL vs Microservice (System Design Analogy)

| Aspect            | DLL (Inside Monolith)                | Microservice (Distributed System)        |
|-------------------|--------------------------------------|------------------------------------------|
| Boundary          | Assembly boundary                    | Service boundary                         |
| Interface         | Public classes/methods               | REST/gRPC APIs                           |
| Communication     | In-process (fast)                    | Network calls (slower)                   |
| Deployment        | Deployed with the application        | Independent deployment                   |
| Failure Scope     | App may crash if DLL fails           | Isolated failures                        |
| Update Model      | Versioning managed at build/deploy   | Independent CI/CD pipeline               |

## 🧩 The Big Picture

When you use DLLs, you’re not just organizing code — you’re **designing systems with modularity in mind**. DLLs are 
the **building blocks of maintainable monoliths**, the same way microservices are the building blocks of scalable distributed systems.

## ✅ Takeaway:
Next time you see a `.dll` in your project, don’t just think “dependency.”
Think: **“This is a design boundary — a self-contained service inside my system.”**
