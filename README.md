<style>
    *{
        font-family:'Poppins', sans-serif;
        
    }
    P{
        font-size:12px;
    }
    UL{
        font-size:12px;
    }
    </style>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500&amp;display=swap" rel="stylesheet">
<b style="color:#5656f6;font-size:48px;margin:0px">SimuleX</b>
<hr style="-webkit-appearances:none;background:#5656f6;border:none;height:4px;border-radius:4px">
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

 
    ```python
    
    from projectileSim import projectile as pJ

    pJ.simulate(0, 1009, conv.getradians(45))

    ```

</li>
