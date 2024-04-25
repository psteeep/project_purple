import json
import os


def get_cfg(json_file_path):
    with open(json_file_path, 'r') as cfg_file:
        cfg_dict = json.load(cfg_file)

    return cfg_dict


def process_cfg(json_file_path):
    config, _ = get_cfg(json_file_path)
    config.summary_dir = os.path.join("../experiments", config.exp_name, "summary/")
    config.checkpoint_dir = os.path.join("../experiments", config.exp_name, "checkpoint/")
    return config
