##########################################################################
# esp 内存大小查看
# esp 外存大小查看
##########################################################################
import micropython
import esp


def flashSize():
    return esp.flash_size() / 1024 / 1024


def mem_info():
    return micropython.mem_info()
