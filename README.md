# Grid Mapper

A collection of Python scripts that make [maidenhead locator] maps with [GMT].
Normally I'd use `pygmt` but something is wrong with my installation, so
instead, to run this use the provided script `gridmap.sh`.

`gridmap.sh <locator>`

This can be used to make maps at multiple scalse 

`gridmap IO`

`gridmap IO91`

and 
`gridmap TO91pm`

yield 

![IO](examples/IO.pdf)
![IO91](examples/IO91pm.pdf)
![IO91pm](examples/IO91pm.pdf)

respectively.

[maidenhead locator]:https://en.wikipedia.org/wiki/Maidenhead_Locator_System
[GMT]:https://www.generic-mapping-tools.org/

