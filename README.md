# Connect-4

Minimax function to play Connect-4.
Uses [Zobrist hashing](https://en.wikipedia.org/wiki/Zobrist_hashing) to prevent checking of identical game states.


Technically, this can solve Connect-4 if you have it set at maximum depth, but it's too slow right now.
I need to get multithreading to work.

Python was not the correct language to write this in. Likely going to redo this in ~~C++ or C#~~ [redoing it in rust to learn it](https://github.com/Aiqojo/rust4)
