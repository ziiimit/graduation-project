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



# 创建某个Video下的Article
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
                MATCH (v:Video {url:$url})
                CREATE (a:Article {title:$title, sequence:$sequence})-[:GENERATED_FROM]->(v)   
            """, url=url, title=article["title"], sequence=article["sequence"])

            for index, paragraph in enumerate(article["paragraphList"]) :

                session.run("""
                MATCH (a:Article {title:$title})
                CREATE (a)-[:CONSTRUCTED_BY]->(:Paragraph {sequence:$sequence, content:$content})   
            """, title=article["title"], sequence=index, content=paragraph)



def getParagraphList(articleTitle):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session: 

            result = session.run("""
                MATCH (:Article {title:$title})-[CONSTRUCTED_BY]->(p:Paragraph)
                RETURN p
                ORDER BY p.sequence
            """,title=articleTitle)

            result = [item['p'] for item in result.data()]
            return result
        


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
        


def addPropositionsToParagraph(articleTitle, paragraphSequence,propositionList):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            for proposition in propositionList:
                # print(proposition)
                session.run("""
                    MATCH (:Article {title:$title})-[:CONSTRUCTED_BY]->(p:Paragraph {sequence:$sequence})
                    CREATE (proposition:Proposition {content:$content})-[:GENERATED_FROM]->(p)
                    SET proposition.hasEmbedding = False
                """, title=articleTitle, sequence=paragraphSequence,content=proposition)
            
            session.run("""
                MATCH (:Article {title:$title})-[:CONSTRUCTED_BY]->(p:Paragraph {sequence:$sequence})
                SET p.hasPropositions = True
            """, title=articleTitle, sequence=paragraphSequence)


def hasPropositions(articleTitle, paragraphSequence):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (:Article {title:$title})-[:CONSTRUCTED_BY]->(p:Paragraph {sequence:$sequence})
                RETURN p.hasPropositions as hasPropositions
        """,title=articleTitle,sequence=paragraphSequence)
            
            return result.data()[0]['hasPropositions']
            


# str = '[\n"The existence of anorexia nervosa for centuries points towards a potential hardwiring of this condition into the biology of affected individuals.",\n"Anorexia nervosa has existed for centuries.",\n"The existence of anorexia nervosa suggests that it may be hardwired into the biology of affected individuals.",\n"Being hardwired does not imply an absence of treatment options.",\n"Anorexia nervosa can be addressed and cured with appropriate interventions.",\n"Appropriate interventions can address and cure anorexia nervosa.",\n"Early detection is important in addressing and curing anorexia nervosa.",\n"Comprehensive therapeutic approaches are important in addressing and curing anorexia nervosa." \n]'




# addPropositionsToParagraph("Understanding anorexia nervosa",0,['Anorexia nervosa is commonly known as anorexia.', 'Anorexia nervosa is the most prevalent among all eating disorders.', 'Anorexia nervosa is the most perilous among all eating disorders.', 'Anorexia nervosa surpasses even depression in terms of prevalence.', 'Anorexia nervosa holds the title of the most dangerous psychiatric disorder.', 'The untreated consequences of anorexia can lead to a remarkably high probability of death.', 'The severity of anorexia emphasizes the urgent need for intervention.'])

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
        
# print(getCorrespondingArticle(153))