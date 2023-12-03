# PLOT GENERATOR

This project is a script to generate plots and stats of SUMO-CARLA co-simulation event

## Readme:

The plot-generator package is a tool for generating random plots for stories. It provides a variety of plot templates for ego and nearby vehicles

## Installation:

To install the plot-generator package, you can use pip:

```sh
$ pip install -r requirements.txt
```

## IMPORTANT:
It's important to add those two folders, otherwise the script could break

```sh
$ mkdir input && mkdir output
```

## Usage:

It needs two `.csv` files, to start, those should be placed in `{PROJECT_ROOT}/input`

- One of them is all events registered in the co-simulation, for instance: `testCarla2Sumo.csv`

| CarlaId | SumoId | Model                    | Role | Carla X              | Carla Y           | Carla Z | SUMO X             | SUMO Y             | SUMO Z | SUMO Vector X     | SUMO Vector Y     | SUMO Vector Z      | time               |
| ------- | ------ | ------------------------ | ---- | -------------------- | ----------------- | ------- | ------------------ | ------------------ | ------ | ----------------- | ----------------- | ------------------ | ------------------ |
| 270     | 0      | vehicle.chevrolet.impala | bot  | -0.30096709728240967 | 304.2039794921875 | 0.0     | 503.761474609375   | 122.02994537353516 | 0.0    | 2.684596538543701 | 1.026368260383606 | 0.7075497508049011 | 1700519357.715146  |
| 270     | 0      | vehicle.chevrolet.impala | bot  | -0.2984408438205719  | 304.197998046875  | 0.0     | 503.7639465332031  | 122.03594970703125 | 0.0    | 2.684596538543701 | 1.026368260383606 | 0.7075497508049011 | 1700519357.7636142 |
| 270     | 0      | vehicle.chevrolet.impala | bot  | -0.2934185266494751  | 304.18603515625   | 0.0     | 503.76885986328125 | 122.04798126220703 | 0.0    | 2.684596538543701 | 1.026368260383606 | 0.7075497508049011 | 1700519357.8264205 |

- The other one is nearby vehicles registered during the co-simulation, for instance: `nearbyVehicles.csv`

| CarlaId | Name       | Model      | Role   | Distance          | Carla X             | Carla Y           | Carla Z | time               |
| ------- | ---------- | ---------- | ------ | ----------------- | ------------------- | ----------------- | ------- | ------------------ |
| 323     | Citroen C3 | Citroen C3 | nearby | 19.52893261546941 | -15.420184135437012 | 131.9491424560547 | 0.0     | 1700519419.6671655 |
| 323     | Citroen C3 | Citroen C3 | nearby | 19.52893261546941 | -15.420184135437012 | 131.9491424560547 | 0.0     | 1700519419.685871  |
| 323     | Citroen C3 | Citroen C3 | nearby | 19.52893261546941 | -15.420184135437012 | 131.9491424560547 | 0.0     | 1700519419.699387  |

Ask for help:

```sh
$  python ./plot-generator.py --help
```

```sh
usage: plot-generator.py [-h] [--csv-file CSV_FILE] [--nearby-csv-file NEARBY_CSV_FILE] [--nearby-vehicles NEARBY_VEHICLES] [--ego-name EGO_NAME]
                         [--nearby-individual-plotting NEARBY_INDIVIDUAL_PLOTTING] [--nearby-ego-plotting NEARBY_EGO_PLOTTING] [--file-name FILE_NAME]

options:
  -h, --help            show this help message and exit
  --csv-file CSV_FILE   all events csv file
  --nearby-csv-file NEARBY_CSV_FILE
                        nearby csv file for all events
  --nearby-vehicles NEARBY_VEHICLES
                        number of vehicles nearby to plot
  --ego-name EGO_NAME   name of the ego vehicle, g.e. hero
  --nearby-individual-plotting NEARBY_INDIVIDUAL_PLOTTING
                        Need to see the individual plotting for nearby vehicles?
  --nearby-ego-plotting NEARBY_EGO_PLOTTING
                        Need to see the individual plotting for nearby vehicles with ego?
  --file-name FILE_NAME
                        Output file name
```

Run the script:

```sh
$  python ./plot-generator.py --csv-file testCarla2Sumo.csv --nearby-csv-file nearbyVehicles.csv --nearby-vehicles 3 --ego-name hero
```

Finally, you should have some plots like these ones:


![HERO](https://github.com/scrodrig/carla-sumo-script/assets/5466692/9815ee58-d9d5-4ad5-9db7-d55b486622ac)


![hero-carla_ids](https://github.com/scrodrig/carla-sumo-script/assets/5466692/8e5f2f41-5584-4e08-bae2-3dd7051601dd)



