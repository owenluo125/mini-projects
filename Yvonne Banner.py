# Arknights Endfield gacha simulator for Yvonne banner
# Simulates going to 60 pulls everytime for the dossier
# Assumes you already have the dossier from the previous banner
# Takes into account AIC quota + Bond quota
# Big assumption, assumes you already own every unit, including new 6-stars
# Only assumes you have 5-star and 4-star units at max dupes
# Big assumption, during soft pity 5-star and 4-star rates drop proportionally

""" Pulls every given every banner:
5 from weekly login
5 from AIC quota exchange
10 from previous dossier
10 from urgent headhunt (isn't affected by pity and doesn't affect it)
X from bond quota (at minimum with worst luck possible, about 3)
"""

""" How the gacha works
Base rates:
6-star: 0.8000%
5-star 8.0000%
4-star 91.2000%
When you reach 65 pulls without any 6-stars, the 66th pull and so on will get a flat +5.0000% increase in chance for 6-stars
If you reach 80 without any, the 80th pull guarantees it.
If you get a 6-star, you have a 50% chance of getting the banner up unit, there is no guarantee after losing.
The first time you reach 120 without getting the banner up unit, that pull will grant you it, and consumes your pity.
Each 4-star grants: 20x arsenal tickets, 5x AIC quota
Each 5-star grants: 200x arsenal tickets, 20x AIC quota, 10x bond quota
Each 6-star grants: 2000x arsenal tickets, 50x bond quota
The first 30 pulls you do on a banner gives you an urgent recruitment, this gives you a free 10 pull, however pity does not apply here and pity cannot be built
The first 60 pulls you do on a banner gives you a headhunting dossier, this gives you a free 10 pull next banner"""

import random

