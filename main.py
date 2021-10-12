from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")

# chinook.pretty_print("SELECT * FROM Album")

# chinook.pretty_print("SELECT * FROM Artist")

chinook.pretty_print("SELECT * FROM Invoice")


# JOIN
# - So far we can only see the IDs of customers, but not their names.
#   We'd also like to see the customer's city (BillingCity) and how much they paid.
# - But this data comes from two different tables... how can we query both
#   at the same time?
# - We will use a JOIN command in our SQL sentence - more precisely the INNER JOIN

chinook.pretty_print("""SELECT Invoice.CustomerId, Customer.FirstName, Customer.LastName, Invoice.BillingCity, Invoice.Total
                        FROM Invoice
                        INNER JOIN Customer 
                        ON Invoice.CustomerId=Customer.CustomerId;
                    """)

# WHERE
# How would you update the above SQL query to only show invoices from Stockholm customers?
chinook.pretty_print("""SELECT Invoice.CustomerId, Customer.FirstName, Customer.LastName, Invoice.BillingCity, Invoice.Total
                        FROM Invoice
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                        WHERE Invoice.BillingCity='Stockholm';
                    """)

# SUM, AVG(average), GROUP BY, MAX(the highest entry), MIN(the cheapest order)
# We can see that all the Stockholm orders come from the same man: Joakim Johansson. How can we calculate a sum of his orders?
chinook.pretty_print("""SELECT SUM(Invoice.Total)
                        FROM Invoice
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                        WHERE Invoice.BillingCity='Stockholm';
                    """)

# What if we'd like to find out what's the orders total for every customer individually, not only Joakim? We could use
# a GROUP BY command which groups all the invoices based on the same CustomerId:
chinook.pretty_print("""SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total)
                        FROM Invoice
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                        GROUP BY Invoice.CustomerId;
                    """)

# HOMEWORK

# What order (Invoice) was the most expensive? Which one was the cheapest?
chinook.pretty_print("""SELECT MAX (Invoice.Total), *
                        FROM Invoice;
                    """)

# Which one was the cheapest?
chinook.pretty_print("""SELECT MIN(Invoice.Total), *
                        FROM Invoice;
                    """)

# Which city (BillingCity) has the most orders?
chinook.pretty_print("""SELECT Invoice.BillingCity, COUNT (*) AS Invoice_num 
                        FROM Invoice
                        GROUP BY Invoice.BillingCity
                        ORDER BY Invoice_num DESC; 
                    """)

# Calculate (or count) how many tracks have this MediaType: Protected AAC audio file
chinook.pretty_print("""SELECT COUNT(*)
                        FROM MediaType
                        INNER JOIN Track ON Track.MediaTypeId=MediaType.MediaTypeId
                        WHERE MediaType.Name='Protected AAC audio file';
                    """)

# Find out what Artist has the most albums?
chinook.pretty_print("""SELECT Artist.Name, COUNT(*) as Album_num
                         FROM Album
                         JOIN Artist ON Album.ArtistId=Artist.ArtistId
                         GROUP BY Album.ArtistId
                         ORDER BY Album_num DESC;
                    """)

# What genre has the most tracks?
chinook.pretty_print("""SELECT Genre.Name, COUNT(*) as Track_num
                        FROM Genre
                        JOIN Track ON Genre.GenreId=Track.GenreId
                        GROUP BY Track.GenreId
                        ORDER BY Track_num DESC;
                    """)

# Which customer spent the most money so far?
chinook.pretty_print("""SELECT Invoice.CustomerId, Customer.FirstName, Customer.LastName, Customer.City, SUM(Invoice.Total) as Invoice_sum
                        FROM Invoice
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                        GROUP BY Invoice.CustomerId
                        ORDER BY Invoice_sum DESC;
                    """)

# What songs were bought with each order?
chinook.print_tables("SELECT * FROM Track")
chinook.pretty_print("""SELECT Invoice.InvoiceId, Track.Name
                        FROM Invoice
                        JOIN InvoiceLine ON InvoiceLine.InvoiceId=Invoice.InvoiceId
                        JOIN Track ON InvoiceLine.TrackId=Track.TrackId
                    """)
