## Blockchain theory

### understanding proof of Work

A proof of Work algorithm (POW) is how new Blocks are created or _mined_ on the blockchain. 
The goal of PoW is to discover a number which solves a problem.
The number must be difficult to find but easy to verify - computationally speaking - by anyone on the network.
This is the core idea behind Proof of Work.

In Bitcoin, the Proof of Work algorithm is called [Hashcash](https://en.wikipedia.org/wiki/Hashcash). 
It's the algorithm that miners race to solve in order to create a new block.
In general, the difficulty is determined by the number of characters searched for in a string.
The miners are then rewarded for their solution by receiving a coin - in a transaction.

The network is able to easily verify their solution.