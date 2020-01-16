## Design - Cohesion 

Design has the following components:
  * Architecture 
  * High Level
  * Models
  * Coupling
  * Cohesion: 
    * Cohesion is the other area to focus on when we are talking about modularity. 
    * Cohesion is the measurement of how focused our module is on a single task.
    * The more focused the module, the higher the cohesion.
  * Low Level
  * Modularity



**Cohesion overview:**
  * Basics:
    * With cohesion, higher is better. We want modules which only do one thing and one thing only. The reason for this is with maintainability. 
    * With low cohesion, we can't reuse the code anywhere. 
    * If we are smart and build a set of really cohesive modules, we can use those modules as building blocks for our next project.
    * The goal with modularity is to have a balance with both coupling and cohesion. We want to create loose coupling, and high cohesion.

**Cohesion Types:**
  * Weak Cohesion
    * ```Coincidental Cohesion``` - The tasks within the module are only linked because they are in the same module. This is the weakest form of cohesion. Here, the modules are completely random. There is nothing linking the tasks within a module, except the fact that they were simply put into the same file.
    * ```Temporal Cohesion``` - The tasks within the module are only linked because events happen around the same time. An example in the computer world would be "do shutdown activities". In this command we could be doing server calls, shutting off physical machines, sending emails, updating the front end, etc. The list could include really anything. For this reason, it is weakly cohesive.
    * ```Logical Cohesion``` - The tasks within the module are linked due to being in the same general category. With this level, we have begun to organize the modules a bit more. We have made general categories, and broken up the modules into these categories. If our module for example was "backup manager", then it still has a lot of wiggle room. In this controller we could be backing up user data, financial data, cache, cookies, and so on. Additionally we could be running commands that might have to do with backing up. Overall, this is still a weak form of cohesion.

  * Medium Cohesion
    * ```Procedural Cohesion``` - The order of execution passes from one command to the next. Here we have a relationship of time. This is different from temporal because the tasks are both linked, and essential for one another. There is an order by which these must be executed to work properly.
    * ```Communicational Cohesion``` - When all tasks support the same input and output data.
    * ```Sequential Cohesion``` - A combination of the previous two. When all tasks work in which the output data for one, is the input data for the next. With this, we have a procedure of tasks, and these tasks all share the same data. 

  * Strong Cohesion
    * Functional Cohesion - This is when all tasks within a module support activities needed for one, and only one problem-related task. In essence the module only does a single action. In these situations, the module is more like a large function. Just from looking at the name, you know exactly what the module is doing.
    * Object Cohesion - This can either be lumped in with functional cohesion, or by itself. Object cohesion is when all activities modify a single object.This only works in object-oriented languages.
