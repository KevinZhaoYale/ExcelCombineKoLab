import pandas as pd
import glob
import GlobalVariables as globvar



file_list = glob.glob(globvar.path + globvar.file_type)
print('File names:', file_list)
#check to make sure all your files are here

output = pd.DataFrame()

for file in file_list:
   df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)

   output = output.append( df, ignore_index=True)

print('Final Excel sheet now generated at location', globvar.output_location)
output.to_excel(globvar.output_location, index=False)