from crewai_tools import tool
import yfinance as yf

class Tools:
    @tool("One month stock price history")
    def stock_price(ticker: str):
        """
        Useful to get a month's worth of stock price data as CSV.
        The input of this tool should a ticker, for example AAPL, NET, TSLA etc...
        """
        stock = yf.Ticker(ticker)
        return stock.history(period="6mo").to_csv()

    @tool("Stock news URLs")
    def stock_news(ticker: str):
        """
        Useful to get URLs of news articles related to a stock.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return list(map(lambda x: x["link"], stock.news))

    @tool("Stock information analysis")
    def stock_information(ticker: str):
        """
        Useful to analyze and retrieve general information about a stock.
        This includes company details like sector, full name, market cap, and more.
        The input to this tool should be a ticker
        """
        stock = yf.Ticker(ticker)
        info = stock.info
        return "\n".join([f"{key}: {value}" for key, value in info.items()])

    @tool("Company's income statement")
    def income_stmt(ticker: str):
        """
        Useful to get the income statement of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.income_stmt.to_csv()

    @tool("Balance sheet")
    def balance_sheet(ticker: str):
        """
        Useful to get the balance sheet of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.balance_sheet.to_csv()

    @tool("Get insider transactions")
    def insider_transactions(ticker: str):
        """
        Useful to get insider transactions of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.insider_transactions.to_csv()
    