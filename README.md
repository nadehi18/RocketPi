# RocketPi

RocketPi was a custom designed rocket with a payload of a Raspberry Pi Zero W.  The Zero W also had two different sensors connected: an altimeter and an accelerometer.  

## Rocket Design

The rocket was designed using OpenRocket.  The file is in the repository, and will give most of the specifications of the rocket. The rocket is able to use three different Estes Model Rocket Engines: C-11, D-12, and E-9.  During my flights, I used a D-12 and E-9. The results of these flights are in the repository as well.

## Module Design

The module was based around a Raspberry Pi Zero W.  The following items are included in the module:
* Raspberry Pi Zero W
* LSM303 Accelerometer
* MPL3115A Altimeter
* PowerBoost 500C
* 150mah 3.3V Lithium Polymer Battery
* Electrical Pushbutton
* 100K Ohm Resistor
* 10K Ohm Resistor

The module is setup so that pressing the pushbutton powers on the Raspberry Pi; then the Raspberry Pi has a low power script installed which will safely power off the module when the battery is depleted.  From some rudimentary tests, the battery would last nearly 30 minutes of use, which is more than enough for a launch.  The module cam be charged using a Micro USB cable; and the Raspberry Pi can be ran straight off of a power supply, bypassing the PowerBoost.  

Module Wiring Diagram:

![Wiring Diagram](https://github.com/nadehi18/RocketPi/blob/master/RocketPiWiringSchematic.png)

## Sensor Script

The sensor monitoring script was written in Python, and utilized some premade modules for each sensor.  The python script recorded the rocket's altitude, temperature, acceleration, position, and time.  The program placed all of this data in a .csv file which was imported into a Google Sheet and had a graph constructed of it.  

## Rocket Images

Simulated Image from OpenRocket:

![Simulated Rocket](https://github.com/nadehi18/RocketPi/blob/master/simulated-image.png)

Completed Rocket:

![Rocket](https://github.com/nadehi18/RocketPi/blob/master/rocket-whole.png)

Expanded Rocket:

![Expanded Rocket](https://github.com/nadehi18/RocketPi/blob/master/rocket-expanded.png)

## Raspberry Pi Module Images

Sensors:

![Sensors](https://github.com/nadehi18/RocketPi/blob/master/sensor-side.png)

Battery Circuit:

![Battery Circuit](https://github.com/nadehi18/RocketPi/blob/master/battery-circuit.png)

Side View:

![Module Side View](https://github.com/nadehi18/RocketPi/blob/master/side-view.png)
