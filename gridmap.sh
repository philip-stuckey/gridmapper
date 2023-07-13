#!/usr/bin/bash

region=$(python src/maiden_region.py $1)
width=$(python src/subsquare_dim.py $1 0)
height=$(python src/subsquare_dim.py $1 1)
scale=$(python src/squarescale.py $1)
font=6,,grey=faint
gmt begin "$1"
gmt coast -R$region -Ggrey -N2 -Ia 
gmt text <(python src/subsquares.py $1) -F+f$font
gmt basemap -Bxafg$width -Byafg$height
gmt basemap -TdjLB+f -LjBR+w$scale+o0.5c/0.5c+u+f -Fl+gwhite

gmt end show

