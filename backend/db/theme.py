from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")

# theme是否存在
def themeExists(themeName):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
            MATCH (t:Theme {themeName:$themeName}) 
            return (t)
         """, themeName=themeName)
            
            return len(result.data()) > 0


# 创建theme
def createTheme(themeName):

    if themeExists(themeName):
        return

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
            CREATE (:Theme {themeName:$themeName}) 
         """, themeName=themeName)
            
        

