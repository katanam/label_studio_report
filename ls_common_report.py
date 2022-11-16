from pathlib import Path


def get_frame_dict(config):
    path_list = config.source_folder_path.glob('*.txt')  # create list of txt files
    result = {}
    for path in path_list:
        case_id = path.stem.split('_')[0]
        temp = []
        for frame in path.read_text().split('\n'):
            temp.append(Path(frame).stem)
        result[f'frames_{case_id}'] = temp

    return result
