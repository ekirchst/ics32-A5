# Evan
# ekirchst@uci.edu
# 59946460

from pathlib import Path
import ui as ui
import admin as admin
import user as user
import OpenWeather as opw
import LastFM as lfm
import WebAPI
from ds_client import send
# port = 168.235.86.101


if __name__ == "__main__":

    '''
    main function containing 2 sets of test cases and the code to start my entire program
    '''
    if ui.user() == 1:
        admin.start()
    else:
        user.comm_list()
        user.start()
