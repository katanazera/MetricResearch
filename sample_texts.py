text_agent = '''
Building agents with LLM (large language model) as its core controller is a cool concept. 
Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. 
The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; 
it can be framed as a powerful general problem solver.

Agent System Overview
In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:

Planning
Subgoal and decomposition: The agent breaks down large tasks into smaller, manageable subgoals, 
enabling efficient handling of complex tasks.
Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, 
learn from mistakes and refine them for future steps, thereby improving the quality of final results.
Memory
Short-term memory: I would consider all the in-context learning (See Prompt Engineering) as 
utilizing short-term memory of the model to learn.
Long-term memory: This provides the agent with the capability to retain and recall (infinite) information over extended periods, 
often by leveraging an external vector store and fast retrieval.
Tool use
The agent learns to call external APIs for extra information that is missing from the 
model weights (often hard to change after pre-training), including current information, code execution capability, 
access to proprietary information sources and more.
'''

text_agent_planning = '''
Component One: Planning
A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.

Task Decomposition
Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. 
The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and 
simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an 
interpretation of the model’s thinking process.

Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. 
It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. 
The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier 
(via a prompt) or majority vote.

Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.",
 "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. 
 "Write a story outline." for writing a novel, or (3) with human inputs.
'''

text_skyline = '''
The Nissan Skyline GT-R R34 is an iconic sports car that has captured the hearts of automotive enthusiasts worldwide. 
Debuting in 1999, this fifth-generation GT-R took the automotive industry by storm with its breathtaking design and 
superior performance capabilities. 
Over the years, Nissan released several variations of the GT-R R34, 
each fine-tuned to cater to the distinct desires of speed aficionados. 
These limited production runs, often spanning just a few hundred units, 
have elevated the GTR R34’s status from an exceptional sports car to a cherished collector’s gem.

The base GT-R R34 set the foundation for what would become a celebrated lineage of sports cars. 
Powered by a 2.6-liter twin-turbocharged RB26DETT inline-six engine, it unleashed 276 horsepower to all four wheels through 
Nissan’s ATTESA E-TS (Advanced Total Traction Engineering System for All Electronic Torque Split) all-wheel-drive system. 
Its aerodynamic design and advanced suspension made it a formidable competitor on both the road and the track, 
instantly gaining a reputation for its handling prowess and agility. 
'''