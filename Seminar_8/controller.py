
from distutils.log import info
import import_data
import Input
import export
import logg

def start():
    if Input.user_choice() == '1':
        info = Input.exp()
        export.print_baza(info)
        logg.log_info(info)
    else:
        info= Input.data()
        import_data.add(info)
        logg.log_info(info)




