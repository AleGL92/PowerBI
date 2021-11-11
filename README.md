# PowerBI
This is an example of a PowerBi Dashboard. The first dashboard shows metric tons of recycled glass per year and the comparison with the previous year. The second one shows kg of recycled glass per habitants and habitants per number of containers. As the data is downloaded directly from Github, it's possible to download the pbix file, and run it with the dashboard already working.

Before starting to make the dashboard, it's useful to prepare the data. It was given in xlsx format, so we transform it to csv, which is better for Github, as we can see the preview, get the raw link easier and download it from Power BI easily. In this process, we need  to select UTF-8 csv type, as we have some cells with the characters 'í', 'ó' and 'ñ'.

The real values of the column 'cantidad' have been modified, as requested by the provider of the data. Also, there was another deleted column called 'matricula' which was the real plate number of the vehicles picking up the glass for recycling. Both tasks have been done with the Python code called DATA_MOD.py.

There are 5 csv files uploaded to this repository, and can be downloaded directly to Power BI, from the 'Get data' menu, then selecting from web data source, and finally, pasting the link of each csv in Github.  After importing the csv files to PowerBI, some name files were changed. Dimensiones2 its now called UG_INE, Dimensiones1 is now UG_COM_PROV, and all the others were left with the original name.

Some of the UG numbers, wich is going our primary key for linking all the tables, come in number format by default. We need to click in 'Transform Data', and change the type to text, so that we dont lose zeros appearing before numbers. Also we need to change the data type from the 'cantidad' column to decimal number, as they come originally as text. This process has been repeated for some more columns, in the cases where the format wasnt the right.

Once we have all the right formats for the data, we append the csv containing year 2020 data, with the csv containing the 2 other years. This way, we can write DAX easily. Now we can select the data in each year writing a DAX like the following one:

Year 18 = CALCULATE(SUM(E_18_19_20[CANTIDAD]), E_18_19_20[FECHA_MOVIMIENTO].[YEAR] = 2018)

And to compare with the previous years, we could use:

Var 19vs18 = [Year 19]/[Year 18]-1 (then selecting percentage format)

Finally, we can make the map graphic. First we select the CCAA columns and then, we select conditional format between all the format options in the visualization. If the value is higher or lower that the average, it will show the selected colour.

The created dashboard and the panel should be accessible in the folowing link to my Power Bi workspace:

https://app.powerbi.com/groups/me/reports/2c12eb24-60eb-4b5b-b012-e09903f05285?ctid=0a925443-5411-4877-9346-300463b8e10f&pbi_source=linkShare
