from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")


def getArticlePropositions(articleTitle):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (:Article {title:$title})-[:CONSTRUCTED_BY]->(:Paragraph)<-[:GENERATED_FROM]-(proposition:Proposition)
                return proposition.content as content,ID(proposition) as id
            """,title=articleTitle)

            return result.data()   #listItem : {'content': 'Individuals may exhibit characteristics of both disorders simultaneously.', 'id': 1}


def setPropositionsEmbedding(propositionsListWithEmbeddings):#listItem : {'content': 'Individuals...', 'id': 1, embedding:[]}

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            for item in propositionsListWithEmbeddings:
                session.run("""
                        MATCH (n:Proposition)
                        WHERE ID(n) = $id
                        CALL db.create.setNodeVectorProperty(n, 'embedding', $vector)
                        SET n.hasEmbedding = True
                    """,id=item['id'], vector=item['embedding'])



def hasEmbedding(propositionListItem):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (n:Proposition)
                WHERE ID(n) = $id
                RETURN n.hasEmbedding as hasEmbedding
            """, id=propositionListItem['id'])

            return result.data()[0]['hasEmbedding']

# hasEmbedding({'content': 'The evolving nature of these disorders requires continuous research and exploration.', 'id': 1986})

def addPropositionVectorIndex():
    
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            session.run("""
                CREATE VECTOR INDEX `proposition-embeddings`
                FOR (n: Proposition) ON (n.embedding)
                OPTIONS {indexConfig: {
                `vector.dimensions`: 1024,
                `vector.similarity_function`: 'cosine'
            }}""")

# addPropositionVectorIndex()
            
# 返回top-num个
def findSimilarPropositions(queryEmbedding, num):
        
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                CALL db.index.vector.queryNodes('proposition-embeddings',$num,$queryEmbedding)
                YIELD node AS similarProposition, score
                RETURN ID(similarProposition) as id, similarProposition.content as content, score
            """, queryEmbedding=queryEmbedding, num=num)

            return result.data()


def getCorrespondingParagraph(propositionID):
        
    with GraphDatabase.driver(URI, auth=AUTH) as driver:

        driver.verify_connectivity()

        with driver.session(database="neo4j") as session:

            result = session.run("""
                MATCH (pro:Proposition)-[:GENERATED_FROM]->(para:Paragraph)
                WHERE ID(pro) = $id
                RETURN ID(para) as id, para.content as content
            """, id=propositionID)
            return result.data()[0]
        


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
 