from pathlib import Path
from typing import List

from config_ls_model import Model


def prepare_label_studio_txt_report(config: Model) -> List[str]:
    """
    Read .txt files from specified folder, extract filenames and output them to new .txt file.
    Also, it returns the list of filenames.
    :param config: parsed config
    :return: list of filenames
    """
    path_list = config.source_folder_path.glob('*.txt')  # create list of txt files
    result_list = []
    for path in path_list:
        path_number = path.stem.split('_')[0]
        result_list.append(f'frames_{path_number}')
        for frame in path.read_text().split('\n'):
            result_list.append(Path(frame).stem)

    output_path = Path(config.target_file_path)
    output_path.write_text('\n'.join(result_list))
    return result_list


if __name__ == '__main__':
    config_work = Model.parse_file("config_ls_txt.json")
    filenames = prepare_label_studio_txt_report(config_work)
    print(filenames)
