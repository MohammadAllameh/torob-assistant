from crewai import Agent,Task,Crew,LLM
from crewai_tools import CSVSearchTool
from autoscraper import AutoScraper
import pandas as pd
# from crewai_tools import CSVSearchTool



url="https://torob.com/browse/522/%DA%A9%D8%A7%D8%B1%D8%AA-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9-graphic-card/b/29/asus-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3/?page=1&size=5"

product = ["کارت گرافیک ایسوس مدل Dual GeForce RTX™ 4060 OC Edition حافظه 8 گیگابایت","کارت گرافیک ایسوس مدل TUF Gaming GeForce RTX™ 4060 Ti OC Edition حافظه 8 گیگابایت"]
price = ["از ۱۹٫۴۹۰٫۰۰۰ تومان"]

# scraper = AutoScraper()
# print("start")
# pr = scraper.build(url, product)
# prc = scraper.build(url, price)

# dataFm=pd.DataFrame({"product":pr,"price":prc})



# dataFm.to_csv("demo.csv")
# output_lines = [f"{p} - {c}" for p, c in zip(pr, prc)] 
# with open("demofile3.txt", "w", encoding="utf-8") as f:
#     for line in output_lines:
#         f.write(f"{line}\n")

# print(pr)
# with open("demofile3.txt", "w", encoding="utf-8") as f:
#     f.write(f"File content: {pr} \n  File content: {prc}")


llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

df = pd.read_csv('demo.csv')

tool = CSVSearchTool(csv='demo.csv')

filereader = Agent(
    role = "filereader",
    description="read file and save it in your memory",
    goal = "read products with prices",
    backstory = "you are a expert online shop advisor",
    llm=llm,
    # memory=True,
    # verbose=True
    tools=[tool]
)
inp = input("what a quesiton?")

flereadertask = Task(
    description = inp,
    expected_output = "please show me the products with its price ",
    agent = filereader
)

myCrew = Crew(agents=[filereadertask],tasks=[flereadertask])

resualt = myCrew.kickoff()

print(resualt)
