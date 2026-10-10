# Welcome to BookStore Inventory And Analytics System Project


from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# main class for bookstore management
class Bookstore:



     # Load the dataset
    def __init__(self):
        self.inventory = pd.read_csv("inventory.csv")
        self.sales = pd.read_csv("sales.csv")




     # Add a new book 
    def add_book(self, title, author, genre, price, quantity):
        
        if price > 0 and quantity > 0:
            new_book = [title, author, genre, price, quantity]
            self.inventory.loc[len(self.inventory)] = new_book
            print("Book added to inventory.")
        else:
            print("Error: Price and quantity must be positive.")





    # Update the inventory 
    def update_inventory(self, title, quantity):
        if quantity > 0:
            for index, row in self.inventory.iterrows():
                if row['Title'] == title:
                    self.inventory.at[index, 'Quantity'] = row['Quantity'] + quantity
                    print("Inventory updated.")
                    return
            print("Error: Book not found.")
        else:
            print("Error: Quantity must be positive.")





    # Record the sale 
    def record_sale(self, title, quantity):
        for index, row in self.inventory.iterrows():
            if row['Title'] == title:
                if row['Quantity'] >= quantity:

                    # Update stock
                    self.inventory.at[index, 'Quantity'] = row['Quantity'] - quantity
                    
                    # Calculate revenue
                    revenue = quantity * row['Price']
                    
                    # Add to sales dataset
                    new_sale = ["2026-10-10", title, quantity, revenue]
                    self.sales.loc[len(self.sales)] = new_sale
                    print("Sale recorded successfully.")
                    return

                else:
                    print("Not enough stock available.")
                    return
        print("Error: Book not found.")





    # Generate the report
    def generate_report(self):
        print("\n--- Summary Report ---")
        
        # Use NumPy for numerical analysis
        revenue_array = self.sales['Total Revenue'].values
        price_array = self.inventory['Price'].values
        
        total_revenue = np.sum(revenue_array)
        average_price = np.mean(price_array)
        
        print("Total Revenue: ", total_revenue)
        print("Average Book Price: ", average_price)
        print("\nInventory:")
        print(self.inventory[['Title', 'Quantity']])





     # Visualize the data
    def visualize_data(self):
        merged_data = pd.merge(self.sales, self.inventory, on='Title')


        
        # 1. Bar Chart: Total sales by genre
        genre_sales = merged_data.groupby('Genre')['Quantity Sold'].sum()

        plt.figure(figsize=(7, 4))

        plt.bar(genre_sales.index, genre_sales.values, color='blue')

        plt.title("Total Sales by Genre")

        plt.xlabel("Genre")

        plt.ylabel("Total Sold")

        plt.show()




        # 1.1 Bar Chart: Total sales by author
        author_sales = merged_data.groupby('Author')['Quantity Sold'].sum()
        
        plt.figure(figsize=(7 , 4))
        
        plt.bar(author_sales.index, author_sales.values, color='green') 
        
        plt.title("Total Sales by Author")
        
        plt.xlabel("Author")        
        
        plt.ylabel("Total Sold")
        
        plt.show()
        




        # 2. Line Graph: Monthly sales trends

        # Basic string slicing to get YYYY-MM from Date
        month_list = []
        for date in self.sales['Date']:
            month_list.append(date[0:7])
            
        self.sales['Month'] = month_list
        monthly_sales = self.sales.groupby('Month')['Total Revenue'].sum()

        
        plt.figure(figsize=(7, 4))

        plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='green')

        plt.title("Monthly Sales Trends")

        plt.xlabel("Month")

        plt.ylabel("Revenue")

        plt.show()




        # 3. Pie Chart: Revenue share by book genre
        genre_revenue = merged_data.groupby('Genre')['Total Revenue'].sum()
        plt.figure(figsize=(6, 6))

        plt.pie(genre_revenue.values, labels=genre_revenue.index, autopct='%1.1f%%')

        plt.title("Revenue Share by Book Genre")

        plt.show()




        # 4. Heatmap: Correlation between book prices and sales volumes[cite: 3]
        book_stats = merged_data.groupby('Title')[['Price', 'Quantity Sold']].sum()
        plt.figure(figsize=(6, 4))

        sns.heatmap(book_stats.corr(), annot=True, cmap='Blues')

        plt.title("Correlation between Book Prices and Sales")

        plt.show()




# Create bookstore object
store = Bookstore()


# Test the functionalities
print("Testing Add Book:")
store.add_book("HTML Basics", "John Smith", "Technology", 20.0, 30)

print("\nTesting Update Inventory:")
store.update_inventory("Python Basics", 10)

print("\nTesting Record Sale:")
store.record_sale("Data Science 101", 5)

print("\nTesting Reports:")
store.generate_report()

print("\nGenerating Visualizations...")
store.visualize_data()







     
































































































































