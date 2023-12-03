from loguru import logger
from pathlib import Path
from util.converters import convert_seconds

from util.filter import filter_by_column, __get_nearby_carla_ids
from util.physics import calculate_total_distance
from util.stats import average_velocity, closest_point, number_of_records, seconds_difference, seconds_difference_delay


def write_to_txt(
    file_name,
    all_dataframe,
    nearby_vehicles_dataframe,
    ego_name="ego",
    nearby_vehicles=3,
):
    HERE = Path(__file__).parent.parent
    OUTPUT_FOLDER = HERE / "output"
    file_path = OUTPUT_FOLDER / file_name

    logger.info("{}: {}".format("PATH TO FILE", file_path))

    with open(file_path, "w") as file:
        file.write(f"*********************************************************\n")
        file.write(f"********************File name: {file_name}****************\n")
        file.write(f"**********************************************************\n")
        file.write(f"Report \n")

        file.write(f"--------------------------------------------------------\n")

        number_rows = number_of_records(all_dataframe)
        file.write(f"Number of records all: {number_rows}\n")

        carla_ego_dataframe = filter_by_column(all_dataframe, "Role", ego_name)
        file.write(
            f"Number of records of {ego_name}: {number_of_records(carla_ego_dataframe)}\n"
        )

        file.write(f"--------------------------------------------------------\n")
        minutes, seconds = convert_seconds(seconds_difference(all_dataframe))
        file.write(
            "Total Test time elapsed: {:.0f}:{:.2f} min \n".format(minutes, seconds)
        )
        minutes, seconds = convert_seconds(seconds_difference(carla_ego_dataframe))
        file.write(
            "Test for {} time elapsed: {:.0f}:{:.2f} min \n".format(
                ego_name, minutes, seconds
            )
        )
        file.write(f"--------------------------------------------------------\n")
        nearby_vehicles_ids = __get_nearby_carla_ids(
            nearby_vehicles_dataframe, nearby_vehicles
        )
        file.write(
            "Nearby vehicles to {}, are {} \n".format(
                ego_name.capitalize(), nearby_vehicles_ids
            )
        )
        file.write(f"****************************LATEX*************************\n\n")

        file.write(
            "{}\n".format(
                nearby_vehicles_dataframe[
                    ["CarlaId", "Name", "Role", "Distance", "time"]
                ].to_latex()
            )
        )

        file.write(f"------------------------------------------------------------\n")
        ego_distance = calculate_total_distance(carla_ego_dataframe)
        file.write(
            "Total distance traveled by {}: {:.2f} meters \n".format(
                ego_name, ego_distance
            )
        )

        ego_velocity = average_velocity(carla_ego_dataframe)

        file.write(
            "Average velocity {}: {:.2f} m/s \n".format(
                ego_name, ego_velocity
            )
        )

        file.write(f"------------------------------------------------------------\n")


        for carla_id in nearby_vehicles_ids:

            nearby_vehicle_dataframe = filter_by_column(all_dataframe, "CarlaId", carla_id)

            nearby_distance = calculate_total_distance(nearby_vehicle_dataframe)
            file.write(
                "Total distance traveled by {}: {:.2f} meters \n".format(
                    carla_id, nearby_distance
                )
            )


            nearby_velocity = average_velocity(nearby_vehicle_dataframe)

            file.write(
                "Average velocity {}: {:.2f} m/s \n".format(
                    carla_id, nearby_velocity
                )
            )

            file.write(
                f"------------------------------------------------------------\n"
            )
            nearby_vehicle = nearby_vehicles_dataframe.loc[
                nearby_vehicles_dataframe["CarlaId"] == carla_id
            ]

            closest_record = closest_point(
                ergo_dataframe=carla_ego_dataframe, nearby_record=nearby_vehicle
            )
            file.write(
                "Closest record between {} - {}: \n{} \n".format(
                    ego_name, carla_id, closest_record.to_latex()
                )
            )
            miliseconds = seconds_difference_delay(closest_record.iloc[0], last_record=nearby_vehicle.iloc[0])
            file.write("Co-simulation delay {:.3f} ms \n".format(miliseconds))
            file.write(
                f"------------------------------------------------------------\n"
            )
