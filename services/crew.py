import yfinance as yf
from langchain_openai import ChatOpenAI
from crewai import Crew
from crewai.process import Process
from services.agent import Agents
from services.task import Tasks

class StockAnalyst:
    """
    주식 분석 작업을 관리하는 클래스.
    """
    def __init__(self, model='gpt-4o-mini', verbose=True):
        """
        StockAnalyst 클래스 초기화
        :param model: 사용할 LLM 모델 이름 (default: gpt-4o-mini)
        :param verbose: 작업 실행 시 로그 출력 여부
        """
        self.model = model
        self.verbose = verbose
        self.crew = None
        self._initialize_agents_and_tasks()

    def _initialize_agents_and_tasks(self):
        """
        에이전트와 작업을 초기화합니다.
        """
        # 에이전트와 작업 객체 생성
        agents = Agents()
        tasks = Tasks()

        # 에이전트 생성
        self.researcher = agents.researcher()
        self.technical_analyst = agents.technical_analyst()
        self.financial_analyst = agents.financial_analyst()
        self.hedge_fund_manager = agents.hedge_fund_manager()

        # 작업 생성
        research_task = tasks.research(self.researcher)
        technical_task = tasks.technical_analysis(self.technical_analyst)
        financial_task = tasks.financial_analysis(self.financial_analyst)
        recommend_task = tasks.investment_recommendation(
            self.hedge_fund_manager,
            [
                research_task,
                technical_task,
                financial_task,
            ],
        )

        # Crew 객체 생성
        self.crew = Crew(
            agents=[
                self.researcher,
                self.technical_analyst,
                self.financial_analyst,
                self.hedge_fund_manager,
            ],
            tasks=[
                research_task,
                technical_task,
                financial_task,
                recommend_task,
            ],
            verbose=self.verbose,
            manager_llm=ChatOpenAI(model=self.model),
            process=Process.sequential, # sequential || hierarchical
            # memory=True,
        )

    def get_analyst_result(self, name):
        """
        주식 분석 결과를 가져옵니다.
        :param name: 분석할 회사 이름 또는 티커
        :return: 분석 결과
        """
        
        if not name:
            raise ValueError(f"'name' 파라미터가 올바르지 않습니다.: {name}")
        
        # 입력받은 name이 유효한 ticker인지 확인
        try:
            ticker = yf.Ticker(name)
            info = ticker.info
            
            # 'symbol'를 확인하여 유효성 검증
            if 'symbol' not in info or info['symbol'] is None:
                return f"'{name}'은(는) 유효한 티커가 아닙니다."
            
        except Exception as e:
            raise ValueError(f"'{name}'에 대해 티커 검증 중 오류가 발생했습니다: {e}")
        
        result = self.crew.kickoff(
            inputs=dict(
                company=name,
                ticker=name,
            ),
        )
        return result
    
class EtfAnalyst:
    """
    ETF 지수 분석 작업을 관리하는 클래스.
    """
    def __init__(self, model='gpt-4o-mini', verbose=True):
        """
        EtfAnalyst 클래스 초기화
        :param model: 사용할 LLM 모델 이름 (default: gpt-4o-mini)
        :param verbose: 작업 실행 시 로그 출력 여부
        """
        self.model = model
        self.verbose = verbose
        self.crew = None
        self._initialize_agents_and_tasks()

    def _initialize_agents_and_tasks(self):
        """
        에이전트와 작업을 초기화합니다.
        """
        # 에이전트와 작업 객체 생성
        agents = Agents()
        tasks = Tasks()

        # Agent 생성
        self.researcher = agents.researcher()
        self.info_analyst = agents.info_analyst()
        self.technical_analyst = agents.technical_analyst()
        self.hedge_fund_manager = agents.hedge_fund_manager()

        # Task 생성
        research_task = tasks.research(self.researcher)
        info_analyst_task = tasks.info_analysis(self.info_analyst)
        technical_task = tasks.technical_analysis(self.technical_analyst)
        recommend_task = tasks.investment_recommendation(
            self.hedge_fund_manager,
            [
                research_task,
                info_analyst_task,
                technical_task,
            ],
        )

        # Crew 객체 생성
        self.crew = Crew(
            agents=[
                self.researcher,
                self.info_analyst,
                self.technical_analyst,
                self.hedge_fund_manager,
            ],
            tasks=[
                research_task,
                technical_task,
                info_analyst_task,
                recommend_task,
            ],
            verbose=self.verbose,
            manager_llm=ChatOpenAI(model=self.model),
            process=Process.sequential, # sequential || hierarchical
            # memory=True,
        )

    def get_analyst_result(self, name):
        """
        분석 결과를 가져옵니다.
        :param name: 분석할 회사 이름 또는 티커
        :return: 분석 결과
        """
        
        if not name:
            raise ValueError(f"'name' 파라미터가 올바르지 않습니다.: {name}")
        
        # 입력받은 name이 유효한 ticker인지 확인
        try:
            ticker = yf.Ticker(name)
            info = ticker.info
            
            # 'symbol'를 확인하여 유효성 검증
            if 'symbol' not in info or info['symbol'] is None:
                return f"'{name}'은(는) 유효한 티커가 아닙니다."
            
        except Exception as e:
            raise ValueError(f"'{name}'에 대해 티커 검증 중 오류가 발생했습니다: {e}")
        
        result = self.crew.kickoff(
            inputs=dict(
                company=name,
                ticker=name,
            ),
        )
        return result
    