import geosoft.gxapi as gxapi
import geosoft.gxpy.gdb as gxdb
import geosoft.gxapi as gxapi
import numpy as np
import PySimpleGUI as sg

LINE_TYPE_NORMAL = gxapi.DB_LINE_TYPE_NORMAL


sg.theme('LightGreen1')

#Run file browser via PySimpleGUI and create list from text file


# Run Oasis table look up
def rungx():

    layout = [[sg.Input(key = '_REA_', enable_events=True),sg.FileBrowse(target = '_REA_')],
    [sg.Text('Choose input channel'),sg.Combo(['    '], key = 'combo1')],
    [sg.Button('Do 1ch Table LookUp', key = 'but1')]]
    window = sg.Window("1ch Table Look Up via UAV to OM", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '_REA_':
            list_chanell_db = gxdb.Geosoft_gdb.open()
            chan_dict = gxdb.Geosoft_gdb.list_channels(list_chanell_db)
            chan_list = list(chan_dict.keys())
            window.Element('combo1').update(values=chan_list)
            line_name_ = gxdb.create_line_name(number=0, line_type=LINE_TYPE_NORMAL, version=0)
            line_x_array = gxdb.Geosoft_gdb.read_channel(list_chanell_db,line=line_name_,channel = 'Time')
            window.BringToFront()
        if event == 'but1':
            tblname = values['_REA_']
            ascii_tbl_read = open(tblname,'r')
            tbl = ascii_tbl_read.readlines()
            time = []
            param = []
            for i in range(len(tbl)):
                timei = tbl[i].replace('\n','')
                temp1 = timei.split(' ')
                time.append(temp1[0])
                param.append(temp1[1])
            time.remove('time')
            param.remove('param')
            print(param)
            break
    window.close()

    list_chanell_db = gxdb.Geosoft_gdb.open()
    line_name_ = gxdb.create_line_name(number=0, line_type=LINE_TYPE_NORMAL, version=0)
    line_x_array = gxdb.Geosoft_gdb.read_channel(list_chanell_db,line=line_name_,channel = 'Time') 
    line_x_array_split =  line_x_array[0]
    res_param = np.zeros(len(line_x_array_split))
    print('Len res_param: ',len(res_param))
    adress_time = np.array(time,dtype = float)
    print(adress_time)
    param_for_lu = np.array(param,dtype = float)
    for i in range(len(line_x_array_split)):
        for j in range(len(adress_time)):
            if line_x_array_split[i]==adress_time[j]:
                res_param[i] = param_for_lu[j]
    res_param = np.array(res_param,dtype = str)
    for i in range(len(res_param)):
        if res_param[i]=='0.0':
            res_param[i]='*'
    print(res_param)
    input_chan_name = values['combo1']
    print(input_chan_name)
    gxdb.Geosoft_gdb.write_channel(list_chanell_db,line=line_name_,channel = input_chan_name,data = res_param,fid=(0.0, 1.0), unit_of_measure=None)

    # Correctness push
    gxapi.GXSYS.display_message("GX Python","Table Look Up Succesful")
    gxdb.Geosoft_gdb.close(list_chanell_db)
