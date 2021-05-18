# LavaBowsPaper

Update 5/18
The odl data is in /Data_Old/, while the 0.5um data is now in /Data/. I've run the original mie code and the miex/dapx/pixx code on this 0.5um data, and the resulting figures have been added to /Figures/.

Update 2/18
I copied over the MIECODE results into /Data/ into their own directory, then separated by compound. FluxDoP.py and variations reference these files to create flux and degree of polarization (DoP) plots. These plots are in their own directory in /Figures/ and are named with the compound, droplet size in um, and wavelength in nm.

Update 2/2  
Master.ipynb is copied from the original repo and updated to enter all information in the first cell, then run all cells to create all figures.

Scripts to create the plots are in the Scripts directory. The plots are in the Figures directory. Data files are in the Data directory when it is impractical to have the data in the python script. Here is a list of the scripts and their corresponding data files and figures:

* LiquidCompounds.py creates TempofPlanetsandComp.png
* SimpleIllumination.py creates SimpleLightcurve1.png and SimpleLightcurve2.png
* PeaksInOrbit.py uses PeaksInOrbit.dat and creates PeaksInOrbit.png
  * Problem with this: .csv file is acting weird -- work on this later...
  * Look into LavaBows/Old/Lightcurve.py
* planets_Mva.py uses planets_Mva.csv to create planets_Mva.png

Go through more of Master.ipynb - there are some important plots towards the end, but rely on dataframes (which are difficult to import correctly, the problem I had with the PeaksInOrbit.py script).

In LavaBows/MIECODE there are "PROGRAM" directories for each of the tested compounds. Master.ipynb reads in the data from these directories and creates the flux and DoP plots. It's pretty elegant actually. I bet if I just copy over the out files from these runs I can copy-paste these cells of Master.ipynb directly... another time...

There's a whole set of python scripts in LavaBows/Old which rely on importing each other (e.g. Orbit.py imports information/functions from Lightcurve.py).

In LavaBows/MIECODE/Old there are plotting scripts (plot.py) in /PROGRAM_10um/Results and /PROGRAM_50um/Results, as well as waterdrop_plot.py. These create flux and DoP plots for the given Mie run.

In LavaBows/PIXELS I create the pixelated face of the planet colored by flux. This is done with quick_plot_pixels.py which reads in the pixel out files.
