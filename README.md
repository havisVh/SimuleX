# Simulex 

A comprehensive Simulation Suit for python.
<br>
<br>
<br>
<h2>Documentation</h2>
<hr>

files included in the repository:
<br>
<ul>
<li>main.py </li>
<li>packageManager.py</li>
<li>plotter.py</li>
<li>projectileSim.py</li>
</ul>
<br>
<hr>
<h2>How to&nbsp;?</h2>
<ul>
<li><h3>How to simulate a projectile?</h3>
You can easily simualte a projectile by using the <b>projectile </b> class from <b>projectileSim.py</b>
<br>
<br>
<h3>for example:<h3>
<br>
to simulate a projectile  of initial velocity 100 and angle of 45 degrees, use the following code:<br>

 

    
    from projectileSim import projectile as pJ
    from converter import converter as conv

    pJ.simulate(0, 100, conv.getradians(45))
    
>   here 0 is the initial x cordinate of the projectile and 100 is the initial velocity of the projectile. This will simulate the projectile and will print the trajectory of the projectile.

Also this will return a python object of the form

    {"type":dataType, "x": array of X coordinates, "y": array of Y coordinates, "maxH": max height of the projectile, "title": "Projectile Trajectory", "xlabel": "distance", "ylabel": "Height"}

   > where dataType is the type of data returned by the simulation and array of X coordinates and array of Y coordinates are the arrays of the X and Y coordinates of the trajectory of the projectile.

   to plot this You can use

    from plotter import *

    plot(data)

    # where data is the python object returned by the simulation.
>also note that it needs matplotlib to be installed.
you can install matplotlib by using the following command : <code>pip install matplotlib</code>

    # or alternatively
    from packageManager import packageManager as packMan
    packMan.install("matplotlib")

>above method is very useful if you want to send and test the simulation elsewhere.
</ul>

</li>
    
    
    # A combined example file
    ##############################################################################
    from projectileSim import projectile as pJ
    from converter import converter as conv
    from plotter import *

    plot(pJ.simulate(0, 100, conv.getradians(45)))
