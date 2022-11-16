from pathlib import Path
from typing import List

from config_ls_model import Model
from ls_common_report import get_frame_dict


def prepare_label_studio_txt_report(config: Model) -> List[str]:
    """
    Read .txt files from specified folder, extract filenames and output them to new .txt file.
    Also, it returns the list of filenames.
    :param config: parsed config
    :return: list of filenames
    """
    frame_dict = get_frame_dict(config)
    result_list = []
    for case_id in frame_dict:
        result_list.append(case_id)
        for frame in frame_dict[case_id]:
            result_list.append(frame)
    output_path = Path(config.target_file_path)
    output_path.write_text('\n'.join(result_list))
    return result_list


if __name__ == '__main__':
    config_work = Model.parse_file("config_ls_txt.json")
    filenames = prepare_label_studio_txt_report(config_work)
    print(filenames)
