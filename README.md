# Grid Mapper

A collection of Python scripts that make [maidenhead locator] maps with [GMT].
Normally I'd use `pygmt` but something is wrong with my installation, so
instead, to run this use the provided script `gridmap.sh`.

`gridmap.sh <locator>`

This can be used to make maps at multiple scalse 

`gridmap IO`

`gridmap IO91`

`gridmap IO91pm`

and

`gridmap IO91pm24`

yield 
![IO](https://github.com/philip-stuckey/gridmapper/assets/7987932/9aacfff6-4e16-4609-bbd0-765c9235a40d)
![IO91](https://github.com/philip-stuckey/gridmapper/assets/7987932/0dcdfc87-2282-4b27-9e5a-86cd6a7d2cd0)
![IO91pm](https://github.com/philip-stuckey/gridmapper/assets/7987932/82c2be61-1e03-4364-9533-54d56957475e)
![IO91pm24](https://github.com/philip-stuckey/gridmapper/assets/7987932/725d5083-aaee-4670-98e8-e719df6e8015)

respectively.

[maidenhead locator]:https://en.wikipedia.org/wiki/Maidenhead_Locator_System
[GMT]:https://www.generic-mapping-tools.org/
