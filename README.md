# qt-python-probability-space-visualisation

Exploration of graphical representations of static and dynamic probability spaces using Qt.

A number of versions will be developed:

## Version 1 - static visualization (heatmap)

    Representation of arbitrary percentages on a 2d heatmap using pre-defined colour maps.

##  Version 2 - dynamic visualization (heatmap) 

    A colour map linked to timed update, updating the visualization in near real time showing 
    shifting probabilities.
    
##  Version 3 - Numpy (Poisson) derived Probability space 

    Refactoring of Probability Space using Numpy / SciPy to 
    calculate probability distribution.
    
## Version 4 - Numpy (Poisson) with simulated probability movements

    As version 3 with basic simulation of probabilty movements
    to explore animation & GUI updates.
    
## Version 5 - message queue visualization

    A separate simulator is used to generate update messages
    at a given frequency and behaviour.  These are posted
    to a message queue then picked up by a separate subscriber.