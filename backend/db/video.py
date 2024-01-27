from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")



# 检查Video所对应的Video是否存在
def videoExists(url):
   
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                    MATCH (v:Video {url:$url}) 
                    return (v)
                """, url=url)
            
            return len(result.data()) > 0


# 创建Video
def createVideo(url, caption):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:
    
            session.run("""
                CREATE (:Video {url:$url, caption:$caption})
            """, caption=caption, url=url)


