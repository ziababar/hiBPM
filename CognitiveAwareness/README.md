The structure of the project is as follows.

##Actors##
There are a number of actors in hiBPM. These can be individuals, departments, enterprises, or even technological systems. Each actor has certain objectives and motives.

##Processes##
hiBPM process structures are shown as workflows that actors execute.

##Plans##
In this project, we have the following plans

1. Plans that result in a change in execution behavior of workflows
    - there has to be a plan that "instructs" a process stage on how to construct the context sensing process stage
       PS 1: develop plan for context sensing
       PS 2: execute plan to create process configuration for context sensing
       PS 3: analyze context

2. Plans that result in a change in execution behavior of entities
    - there has to be a plan that "instructs" how to reconfigure the entities to handle a new context
       PS 1: develop plan for reconfig software system
       PS 2: execute the plan and create new reconfiguration
       PS 3: this new software system is then used in the process

##Designs##
In this project, we have the following designs

1. Show how entities can be setup
2. Have substitutable components

##Catalogues##
 - catalogues are not "used" repeatedly
 - catalogues do not provide execution instructions
 - so they are information flow


##prototype architecture##
 - Pattern Repository
 - Data Extractor

 - Context Analyzer
   - User Context Monitor
   - Model Context Monitor
   - Data Context Monitor

 - Quality Evaluator
 - Workflow Planner
 - Data Preparator

 - Data Miner 