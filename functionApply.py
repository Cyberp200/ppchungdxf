#functionApply.py
#2022-05-09
#Script to highlight all the types of functions that ezdxf library has.

'''
_______ __   __ ______  _______  ______      _______ _______ _     _
|         \_/   |_____] |______ |_____/      |______ |  |  | |_____|
|_____     |    |_____] |______ |    \_      |______ |  |  | |     |

'''
#CYBER ENGINEERING FOR MATERIAL HANDLING

#cyberp200@rocketmail.com (github)
#ppchung@gmx.com
#562-480-2114

'''---imports---'''
import ezdxf

'''---vars---'''

'''---script debug label---'''
print('\ndebug: functionApply.py\n')

'''---main---'''

#   make new DXF files
drawing01 = ezdxf.new()

#   set the units
#       0 Unitless, 1 In, 2 Ft, 4 mm
drawing01.header['$INSUNITS'] = 1

modelSpace = drawing01.modelspace()

points01 = [(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)]
modelSpace.add_lwpolyline(points01)

drawing01.saveas("lwpolyline1.dxf")

'''---functions---'''
