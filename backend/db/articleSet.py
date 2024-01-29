from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")



# 检查指定的ArticleSet是否存在
def articleSetExists(url):
   
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                    MATCH (v:ArticleSet {url:$url}) 
                    return (v)
                """, url=url)
            
            return len(result.data()) > 0


# 创建ArticleSet，同时指定所属的theme
def createArticleSet(url, title, themeName):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
    
            session.run("""
                MATCH (t:Theme {name:$name})
                CREATE (:ArticleSet {url:$url, title:$title})-[:BELONGS_TO]->(t)
            """, name=themeName, title=title, url=url)
 

# 获取某个ArticleSet的所有的Article
def getAllArticle(articleSetTitle):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (:ArticleSet {title:$title})<-[:GENERATED_FROM]-(n:Article)
                RETURN n as article, ID(n) as id
                ORDER BY n.sequence
            """,title=articleSetTitle)
            result = [{'title':item['article']['title'], 'sequence':item['article']['sequence'],'id':item['id']} for item in result.data()]
            return result # [{'sequence': 0, 'title': 'Intro to eating disorders','id':0},..]

# 获取某个as对应的theme
def getAeticleSetTheme(articleSetTitle):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (:ArticleSet {title:$title})-[:BELONGS_TO]->(t:Theme)
                RETURN t
            """,title=articleSetTitle)

            return result.data()[0]['t']
