# UnderTheInfluence
A command-line application for raiding influence calculations in NationStates
##NOTICE: This project is current an early work in progress
Suggestions and contributions are appreciated at this time. While you are welcome to use the software in its current state as-is, it may not have the features you need or want yet.

Adding pilers in NationStates also increases the costs of passwords and transitions. However, this can be circumvented by removing your pilers right before doing the action in question, and then bringing them back. The program does the math assuming this is what you will do, as it is the most efficient option. I have plans to add other modes which will allow for the calculation of inefficient routes (keeping the pilers in), but the program cannot currently do this at this time.

The program currently assumes there is no floor for the cost of a transition. This may or may not be correct. I have yet to validate.

This project uses the pynationstates wrapper which must be installed beforehand (pip install nationstates). This application makes calls to the nationstates.net API. The username you provide will be given to the API as part of the UserAgent the program sends to identify itself to the API. This application uses pynationstates' built-in rate-limiter.
