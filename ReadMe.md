# Coffee Shop Simulations
## Paul McDermott & Justin Standish-White

This project explores the coffeebar dataset and, using insights from analysing that dataset, develops a simulation programme in python. The end objective is to simulate 5 years of transactions for the coffee shop.


## Description

An in-depth paragraph about your project and overview of use.
This project is the key deliverable for a master's level introduction to programming in Python at the Toulouse School of Economics. Our work herein uses a vast array of skills picked up during the short course. These include working with pandas, class structures, project management and general data analysis. 

This project is divided into four parts. They are summarised below.

1. Exploring existing data. We explore the provided coffeebar data and answer several questions as requested. The key information here is to determine what food and drinks the store sells and the relative popularity of these items amongst customers. Our results show clear time patterns in purchases, with patterns being homogenous within 3 distinct time periods: a morning slot from 8-11am, a lunch time slot from 11-1pm and an afternoon slot from 1-6pm. We can take the probabilities of buying each item within these slots and use these in our subsequent simulations.

2. Setting up a class structure. We have four types of customers that may enter the store. Returning customers have two types: regulars and hipsters, who differ in their initial budgets. Then, walk-ins are split into normal walk-ins and trip advisor tourists, the latter of which may leave a tip after their purchase. 
In this stage of the project, we set up these classes as well as a store class, although we will only use one store. This allows us to build most of the functionality into the classes and keep information stored within objects.
For instance, we build several methods into the store class which determine whether customers enter in a given minute and then determines what type of customer. To support this, initialising a store requires a food and drink 'menu' which contains prices as well as the probabilities at different times, determined in Part 1.

3. With this structure, we now run simulations by using our minute_of_business function which simulates a possible transaction in a given minute. If a transaction occurs, this outputs the details of it and stores these in the store and the relevant customer. 
We can then analyse this information after simulating 5 years of activity with this minute-level function as the base. 

4. We explore some extension questions.

## Getting Started

### Dependencies

* This project was set up using Pycharm CE, with a Conda interpreter. We used M1 MacBooks. 


### Executing program

* The code should be straightforward to run. Here is an explainer for the files.

1. Exploratory. This covers Part 1 in its entirety.

2. Classes folder, this contains the set up for the Customer and Store Classes. This is Part 2 in its entirety. 

3. Functions, this sets up the functions for our simulations. This is part of Part 3.

4. Simulations. This runs the simulations (Part 3) and contains most of the extension analysis (Part 4).

5. Simulation Analysis. This analyses the simulated data to complete Part 3. 

6. Test. This was created to test a specific feature of our system. It has no directly relevant output for the project.

7. Old Code. This contains some code we didn't end up using but wanted to have for a reference. 

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names.

ex. Paul McDermott
ex. Justin Standish-White




## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)