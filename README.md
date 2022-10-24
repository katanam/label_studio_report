# Label Studio Reporter
* load list of PNG files from *.txt files. 
* for each file: split extension and leave pure file name. 
* write output to new *.txt file or *.xlsx file

## Set up
> git clone git@github.com:katanam/label_studio_report.git

## Quick Start
* Create *.txt files with list of frames in input folder
* Open config_ls.json and change "source_path" correspondingly
* Run script depending on the necessary output format (.txt or .xlsx):
 
  ls_txt_report.py 
  ls_xlsx_report.py
