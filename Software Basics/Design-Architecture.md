## Design - Architecture

Design has the following components:
  * Architecture
    * Architecture is the very top level of design
    * Architects are the link between idea and reality
    * Architecture is something that cannot be fixed once implemented
    * (very important) in software, bad architecture is something that can't be fixed with good programming. 
  * High Level
  * Models
  * Coupling
  * Cohesion
  * Low Level
  * Modularity

**Architecture** overview:
  * Software architecture is all about breaking up larger system into smaller focused systems
    * Our first step is to take the requirements, and build an initial architecture. We take this broad set of ideas and guidelines, and have to organize it into functioning areas.
    * Good Architure is hard. It takes a lot of resources to develop correctly. However, this upfront cost is almost always recovered from how maintainable the software is. This will reduce the amount of bugs, and the time to fix those bugs.
    * Maintainable software has good architecture
    * Architecture mistakes are **almost impossible to fix** once coding has begun
  * Good architecture allows for faster development, and smarter task allocation
    * Good architecture also allows the company to decide where to by and where to build
    * Reduces overall idle time 

Another benefit of breaking the project up is the idea of **buy vs build**. If we have for example 4 development teams. Through architecture design we have broke the project up into 5 different large projects. We go through each of these projects and learn that 1 of them has already been solved before and is for sale on the market. We can then allocate the 4 teams to the other ones, and just purchase the already created software, saving us time and money.

**Architecture Patterns** overview:
  * Pipe and Filter pattern
    * Process data through multiple different layers. The key to this pattern is the ability of each step to input, and output the **same type of data**. So if you send a set of numbers in one side, you will get a set of numbers out the other side.
    * There is definitely an added complexity with this pattern. Setting it up can be tricky to get correct. Also, if the data is lost at any step, the entire process is broken.
  * Client-Server pattern
    * The client-server pattern is one that is quite common today. Every single website and most phone apps use this architecture. With this pattern there are two parts to the software, the client, and the server.
  * Master-Slave pattern
    * The master is in full control of all slaves associated with it. This is good for a multitude of different applications, e.g. duplicate backup servers
    * This pattern is also used with "multi-threading". Here we break up an operation into a bunch of small parts. Each of those parts are given a thread and fed through the CPU. If a CPU has multiple cores, it can process multiple threads at the same time.
  * Layered pattern
    * The layered pattern consists of divvying up program into layers of technology. These layers only communicate with adjacent layers. 
    * This pattern simplifies the communication channels, and helps to better distinguish the areas of the program. Overall, this helps to make the program more maintainable. The downside to this, is that there can be of added complexity in some areas. For example, if you need to send a message from layer 1 to layer 9. There will have to be a function in each layer to pass that message along.

One of the best practices in the software architecture design in to break projects into **subsystems** and **modules**.
  * subsystem - independent system which holds independent value
  * module - component of a subsystem which can not function as a standalone. 

 **Examples**

client-server example:\
Let's take an iPhone app for example. What you download in the app store is what is known as the "client software". This is the version of the app built to talk to the server. It doesn't store any of the server's data locally. It is just setup to make the appropriate server calls when necessary.

The other part of this is of course the "server software". This is the software that is installed onto a server to receive the requests from the client. The server holds and updates the data. It also processes requests, and sends the data to the clients. Servers have to be tuned correctly, as there can be a near unlimited number of clients requesting information.



