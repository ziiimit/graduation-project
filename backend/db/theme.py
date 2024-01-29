from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")

# theme是否存在
# def themeExists(themeName):

#     with GraphDatabase.driver(URI, auth=AUTH) as driver:

#         driver.verify_connectivity()

#         with driver.session(database="neo4j") as session:

#             result = session.run("""
#             MATCH (t:Theme {name:$themeName}) 
#             return (t)
#          """, name=themeName)
            
#             return len(result.data()) > 0



            
def getThemeArticleSetTitleList(themeName):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
            MATCH (as:ArticleSet)-[:BELONGS_TO]->(t:Theme {name:$name})
            return as.title as title
         """, name=themeName)
            
            return [item['title'] for item in result]

            

            

