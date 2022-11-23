import pandas as pd
import sys

df = pd.read_csv('Education.csv', index_col=0)

clean_cols = [
    # Location & ID data
    'Federal Information Processing Standard (FIPS) Code', 
    'State',
    'Area name',
    'Year',
    # Education Data
    'Less than a high school diploma',
    'High school diploma only',
    'Some college or associate\'s degree',
    'Bachelor\'s degree or higher',
    'Percent of adults with less than a high school diploma',
    'Percent of adults with a high school diploma only',
    'Percent of adults completing some college or associate\'s degree',
    'Percent of adults with a bachelor\'s degree or higher'
]
education_cols = [
    'Less than a high school diploma',
    'High school diploma only',
    'Some college or associate\'s degree',
    'Bachelor\'s degree or higher',
    'Percent of adults with less than a high school diploma',
    'Percent of adults with a high school diploma only',
    'Percent of adults completing some college or associate\'s degree',
    # 'Percent of adults with a bachelor\'s degree or higher'
]

cleandf_rows = []

for index, row in df.iterrows():
    
    for year_range in ['2007-11', '2016-20']:
        # Get year range as list of ints
        start_year, end_year = year_range.split('-')
        end_year = f'20{end_year}'
        years = [x for x in range(int(start_year), int(end_year)+1)]

        for year in years:
            # ID Data
            new_row = [   
                row['Federal Information Processing Standard (FIPS) Code'], 
                row['State'],
                row['Area name'],
                year
            ]
            # Education Data
            for ed in education_cols:
                rowValue = row[f'{ed}, {year_range}']
                if isinstance(rowValue, str):
                    rowValue = ''.join(rowValue.split(','))
                new_row += [rowValue]

            # Percent BACHELOR'S DEGREE COLS
            if year_range == '2007-11':
                new_row += [row[f'Percent of adults with a bachelor\'s degree or higher 2007-11']]     # NO COMMA for year
            elif year_range == '2016-20':
                new_row += [row[f'Percent of adults with a bachelor\'s degree or higher 2015-19']]

            cleandf_rows.append(new_row)
            
cleandf = pd.DataFrame(cleandf_rows, columns=clean_cols)
cleandf.to_csv('../Education_NumsCleaned.csv', index=False)


