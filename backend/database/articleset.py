from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")


# 创建articleset
def createArticleSet(sourceVideoURL, title_en,title_zh,theme,intro_en,intro_zh):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            session.run("""
                MATCH (t:Theme {title_en:$theme})
                CREATE (:ArticleSet {sourceVideoURL:$sourceVideoURL, title_en:$title_en, title_zh:$title_zh,intro_en:$intro_en,intro_zh:$intro_zh})-[:BELONGS_TO]->(t)
            """, theme=theme,sourceVideoURL=sourceVideoURL,title_en=title_en,title_zh=title_zh,intro_en=intro_en,intro_zh=intro_zh)


# 找到某个theme下的asList
def getArticleSetList(themeTitle_en):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            res = session.run("""
                MATCH (as:ArticleSet)-[:BELONGS_TO]->(:Theme {title_en:$themeTitle_en})
                RETURN as.title_en as title_en,as.title_zh as title_zh, as.intro_en as intro_en, as.intro_zh as intro_zh
            """,themeTitle_en=themeTitle_en)

            return res.data()


# 找到某个article set的article列表
def getArticleSet(articleSetTitle_en):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            res = session.run("""
                MATCH (as:ArticleSet {title_en:$articleSetTitle_en})-[:HAS]->(a:Article)
                RETURN a.title_en as title_en,a.title_zh as title_zh,a.summary_en as summary_en,a.summary_zh as summary_zh,as.title_zh as articleSetTitle_zh
                ORDER BY a.sequence
            """,articleSetTitle_en=articleSetTitle_en)

            return res.data()
        

