[![AppID](../assets/Hello_GithubID.png)](../Hello_APP_Github_ID.py)

# Hello Graphics
Check samples with Hello_something.py for sample code on how to do stuff
* The code did a functional approach (no classes) ... dont add classes or I might refactor lmao

## ![API Documentation Generator](../Hello_Markdown_Doc.py)

## ![Public API](BitmapLib_Doc.md)

## ![Internal API](BitmapLibInternals_Doc.md)

# References

**The Basics:** https://github.com/TechnoTanuki/Python_BMP#readme

**Functional Progamming in Python:** https://machinelearningmastery.com/functional-programming-in-python/

**Details on the windows bitmap format:** https://docs.microsoft.com/en-us/windows/win32/gdi/bitmap-storage

**Ground up 2D graphics:**
* https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm 
* https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
* https://en.wikipedia.org/wiki/B-spline
* https://en.wikipedia.org/wiki/B%C3%A9zier_curve
* see: ![2D Graphics Primitives](../Python_BMP/primitives2D.py)
* ![BitFonts ground up](../Python_BMP/fonts.py)

**3D entities to onscreen 2D:** https://www.evl.uic.edu/luc/488/slides/class7.pdf
* ![predefined 3D entities](../Python_BMP/solids3D.py)

**Math in Computer Graphics:** https://faculty.cc.gatech.edu/~turk/math_gr.html 
* ![mini math lib](../Python_BMP/mathlib.py)
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

**Text and Fonts (images are links to sample code)**

[![Text Demo](../assets/fonts/8x14x3px1cs024bitplotstring2filebc0c13303664.bmp)](../Hello_Earth.py)

[![Reverse text](../assets/fonts/8x8x1px0cs024bitplotreversedstring2filebc0c65535.bmp)](../Hello_Earth_Reverse_text.py)

![Sideways text](../Hello_Earth_Sideways_text.py)

[![Upsidedown text](../assets/fonts/8x8x1px0cs024bitplotupsidedownstring2filebc0c65535.bmp)](../Hello_Earth_Upsidedown_text.py)

[![Vertical text](../assets/fonts/8x8x1px0cs024bitplotverticalstring2filebc0c16753920.bmp)](../Hello_Earth_Vertical_text.py)

[![Dot Font](../assets/fonts/8x14x4px1cs024bitplotstringasdots2filebc0c13303664.bmp)](../Hello_World_Dots.py)

[![Dot_Font Reversed](../assets/fonts/8x14x4px1cs024bitplotreversedstringasdots2filebc0c13303664.bmp)](../Hello_World_Dots_reversed.py)

[![Dot Font Vertical](../assets/fonts/8x14x4px1cs024bitplotverticalstringasdots2filebc0c16753920.bmp)](../Hello_World_Dots_vertical.py)

![Dot Fot Sideways](../Hello_World_Dots_sideway.py)


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

[![Rectangle](../assets/test_images/raccoon-rectangle.bmp)](../Hello_Rectangle.py)

[![Filled Rectangle](../assets/test_images/raccoon-filledrectangle.bmp)](../Hello_FilledRectangle.py)

![Filled Gradient Rectangle](../Hello_FilledGradRect.py)

**Regular Polygons**
![Regular Polygon](../Hello_Regular_Polygon.py)
![Thick Regular Polygon](../Hello_Thick_Regular_Polygon.py)
![Gradient Thick Regular Polygon](../Hello_Gradient_Thick_Regular_Polygon.py)

**Circle (images are links to sample code** 

[![Circle](../assets/text_images/raccoon-thinredcircle.bmp)](../Hello_Circles.py)

[![Filled Circle](../assets/test_images/raccoon-filledcircle.bmp)](../Hello_FilledCircle.py)

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

[![Sphere](../assets/test_images/raccoon-sphere.bmp)](../Hello_Sphere.py)

[![Icoahedron](../assets/HelloIcosahedron.jpg)](../Hello_Icosahedron.py)

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


**Downscale or Upscale Color Encoding in Bits**
* ![24 bits to 8 bits](../Hello_8bitBMP_Downscale.py)
* ![24 bits to 4 bits](../Hello_4bitBMP_Downscale.py)
* ![24 bits to 1 bit](../Hello_1bitBMP_Downscale.py)

**Resize**
* ![Resize Larger](../Hello_Resize_Larger_by_n.py)
* ![Resize Smaller](../Hello_Resize_Smaller_by_n.py)

**Image and Color Processing (the images are links to sample code)**

[![Invertbits](../assets/test_images/raccoon-invertbits.bmp)](../Hello_Invert_Colors.py)

[![Monofilter](../assets/test_images/raccoon-monochrome.bmp)](../Hello_Monochrome.py)

[![Colorfilter](../assets/test_images/raccoon-cyanfilter.bmp)](../Hello_Color_Filter.py)

[![BrightAdj](../assets/test_images/raccoon-adjustbrightness.bmp)](../Hello_BrightnessAdj.py)

[![GammaAdj](../assets/test_images/raccoon-gammaadj.bmp)](../Hello_GammaAdj.py)

[![Outline](../assets/test_images/raccoon-outline.bmp)](../Hello_Outline.py)

[![VerticalBrightnessGradient](../assets/test_images/raccoon-verticalbrightnessgrad.bmp)](../Hello_Vertical_Brightness_Gradient.py)

[![TVScanline](../assets/test_images/raccoon-eraseeverynthhoriline.bmp)](../Hello_TV_Scanlines.py)

[![RectMonoFilter](../assets/test_images/raccoon-monofilterinregion.bmp)](../Hello_Rectangular_Mono_Filter.py)

[![RectColorFilter](../assets/test_images/raccoon-cyanfilteregion.bmp)](../Hello_Rectangular_Color_Filter.py)

[![RectBrightnessAdj](../assets/test_images/raccoon-adjustbrightnessinregion.bmp)](../Hello_Rectangular_BrightnessAdj.py)

[![RectGammaAdj](../assets/test_images/raccoon-gammaadjtoregion.bmp)](../Hello_Rectangular_GammaAdj.py)

[![Pixel Blur](../assets/test_images/raccoon-pixelizenx.bmp)](../Hello_Pixellate_the_Earth.py)

[![Circular Color Filter](../assets/test_images/raccoon-yellowcircregion.bmp)](../Hello_Circular_Color_Filter.py)

[![Circular Mono Filter](../assets/test_images/raccoon-monochromecircregion.bmp)](../Hello_Circular_Mono_Filter.py)

[![Pixel Blur Circular Region](../assets/test_images/raccoon-pixelizenxncircregion.bmp)](../Hello_Circular_Pixellate.py)

[![Circular Region Brightness Adj](../assets/test_images/raccoon-brightnessadjcircregion.bmp)](../Hello_Circular_Region_BrightnessAdj.py)

[![Circular Region Gamma Adj](../assets/test_images/raccoon-gammacorrectcircregion.bmp)](../Hello_Circular_Region_GammaAdj.py)

[![Crop](../assets/test_images/raccoon-cropregion.bmp)](../Hello_Crop_Earth.py)

![Save Selection](../Hello_Save_Selection.py)

![Copy_Paste](../Hello_Copy_Paste_Earth.py)



**Flip/Rotate (the images are links to sample code)**

[![FlipVertical](../assets/test_images/raccoon-flipvertical.bmp)](../Hello_Flip_Vertical.py)

[![FlipHorizontal](../assets/test_images/raccoon-fliphorizontal.bmp)](../Hello_Flip_Horizontal.py)

[![FlipHorizontal](../assets/test_images/raccoon-flipXY.bmp)](../Hello_FlipXY.py)

**Mirror (the images are links to sample code)**

[![MirrorTop](../assets/test_images/raccoon-mirrortop.bmp)](../Hello_Mirror_Top.py)

[![MirrorTopLeft](../assets/test_images/raccoon-mirrortopleft.bmp)](../Hello_Mirror_TopLeft.py)

[![MirrorTopRight](../assets/test_images/raccoon-mirrortopright.bmp)](../Hello_Mirror_TopRight.py)

[![MirrorBottom](../assets/test_images/raccoon-mirrorbottom.bmp)](../Hello_Mirror_Bottom.py)

[![MirrorBottomLeft](../assets/test_images/raccoon-mirrorbottomleft.bmp)](../Hello_Mirror_BottomLeft.py)

[![MirrorBottomRight](../assets/test_images/raccoon-mirrorbottomright.bmp)](../Hello_Mirror_BottomRight.py)

**Fractals (the images are links to sample code)**

[![Mandelbrot](../assets/fractals/mandelbrot.bmp)](../Hello_Mandelbrot_Set.py)

[![Multibrot](../assets/fractals/multibrot.bmp)](../Hello_Multibrot_Set.py)

[![Julia](../assets/fractals/julia.bmp)](../Hello_Julia_Set.py)

[![Multijulia](../assets/fractals/multijulia.bmp)](../Hello_Multijulia_Set.py)

[![Tricorn](../assets/fractals/tricorn.bmp)](../Hello_Tricorn_Set.py)

[![Multicorn](../assets/fractals/multicorn.bmp)](../Hello_Multicorn_Set.py)

[![Newtons](../assets/fractals/newtons.bmp)](../Hello_Newtons_fractal.py)

[![Newtons4](../assets/fractals/newtons4.bmp)](../Hello_Newtons_fractal4.py)

[![Koch](../assets/fractals/koch3.bmp)](../Hello_KochSnowflake.py)

[![Hilbert6](../assets/fractals/hilbert6.bmp)](../Hello_HilbertCurve.py)

[![Hilbert4](../assets/fractals/hilbert4.bmp)](../Hello_ThickHilbertCurve.py)


* ![Newtons Fractal 4.1](../Hello_Newtons_fractal4_1.py)
* ![Newtons Fractal 5](../Hello_Newtons_fractal5.py)
* ![Newtons Fractal 5.3]( ../Hello_Newtons_fractal5_3.py)
* ![Newtons Fractal 6](../Hello_Newtons_fractal6.py)
* ![Newtons Fractal 6.3](../Hello_Newtons_fractal6_3.py)
* ![Fern](../Hello_Fern.py)
* ![Thick Gradient Hilbert Curve](../Hello_ThickGradHilbertCurve.py)
* [!Koch Curve](../Hello_KochCurve.py)
* [!Cat Paws](../Hello_CatPaws.py)

**Parametric Curve Equations**
* ![Cardioid](../Hello_Cardioid.py)
* ![Epicycloid](../Hello_Epicycloid.py)
* ![Flower](/Hello_Flower.py)
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
