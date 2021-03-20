# First attempt at bigger picture

## Content and themes:
There will be two files, server and client. Client will function as the control
ler. Server will be run from the interface device. Server will have several pro
cesses. As of now, the plan is to run one process for enqueueing commands. Each
 8bit bus will have its own process and will be pulling from the queue. If it i
s not relevant, it will put it back? idk still working that one out.

Client will consist of event-based key code and client-side socket code. It wil
l run one process. Server will consist of code as above detailed.

Initial testing will be run on only one pi will still using networking code. On
ce another micro-sd card avails itself, we will run client from one pi and serv
er on the other pi.

