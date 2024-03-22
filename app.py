import pandas as pd
import streamlit as st

# Read data from the Excel file
file_path = "stockdata.xlsx"
stock_data = pd.read_excel(file_path)

def show_high_beta_top_10_stocks():
    # Sort the data by Beta column in descending order
    sorted_data = stock_data.sort_values(by='Beta', ascending=False)
    # Take top 10 rows
    top_10_stocks = sorted_data.head(10)
    return top_10_stocks

def show_low_beta_stocks():
    # Sort the data by Beta column in ascending order
    sorted_data = stock_data.sort_values(by='Beta')
    return sorted_data.head(10)

def show_high_volatility_stocks():
    # Sort the data by Volatility column in descending order
    sorted_data = stock_data.sort_values(by='Volatility', ascending=False)
    return sorted_data.head(10)

def show_low_volatility_stocks():
    # Sort the data by Volatility column in ascending order
    sorted_data = stock_data.sort_values(by='Volatility')
    return sorted_data.head(10)

def show_high_ROI_stocks():
    # Sort the data by Return_on_Investment column in descending order
    sorted_data = stock_data.sort_values(by='Return_on_Investment', ascending=False)
    return sorted_data.head(10)

def show_low_ROI_stocks():
    # Sort the data by Return_on_Investment column in ascending order
    sorted_data = stock_data.sort_values(by='Return_on_Investment')
    return sorted_data.head(10)

def show_high_CAGR_stocks():
    # Sort the data by CAGR column in descending order
    sorted_data = stock_data.sort_values(by='CAGR', ascending=False)
    return sorted_data.head(10)

def show_low_CAGR_stocks():
    # Sort the data by CAGR column in ascending order
    sorted_data = stock_data.sort_values(by='CAGR')
    return sorted_data.head(10)

def show_high_Debt_to_Equity_Ratio_stocks():
    # Sort the data by Debt_to_Equity_Ratio column in descending order
    sorted_data = stock_data.sort_values(by='Debt_to_Equity_Ratio', ascending=False)
    return sorted_data.head(10)

def show_low_Debt_to_Equity_Ratio_stocks():
    # Sort the data by Debt_to_Equity_Ratio column in ascending order
    sorted_data = stock_data.sort_values(by='Debt_to_Equity_Ratio')
    return sorted_data.head(10)

def show_high_PE_Ratio_stocks():
    # Sort the data by P/E_Ratio column in descending order
    sorted_data = stock_data.sort_values(by='P/E_Ratio', ascending=False)
    return sorted_data.head(10)

def show_low_PE_Ratio_stocks():
    # Sort the data by P/E_Ratio column in ascending order
    sorted_data = stock_data.sort_values(by='P/E_Ratio')
    return sorted_data.head(10)

def show_high_PB_Ratio_stocks():
    # Sort the data by P/B_Ratio column in descending order
    sorted_data = stock_data.sort_values(by='P/B_Ratio', ascending=False)
    return sorted_data.head(10)

def show_low_PB_Ratio_stocks():
    # Sort the data by P/B_Ratio column in ascending order
    sorted_data = stock_data.sort_values(by='P/B_Ratio')
    return sorted_data.head(10)

def show_high_EPS_stocks():
    # Sort the data by EPS column in descending order
    sorted_data = stock_data.sort_values(by='EPS', ascending=False)
    return sorted_data.head(10)

def show_low_EPS_stocks():
    # Sort the data by EPS column in ascending order
    sorted_data = stock_data.sort_values(by='EPS')
    return sorted_data.head(10)

def show_high_Dividend_Yield_stocks():
    # Sort the data by Dividend_Yield column in descending order
    sorted_data = stock_data.sort_values(by='Dividend_Yield', ascending=False)
    return sorted_data.head(10)

def show_low_Dividend_Yield_stocks():
    # Sort the data by Dividend_Yield column in ascending order
    sorted_data = stock_data.sort_values(by='Dividend_Yield')
    return sorted_data.head(10)

# Streamlit UI
def main():
    st.title("Stock Data Query System")
    
    query = st.text_input("Enter your query (e.g., 'show high beta top 10 stocks'):")
    
    if query:
        query = query.lower()
        
        if 'show high beta top 10 stocks' in query:
            result = show_high_beta_top_10_stocks()
            st.write("Top 10 stocks with high beta:")
            st.write(result)
        
        elif 'show low beta stocks' in query:
            result = show_low_beta_stocks()
            st.write("Top 10 stocks with low beta:")
            st.write(result)
        
        elif 'show high volatility stocks' in query:
            result = show_high_volatility_stocks()
            st.write("Top 10 stocks with high volatility:")
            st.write(result)
        
        elif 'show low volatility stocks' in query:
            result = show_low_volatility_stocks()
            st.write("Top 10 stocks with low volatility:")
            st.write(result)
        
        elif 'show high roi stocks' in query:
            result = show_high_ROI_stocks()
            st.write("Top 10 stocks with high Return on Investment:")
            st.write(result)
        
        elif 'show low roi stocks' in query:
            result = show_low_ROI_stocks()
            st.write("Top 10 stocks with low Return on Investment:")
            st.write(result)
        
        elif 'show high cagr stocks' in query:
            result = show_high_CAGR_stocks()
            st.write("Top 10 stocks with high CAGR:")
            st.write(result
