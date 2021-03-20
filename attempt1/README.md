# First attempt at bigger picture

## Content and themes:
There will be two files, server and client. Client will function as the 
controller. Server will be run from the interface device. Server will have 
several processes. As of now, the plan is to run one process for enqueueing 
commands. Each 8bit bus will have its own process and will be pulling from the
queue. If it is not relevant, it will put it back? idk still working that one
out.

Client will consist of event-based key code and client-side socket code. It 
will run one process. Server will consist of code as above detailed.

Initial testing will be run on only one pi will still using networking code.
Once another micro-sd card avails itself, we will run client from one pi and 
server on the other pi.

