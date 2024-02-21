from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")


# 创建articleset
def createArticleSet(sourceVideoURL, title_en,title_zh,theme,intro):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            session.run("""
                MATCH (t:Theme {title_en:$theme})
                CREATE (:ArticleSet {sourceVideoURL:$sourceVideoURL, title_en:$title_en, title_zh:$title_zh,intro:$intro})-[:BELONGS_TO]->(t)
            """, theme=theme,sourceVideoURL=sourceVideoURL,title_en=title_en,title_zh=title_zh,intro=intro)


