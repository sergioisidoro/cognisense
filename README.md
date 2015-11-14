## CogniSense is a neuroscience platform

This is a project for the Junction hackathon 2015 (http://hackjunction.com/), built on a weekend - Micro MVP
It consists of a basic platform for inputing, saving, and running procesing/ML services on online biological data.

## How?

Flask + redis + mongodb + Pybrain + NVD3

```
Post --> Flask --> Redis pubsub ---------- Dendrite realtime data -------- live diagnostics
            \                   \ -------- Diagnostics (PyBrain)------------------ /
             \--- MongoDb                   
```

## Final result:

![alt tag](https://raw.github.com/sergioisidoro/cognisense/master/screens/screen1.png)


## Data sources:
We used Muse (http://www.choosemuse.com/) to aquire EEG data to an Android device, that relayed the info every second via POST to our server. 

## TO DO
A lot(!) of stuff.

This was a demo, so everything is using default localhost machine settings. 

See this more as a scaffold for a future project.

## Acknowledgements:
# The Awesome team of the Hackathon:
https://github.com/sergioisidoro (Backend) 

https://www.facebook.com/dalund (Android dev)

https://github.com/Staphylococcus (Identity, marketing, and design)


Some styles used from psdash (CC0 1.0 Universal) - https://github.com/Jahaja/psdash
Thanks man :)


