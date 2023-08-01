[![AppID](../assets/Hello_GithubID.png)](../Hello_APP_Github_ID.py)

# Hello Graphics
Check samples with Hello_something.py for sample code on how to do stuff
* The code did a functional approach (no classes) ... dont add classes or I might refactor lmao

## ![API Documentation Generator](../Hello_Markdown_Doc.py)

## ![Public API](BitmapLib_Doc.md)

## ![Internal API](BitmapLibInternals_Doc.md)

# References

**Functional Progamming in Python:** https://machinelearningmastery.com/functional-programming-in-python/

**Details on the windows bitmap format:** https://docs.microsoft.com/en-us/windows/win32/gdi/bitmap-storage

**Ground up 2D graphics:**
* https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
* https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
* https://en.wikipedia.org/wiki/B-spline
* https://en.wikipedia.org/wiki/B%C3%A9zier_curve
* see: ![2D Graphics Primitives](../pythonbmp/primitives2D.py)
* ![BitFonts ground up](../pythonbmp/fonts.py)

**3D entities to onscreen 2D:** https://www.evl.uic.edu/luc/488/slides/class7.pdf
* ![predefined 3D entities](../pythonbmp/solids3D.py)

**Math in Computer Graphics:** https://faculty.cc.gatech.edu/~turk/math_gr.html
* ![mini math lib](../pythonbmp/mathlib.py)
* fractals http://paulbourke.net/fractals/
* 2D Strange attractors https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/
* parametric curves https://mathworld.wolfram.com/topics/Curves.html
* moar curves https://mathcurve.com

**Colors**
* X11 color source: https://cgit.freedesktop.org/xorg/xserver/tree/os/oscolor.c
* XKCD color source:  https://xkcd.com/color/rgb/

If there is demand for it I could in theory write a book based on this project lmao.

**Books:**
* Roger T. Stevens. Graphics Programming in C (1993). 1st Indian Edition, M & T Publishing Inc
* Bernard Kolman. Elementary Linear Algebra (1991). 5th Edition, Macmillan Publishing Company
* Gerald L. Bradley, Karl J. Smith. Multivariable Calculus (1999). 2nd Edition, Prentice Hall

# Fully commented sample code list below


**Named colors**
* ![Named Colors](../Hello_ColorNames.py)
* ![X11 Colors](../Hello_X11ColorNames.py)
* ![XKCD Colors](../Hello_XKCDColorNames.py)

**Full Gradient Background**
* ![Linear Gradient](../Hello_Linear_Gradient.py)
* ![Circular Gradient](../Hello_Circular_Gradient.py)
* ![Radial Gradient](../Hello_Radial_Gradients.py)
* ![Non Linear Radial Gradient](../Hello_NonLinearRadial_Gradients.py)
* ![Radial Multichannel Gradient](../Hello_RadialMultichannel_Gradients.py)
* ![Non Linear Radial Multichannel Gradient](../Hello_NonLinearRadialMultichannel_Gradients.py)

**Line**
* ![Line](../Hello_Lines.py)
* ![Vector](../Hello_Vector.py)
* ![Thick Rounded Line](../Hello_Thick_Round_Line.py)
* ![Thick Rounded Gradient Line](../Hello_Thick_Round_Gradient_Line.py)

**Rectangle (images are links to sample code)**

[![Rectangle](../tests/assets/test_images/raccoon-rectangle.bmp)](../samples/primitives2d/Hello_Rectangle.py)

[![Filled Rectangle](../tests/assets/test_images/raccoon-filledrectangle.bmp)](../samples/primitives2d/Hello_FilledRectangle.py)

[![Filled Vertical Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle0.bmp)](../Hello_FilledvertGradRect.py)

[![Filled Smoothstep Vertical Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle0smoothstep.bmp)](../Hello_FilledvertGradRectsmoothstep.py)

[![Filled Smootherstep Vertical Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle0smootherstep.bmp)](../Hello_FilledvertGradRectsmootherstep.py)

[![Filled Smootheststep Vertical Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle0smootheststep.bmp)](../Hello_FilledvertGradRectsmootheststep.py)

[![Filled Horizontal Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle1.bmp)](../Hello_FilledhoriGradRect.py)

[![Filled Smoothstep Horizontal Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle1smoothstep.bmp)](../Hello_FilledhoriGradRectsmoothstep.py)

[![Filled Smootherstep Horizontal Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle1smootherstep.bmp)](../Hello_FilledhoriGradRectsmootherstep.py)

[![Filled Smootheststep Horizontal Gradient Rectangle](../tests/assets/test_images/raccoon-filledgradrectangle1smootheststep.bmp)](../Hello_FilledhoriGradRectsmootheststep.py)

[![Filled Vertical Dichromatic Gradient Rectangle](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle0.bmp)](../Hello_FilleddichromaticvertGradRect.py)

[![Filled Vertical Dichromatic Smoothstep Gradient Rectangle ](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle0smoothstep.bmp)](../Hello_FilleddichromaticvertGradRectsmoothstep.py)

[![Filled Vertical Dichromatic Smootherstep Gradient Rectangle ](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle0smootherstep.bmp)](../Hello_FilleddichromaticvertGradRectsmootherstep.py)

[![Filled Vertical Dichromatic Smootheststep Gradient Rectangle ](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle0smootheststep.bmp)](../Hello_FilleddichromaticvertGradRectsmootheststep.py)

[![Filled Horizontal Dichromatic Gradient Rectangle](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle1.bmp)](../Hello_FilleddichromatichoriGradRect.py)

[![Filled Horizontal Dichromatic Smoothstep Gradient Rectangle](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle1smoothstep.bmp)](../Hello_FilleddichromatichoriGradRectsmoothstep.py)

[![Filled Horizontal Dichromatic Smootherstep Gradient Rectangle](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle1smootherstep.bmp)](../Hello_FilleddichromatichoriGradRectsmootherstep.py)

[![Filled Horizontal Dichromatic Smootheststep Gradient Rectangle](../tests/assets/test_images/raccoon-filleddichromaticgradrectangle1smootheststep.bmp)](../Hello_FilleddichromatichoriGradRectsmootheststep.py)

**Regular Polygons**
![Regular Polygon](../Hello_Regular_Polygon.py)
![Thick Regular Polygon](../Hello_Thick_Regular_Polygon.py)
![Gradient Thick Regular Polygon](../Hello_Gradient_Thick_Regular_Polygon.py)

**Circle (images are links to sample code)**

[![Circle](../tests/assets/test_images/raccoon-thinredcircle.bmp)](../Hello_Circles.py)

[![Filled Circle](../tests/assets/test_images/raccoon-filledcircle.bmp)](../Hello_FilledCircle.py)

![Thick Circle](../Hello_Thick_Circle.py)

![Thick Gradient Circle](../Hello_Thick_Gradient_Circle.py)

**Ellipse**
* ![Ellipse](../Hello_Ellipse.py)
* ![Filled Ellipse](../Hello_FilledEllipse.py)
* ![Ellipical Gardient](../Hello_Elliptical_Gradient.py)
* ![Thick Rotated Gradient Ellipse](../Hello_Thick_Gradient_Ellipse_Rotated.py)

**Curves and Spirals**
* ![Bezier Curve](../Hello_BezierCurve.py)
* ![Bspline](../Hello_Bspline.py)
* ![Involute of a Circle](../Hello_InvoluteofaCircle.py)
* ![Cornu Spiral](../Hello_CornuSpiral.py)
* ![Square Spiral](../Hello_SquareSpiral.py)
* ![Thick Expponential Gradient Spiral](../Hello_Thick_Exponential_Spiral_Gradient.py)

**3D and 3D shading effects (Images are links to sample code)**

[![Sphere](../tests/assets/test_images/raccoon-sphere.bmp)](../Hello_Sphere.py)

[![Sphere smoothstep](../tests/assets/test_images/raccoon-spheresmoothstep.bmp)](../Hello_Sphere_smoothstep.py)

[![Sphere smootherstep](../tests/assets/test_images/raccoon-spheresmootherstep.bmp)](../Hello_Sphere_smootherstep.py)

[![Sphere smootheststep](../tests/assets/test_images/raccoon-spheresmootheststep.bmp)](../Hello_Sphere_smootheststep.py)

[![Sphere-dichroma](../tests/assets/test_images/raccoon-spheredichromic.bmp)](../Hello_Sphere_dichromic.py)

[![Sphere-dichroma smoothstep](../tests/assets/test_images/raccoon-spheredichromicsmoothstep.bmp)](../Hello_Sphere_dichromic_smoothstep.py)

[![Sphere-dichroma smootherstep](../tests/assets/test_images/raccoon-spheredichromicsmootherstep.bmp)](../Hello_Sphere_dichromic_smootherstep.py)

[![Sphere-dichroma smootheststep](../tests/assets/test_images/raccoon-spheredichromicsmootheststep.bmp)](../Hello_Sphere_dichromic_smootheststep.py)

[![Icosahedron](../tests/assets/HelloIcosahedron.jpg)](../Hello_Icosahedron.py)

* ![3D](../Hello_3D.py)
* ![Surface Plot](../Hello_3D_surfaceplot.py)
* ![Orb](../Hello_Orb.py)
* ![Benzene](../Hello_Benzene.py)
* ![Globe](../Hello_Globe.py)
* ![Discoball](../Hello_DiscoBall.py)
* ![Coin](../Hello_Coin.py)
* ![Cone](../Hello_Cone.py)
* ![Tetrahedron](../Hello_Tetrahedron.py)
* ![Cube](../Hello_Cube.py)
* ![Octahedron](../Hello_Octahedron.py)
* ![Decahedron](../Hello_Decahedron.py)
* ![Icosahedron Outline](../Hello_Icosahedron_Outline.py)


**Parametric Curve Equations (images are links to sample code)**

[![Flower](../assets/flower.bmp)](/Hello_Flower.py)

* ![Cardioid](../Hello_Cardioid.py)
* ![Epicycloid](../Hello_Epicycloid.py)
* ![Octopetala](../Hello_Octopetala.py)
* ![Gear Curve](../Hello_GearCurve.py)
* ![Heart Curve](../Hello_HeartCurve.py)
* ![Egg Curve](../main/Hello_EggCurve.py)
* ![Lissajous Curve](../Hello_LissajousCurve.py)
* ![Hypotrochoid](../Hello_Hypotrochoid.py)
* ![Superellipse](../Hello_Superellipse.py)
* ![Squircles](../Hello_Squircles.py)

**Spirographs**
* ![Hello_Spirograph.py](../Hello_Spirograph.py)
* ![Hello_Spirograph_1.py](../Hello_Spirograph_1.py)
* ![Hello_Spirograph_2.py](../Hello_Spirograph_2.py)
* ![Hello_Spirograph_Record.py](../Hello_Spirograph_Record.py)

**Graphs**
* ![XY Scatterplot](../Hello_XYScatterplot.py)
