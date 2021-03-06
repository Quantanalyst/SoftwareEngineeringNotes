## Design - Coupling 

Design has the following components:
  * Architecture 
  * High Level
  * Models
  * Coupling:
    * Coupling is one of the major things to look at when designing the modularity of the system. It details how dependent each module is on every other module.
    * A set of modules with tight coupling is bad design. It creates hard to maintain code.
  * Cohesion
  * Low Level
  * Modularity



**Coupling overview:**
  * Basics:
    * Our enemy with all of this is dependence. We don't want our modules to be dependent on one another.
    * We want to be able to swap one module out with another, and only have to update code in the swapped module.
    * The more dependent our program is, the more and more modules we will have to rewrite for every change.
    * Measuring coupling as we design and develop is important.
    * Aim for loose coupling, *justify* in writing anything stronger.

**Coupling Types:**
  * Tight Coupling: This is the worst form of coupling. Tight coupling means there is a strong dependence between modules. Changes will be very hard to make and bugs will be difficult to track down.
    * ```Content Coupling``` - This details when one module modifies or relies on the inner workings of another module. If we have module A and module B, tight coupling would be A calling B.data. A in this situation is directly calling the data from B. This means if B were to change, be replaced, or even just be renamed, then A would fail. If a bunch of files all called the information directly from B, and B were renamed, there would be failures in each of these files.
    * ```Common Coupling``` - This is when a bunch of modules have access to *manipulate* the same global data. If 10 files directly read and write to this global data, we can quickly run into issues. Let's say one of the modules is built wrong. It pushes up an incorrect value to the global data. The other 9 files pull this data down, and instantly corrupt. We now have errors in 10 different places in our program. The only way to track an issue like this down, is to check all 10 files. It becomes a nightmare to debug.
    * ```External Coupling``` - This coupling is when several modules have direct access to the same external Input/Output. A common example of this is with an API. Let's say we have a program with 800 different files all making API calls to Google. The issue here is we don't have control over Google. They are free to change their API whenever they want. One day Google does just that. They decide to rename a call we use. We now have to update 800 different files to mitigate this change. More importantly, our active code will be errored out until we can make those changes. If we are running an online store, that can be a very large amount of money lost.

  * Medium Coupling: Here the coupling is getting better, but we still have room for improvement.
    * ```Control Coupling``` - This is when data is passed that influences the internal logic of another module. 
    * ```Data Structure Coupling``` - This is when multiple modules share the same data-structure. We are starting to get into the area where we might be able to justify this action. Here the major problem is if we switch out the data structure. If we have multiple modules updating the same Array, there will be a problem if we decide to change it to a linked-list. We will have to update every module. These modules all become dependent on the data-structure. If we find out a new data structure will improve our program, we will have to spend a lot of time in the change.

  * Loose Coupling: 
    * ```Data Coupling``` - This is when two modules share the same data. This is a good form of coupling. At the end of the day, our program's modules have to communicate with one another. With this form of coupling, the only thing we are passing back and forth is data. Our modules are processing the data, and making their decisions independently. Due to this, our dependency overall is extremely low. We have the ability to swap our modules easily, with little code that must be updated. Our program becomes more flexible, and easier to maintain.
    * ```Message Coupling``` - This coupling is when messages or commands are passed between modules. This is when we send a message to another module that tells it to start/stop, or run a function. We aren't controlling how these operations are being implemented. We are just giving the modules messages, which it then interprets and executes through it's own logic.
    * ```No Coupling``` - No communication between modules whatsoever. This is undesirables and unrealistic. Our modules need to communicate to have a purpose. No communication is purely a theory level. Our goal is to get as close to data and message coupling as possible.



