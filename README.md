# Bifrost

:wave: Hello and welcome to **BiFrost** code repository. This is a short and simple Artificial Intelligence project. **BiFrost** helps to make your commute easier by showing you the shortest route to take from your start to your destination.

> [!IMPORTANT]
> I am planning to make updates to this project to add a feature regarding time. Basically, to add an option to either schedule your journey at a specific time or schedule an arrival to some place. For this I am planning to make a `.db`, maybe using sql or something, haven't decided. I'll make a **TODO** list. Interested developers please contact via mail or raise a ticket on the issues tab of the repo!

## Introduction

**Bifrost** is an AI application, which gives an optimal route between two places, based on the time taken for the journey. The algorithm for path optimization, is A-star search algorithm. The idea behind this project is to give the user better transportation options, when travelling using public transport. For example, if a person wants to go from Point A to Point B, you have multiple options. The algorithm then calculates a path considering the time taken for the journey to get the best path.
In the early development stages, we used Mumbai(Maharashtra, India) and Navi Mumbai(Maharashtra, India). We got this data using the famous mobile app **M-Indicator**. The app shows real time details about train timings, which we felt was the best way to retrieve the data.
This network of railway, is imitated as a **Graph** data structure. This made it easier to add the nodes (or stops/destinations). Further, if there is any development on creating better lines for transportation, adding to the network will be very easy.
We did this project as a part of our bachelor's degree for the Applied AI subject.

## Logs:

- Version 2: Add new metro lines 2A (Andheri West - Gundavali)
- Version 1: Add metro lines, central, harbour and western local lines. Add mono rails

## Contributions

This project has been commenced under the [MIT License](LICENSE). Thus, making it open source.
The project is still in its development phases and the developer(s) are always looking for improvements. If you want to contribute to this project in any sort of, please make a pull-request with the improved code and/or documentation.
If you are interested in seeing the project grow, please star the project, it will be really motivating for us!

### References:

- https://realpython.com/python-sqlite-sqlalchemy/
- https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
- https://www.metrotraintimings.in/Mumbai/ (to scrape data from)
