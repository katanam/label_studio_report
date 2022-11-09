from pathlib import Path

import pandas as pd

from config_ls_model import Model


def prepare_label_studio_xlsx_report(config: Model):
    path_list = config.source_folder_path.glob('*.txt')  # create list of txt files
    result = {}
    for path in path_list:
        path_number = path.stem.split('_')[0]
        temp = []
        for frame in path.read_text().split('\n'):
            temp.append(Path(frame).stem)
        result[path_number] = temp

    # convert dict to pd.DataFrame for unequal column length:https://stackoverflow.com/a/43866426
    df = pd.DataFrame.from_dict(result, orient='index').T
    df.to_excel(config.target_file_path.with_suffix('.xlsx'), index=False)
    return result


if __name__ == '__main__':
    config_work = Model.parse_file("config_ls_xlsx.json")
    filenames = prepare_label_studio_xlsx_report(config_work)
    print(filenames)
