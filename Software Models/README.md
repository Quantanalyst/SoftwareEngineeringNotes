### Basic Definitions

**Technical debt**: A poor, hard to understand "hacky" implementation which will have to be repaid with interest later on. In other words, 1 hour saved now may cost 20+ hours later. 20% of projects fail. Many of these are due to poor development practices. 

**Software Development Life Cycle**:
  * Requirements: A process for finding out the goals of the system. A way of figuring out the exact specification of **what** the software should do. 
  * Design
  * Implementation: Code and documentation 
  * Verification (Test) : This stage is mostly determined by the requirements. So, the verification stage is a collection of unit and functional test designed to verify that the implemented code meet the requirements. 
  * Maintenance: create lifecyle plan( e.g. check the software every 6 months to see all technologies are up to date, etc) and fixing bugs 

**User Requirements vs. System Specification**: Requirement is a non-technical definition of something that is required from the system. Specification is a technical definition of what is required from the system. Specifications are in essence "technical requirements". They are used to define the problem in terms of the technical constraints.

**Non-Functional vs. Functional Requirements**: Functional requirements are requirements which pertain to the function of the system. Non-Functional requirements are requirements which cover areas that don't directly affect the function of the program.

Non-Functional requirements might have some subcategories:
  * Product requirements: Must haves of the product itself. Talk about behavior
  * Organizational requirements: Company policies, standards, rules, etc (e.g. Product data must be encrypted by AES 256, The project will be developed using the Scrum methodologies, ...) 
  * External requirements: External laws, regulations, trends, etc. 

## Software Models

Some well-known software models are as below:
  * WRSPM Model (World, Requirements, Specification, Program, Machine): 
    * World - Assumptions about what we are developing
    * Requirements - Defining our problem in generic easy to understand terms
    * Specifications - Defining the more technical details of the interface we are building
    * Program - The code, frameworks, development process, etc
    * Machine - The physical hardware we are running on

There are additional areas of classification we can use as well.
  * Eh - Environment hidden. These are pieces of data within the environment, which are just concepts or ideas. For example, the password you have memorized for an account. This piece of information exists only within your mind. Therefore it's a variable, but hidden.
  * Ev - Environment Visible. These are pieces of data within the environment which are now visible. Entering that password into a computer terminal manifests it. It is now represented in the physical world, and in a way which the system can now use.
  * Sv - System Visible. This is the part of the system which is visible to the user. This includes the program and the machine. So the keyboard, monitor, mouse etc. It also covers the screens and part of the program which you can interact with.
  * Sh - System Hidden. This is the part of the system which is hidden from the user. This includes the part of the software that the user doesn't touch, and the components within the machine itself. An example of this would be with a calculator. The user enters in the two numbers to be added. The hidden part is how the machine adds the numbers together before showing the result to the user.

<img src="https://github.com/Quantanalyst/SoftwareEngineeringNotes/blob/master/Software%20Models/wrspm.png"  width="360" height="360">






**waterfall vs. Agile** 
 




