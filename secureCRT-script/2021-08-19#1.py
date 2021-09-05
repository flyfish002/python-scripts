# $language = "Python"

# $interface = "1.0"

import  os

#file_dir = 'D:\\BaiduNetdiskDownload\\2021-08-24\\'
#file_list = os.listdir(file_dir)
file_prefix = 'D:\\BaiduNetdiskDownload\\'
sec_numer = 2  #当前文件夹切换为2个部分上传


#__file__  当前执行程序目录文件名，包含绝对路径
#os.path.split(__file__)[0]  当前执行文件目录
#os.path.split(__file__)[1]  当前执行文件程序名
#os.path.splitext(os.path.basename(__file__))[0]  当前文件名
#os.path.splitext(os.path.basename(__file__))[1]  当前文件名后缀
exec_filename           =  os.path.splitext(os.path.basename(__file__))[0]
exec_filename_list      =  exec_filename.split( "#" )
ar_file_dir_name        =  exec_filename_list[0]    # 2020-03-10
sec_seq                 =  int( exec_filename_list[1] ) -1   #1
file_full_dir_prefix    =  str( file_prefix + ar_file_dir_name + "\\" )
ar_file_list            =  os.listdir( file_full_dir_prefix )   
#crt.Dialog.MessageBox( file_full_dir_prefix )    D:\BaiduNetdiskDownload\2020-03-10

for i  in range ( 0,  len( ar_file_list ) ):
#   if i %  sec_numer  == sec_seq :
      file_abs_path = os.path.join( file_full_dir_prefix, ar_file_list[i] )  #D:\BaiduNetdiskDownload\2020-03-10\534679-535021-v2.ar
    #  crt.Dialog.MessageBox( file_full_dir_prefix )
    #  crt.FileTransfer.AddToUploadList( file_abs_path ) 
      crt.FileTransfer.AddToUploadList( file_full_dir_prefix ) 
      crt.Screen.Send("rz\n")


