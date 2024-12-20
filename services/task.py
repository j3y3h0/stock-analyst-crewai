from crewai import Task
from datetime import datetime

class Tasks:
    def research(self, agent):
        today = datetime.today()
        year_month = today.strftime("%Y%m")
        day = today.strftime("%d")
        file_dir = f"./results/{year_month}/{day}"
        file_dir += "/01_stock_news.md"

        return Task(
            description="Gather and analyze the latest news and market sentiment surrounding the stock of {company}. Provide a summary of the news and any notable shifts in market sentiment.",
            expected_output=f"Your final answer MUST be a detailed summary of the news and market sentiment surrounding the stock. Include any notable shifts in market sentiment and provide insights on how these factors could impact the stock's performance. Use Korean",
            agent=agent,
            output_file=file_dir,
        )

    def technical_analysis(self, agent):
        today = datetime.today()
        year_month = today.strftime("%Y%m")
        day = today.strftime("%d")
        file_dir = f"./results/{year_month}/{day}"
        file_dir += "/02_technical_analysis.md"

        return Task(
            description="Conduct a detailed technical analysis of the price movements of {company}'s stock and trends identify key support and resistance levels, chart patterns, and other technical indicators that could influence the stock's future performance. Use historical price data and technical analysis tools to provide insights on potential entry points and price targets.",
            expected_output=f"Your final answer MUST be a detailed technical analysis report that includes key support and resistance levels, chart patterns, and technical indicators. Provide insights on potential entry points, price targets, and any other relevant information that could help your customer make informed investment decisions. Use Korean",
            agent=agent,
            output_file=file_dir,
        )
    
    def info_analysis(self, agent):
        today = datetime.today()
        year_month = today.strftime("%Y%m")
        day = today.strftime("%d")
        file_dir = f"./results/{year_month}/{day}"
        file_dir += "/02_stock_info_analysis.md"

        return Task(
            description="Analyze and summarize the key fundamental information of {company}'s stock. Include sector, market cap, P/E ratio, 52-week high and low, and other notable financial metrics.",
            expected_output=f"Your final answer MUST be a detailed analysis of the key fundamental information of the stock. Include the sector, market cap, P/E ratio, beta, dividend yield, 52-week high and low, current price, and a short company summary. Use Korean.",
            agent=agent,
            output_file=file_dir,
        )

    def financial_analysis(self, agent):
        today = datetime.today()
        year_month = today.strftime("%Y%m")
        day = today.strftime("%d")
        file_dir = f"./results/{year_month}/{day}"
        file_dir += "/03_financial_analysis.md"

        return Task(
            description="Analyze {company}'s financial statements, insider trading data, and other financial metrics to evaluate the stock's financial health and performance. Provide insights on the company's revenue, earnings, cash flow, and other key financial metrics. Use financial analysis tools and models to assess the stock's valuation and growth potential.",
            expected_output=f"Your final answer MUST be a detailed financial analysis report that includes insights on the company's financial health, performance, and valuation. Provide an overview of the company's revenue, earnings, cash flow, and other key financial metrics. Use financial analysis tools and models to assess the stock's valuation and growth potential. Use Korean",
            agent=agent,
            output_file=file_dir,
        )

    def investment_recommendation(self, agent, context):
        today = datetime.today()
        year_month = today.strftime("%Y%m")
        day = today.strftime("%d")
        file_dir = f"./results/{year_month}/{day}"
        file_dir += "/04_investment_recommendation.md"

        return Task(
            description="Based on the research, technical analysis, and financial analysis reports, provide a detailed investment recommendation for {company}'s stock. Include your analysis of the stock's potential risks and rewards, and provide a clear rationale for your recommendation.",
            expected_output=f"Your final answer MUST be a detailed investment recommendation report to BUY or SELL the stock that includes your analysis of the stock's potential risks and rewards. Provide a clear rationale for your recommendation based on the research, technical analysis, and financial analysis reports. Use Korean, Don't Use Markdown",
            agent=agent,
            context=context,
            output_file=file_dir,
        )
