import pyodbc
import streamlit as st
import pandas

connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:azureserverjohn.database.windows.net,1433;Database=azure_db_John;Uid=azureuser;Pwd=Realmadrid8989;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT 
TOP 5 c.CustomerID, 
c.CompanyName, 
COUNT(soh.SalesOrderID) AS OrderCount 
FROM 
SalesLT.Customer AS c 
LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID 
GROUP BY 
c.CustomerID, 
c.CompanyName 
ORDER BY 
OrderCount DESC;
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)

if st.button('Get data'):
    records = cursor.fetchall()
    # Assuming 'records' is the list of records you got from the SQL query
    # And each record is a tuple (CustomerID, CompanyName, OrderCount)
    list_record = []

    for r in records:
        #print(f"{r.CustomerID}\t{r.OrderCount}\t{r.CompanyName}")
        list_record.append([r[0],r[1],r[2]])

    df_customer_order = pd.DataFrame(list_record, columns=['CustomerID', 'CompanyName', 'OrderCount'])
    st.dataframe(df_customer_order)