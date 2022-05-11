# -----------------------------------
#| Copyright 2022 by Joel C. Alcarez |
#| [joelalcarez1975@gmail.com]       |
#|-----------------------------------|
#|    We make absolutely no warranty |
#| of any kind, expressed or implied |
#|-----------------------------------|
#|       The primary author and any  |
#| any subsequent code contributors  |
#| shall not be liable in any event  |
#| for  incidental or consequential  |
#| damages  in connection with,  or  |
#| arising out from the use of this  |
#| code in current form or with any  |
#| modifications.                    |
#|-----------------------------------|
#|   Contact primary author          |
#|   if you plan to use this         |
#|   in a commercial product at      |
#|   joelalcarez1975@gmail.com       |
#|-----------------------------------|
#|   Educational or hobby use is     |
#|   highly encouraged...            |
#|   have fun coding !               |
#|-----------------------------------|
#|   This graphics library outputs   |
#|   to a bitmap file.               |
# -----------------------------------


def getIFSparams() -> dict:
    return {'fern':(((0,0,0,.16,0,0),
                    (.2,-.26,.23,.22,0,1.6),
                    (-.15,.28,.26,.24,0,.44),
                    (.85,.04,-.04,.85,0,1.6)),
                    (.009,.073,.137,1)),
            'tree':(((0,.2,0,.5,0,0),
                     (.1,0,0,.1,0,.2),
                     (.42,-.42,.42,.42,0,.2),
                     (.42,.42,-.42,.42,0,.2)),
                     (.05,.2,.6,1)),
      'cantortree':(((1/3,0,0,1/3,0,0),
                     (1/3,0,0,1/3,1,0),
                     (2/3,0,0,2/3,0.5,0.5),
                     (0,0,0,0,0,0)),
                     (1/3,2/3,1,1)),
'sierpinskitriangle':(((.5,0,0,.5,0,0),
                       (.5,0,0,.5,1,0),
                       (.5,0,0,.5,.5,.5),
                       (0,0,0,0,0,0)),
                       (1/3,2/3,1,1))}


def mandelparamdict() -> dict:
    return {'maxdefault':(1.75,-1.75,1.5,-1.5),
              'maxeqdim':(1.75,-1.75,1.75,-1.75),
            'middefault':(.75,-1.25,1.25,-1.25),
            'mindefault':(.75,-.75,.5,-.5),
              'mineqdim':(.5,-.5,.5,-.5),
               'custom1':(-.5,-.7,-.5,-.7)}
