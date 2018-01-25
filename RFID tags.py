import numpy as np
import pandas as pd
# import uuid
#
# df_col = pd.read_excel('Structural Column Schedule.xlsx', sheetname='Stru.Col',skiprows=None,
#                        converters={'element ID':str,'Geschoss':str,'Bauabschnitt':str,'Family and Type':str,
#                                    'WBS code':str})
# """1st line in excel file is counted as the header in pandas"""
# # print(len(df_col.index))
#
# """"generate rfid tags for each of the items"""
# df_col['Delivery ID'] = pd.Series([uuid.uuid4() for i in range(len(df_col))],index=df_col.index)
# df_col['Delivery ID'] = df_col['Delivery ID'].apply(lambda x: str(x))
#
#
# """generate WBS code for each of the items, avoid chain indexing"""
# for i in range(len(df_col.index)):
#     df_col.loc[i,'WBS code']="AS_OE_B1_ST_COL"+"_"+df_col.loc[i,'Geschoss']+"_"+df_col.loc[i,'Bauabschnitt']
# # for i in range(len(df_col.index)):
# #     df_col['WBS code'][i]= "AS_OE_B1_ST_COL"+"_"+df_col['Geschoss'][i]+"_"+df_col['Bauabschnitt'][i]
#
#
# """"generate PO ID for each of the items"""
# for i in range(len(df_col.index)):
#     if "Rechteck Stützen - Vorfabriziert" in str(df_col.loc[i,'Family and Type']):
#         df_col.loc[i,'PO ID'] = str(df_col.loc[i,'WBS code'])+"_" + "RSV" + "_" + str(df_col.loc[i,'element ID'])
#     if "Rund Stütze" in str(df_col.loc[i,'Family and Type']):
#         df_col.loc[i,'PO ID'] = str(df_col.loc[i,'WBS code']) + "_" + "OSV" + "_" + str(df_col.loc[i,'element ID'])
#     if "ortbeton" in str(df_col.loc[i,'Family and Type']):
#         df_col.loc[i,'PO ID'] = str(df_col.loc[i,'WBS code']) + "_" + "INS" + "_" + str(df_col.loc[i,'element ID'])
#
#
#
# df_col.to_excel(pd.ExcelWriter('Structural Column Schedule_all.xlsx',engine='xlsxwriter'), sheet_name='delivery', index=False)



""""assign the product categories"""
df_col1 = pd.read_excel('Structural Column Schedule_cal.xlsx', sheetname='delivery',skiprows=None,
                       converters={'element ID':str,'Geschoss':str,'Bauabschnitt':str,'Family and Type':str,
                                   'WBS code':str, 'Length':str})
subtotal1 = df_col1.groupby(['Family and Type', 'Length']).count()
subtotal2= df_col1.groupby(['Family and Type', 'Bauabschnitt']).count()
print(subtotal1,subtotal2)
# print(subtotal.shape)
# print(len(subtotal))

