from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")

def createTheme(title_en,title_zh):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:
            session.run("""
                CREATE (:Theme {title_en:$title_en, title_zh:$title_zh})
            """, title_zh=title_zh, title_en=title_en)
 
theme = [
     {
        'title_en':"The Science of Well-being",
        'title_zh':"健康生活的科学"
     },
     {
        'title_en':"Focus, Productivity and Creativity",
        'title_zh':"专注，效率与创造力"
     },
     {
        'title_en':"Mental Health and Addiction",
        'title_zh':"心理健康与成瘾"
     }
 ]

for item in theme:
    createTheme(title_en=item['title_en'],title_zh=item['title_zh'])