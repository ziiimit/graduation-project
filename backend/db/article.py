from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")



# 查找文章是否存在
def articleExists(article):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:    

            result = session.run("""
                MATCH (a:Article {title:$title})
                RETURN a
            """, title=article["title"])

            return len(result.data()) > 0
        

# 删除文章及其段落
def deleteArticle(article):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session: 

            session.run("""
                MATCH (a:Article {title:$title})-[:CONSTRUCTED_BY]->(p:Paragraph)
                DETACH DELETE (p),(a)
            """,title=article['title'])



# 创建某个ArticleSet下的Article
# article = {title, sequence, paragraphList}
def createArticle(url, article, replace=True):
    
    if articleExists(article) and not replace:
            print("article已经存在")
            return         
    
    if articleExists(article):
        print("删除已存在article")
        deleteArticle(article)

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
 
            session.run("""
                MATCH (v:ArticleSet {url:$url})
                CREATE (a:Article {title:$title, sequence:$sequence})-[:GENERATED_FROM]->(v)   
            """, url=url, title=article["title"], sequence=article["sequence"])

            for index, paragraph in enumerate(article["paragraphList"]) :

                session.run("""
                MATCH (a:Article {title:$title})
                CREATE (a)-[:CONSTRUCTED_BY]->(:Paragraph {sequence:$sequence, content:$content})   
            """, title=article["title"], sequence=index, content=paragraph)


def getParagraphList(articleID):

    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session: 

            result = session.run("""
                MATCH (a:Article)-[CONSTRUCTED_BY]->(p:Paragraph)
                WHERE ID(a) = $id
                RETURN p
                ORDER BY p.sequence
            """,id=articleID)
            return [item['p'] for item in result.data()]


def getAllArticleTitle():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

           articles =  session.run("""
                MATCH (a:Article)
                RETURN a.title as title
            """).data()
           articles = [item['title'] for item in articles]
           return articles
        

# 找某个paragraph对应的Article
def getCorrespondingArticle(paragraphID):
            
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (a:Article)-[:CONSTRUCTED_BY]->(para:Paragraph)
                WHERE ID(para) = $id
                RETURN a.title as title
            """, id=paragraphID)
            return result.data()[0]['title']
        