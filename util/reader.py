from loguru import logger


def load_dataset(args):
    path_carla = args.path_carla
    logger.info('{}: {}'.format("PATH TO FILE", path_carla))
    return 0
