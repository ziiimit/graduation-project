import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)

from utils.embeddings import generateEmbedding
from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")



# 创建embedding的索引，便于后续的retrival，只需在索引不存在时运行一次
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


# 创建Article的Proposition, 生成embeddings并存储
def createPropositonForParagraph(videoTitle,articleSequence,paragraphSequence,propositionList):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            for proposition in propositionList:
                # print("proposition:",proposition)
                embedding = generateEmbedding(proposition)
                session.run("""
                    MATCH (:ArticleSet {title_en:$videoTitle})-[:HAS]->(:Article {sequence:$articleSequence})-[:CONSTRUCTED_BY]->(p:Paragraph {sequence:$paragraphSequence})
                    CREATE (prop:Proposition {text:$text})-[:GENERATED_FROM]->(p)
                    WITH prop
                    CALL db.create.setNodeVectorProperty(prop, 'embedding', $vector)
                """, videoTitle=videoTitle, articleSequence=articleSequence, paragraphSequence=paragraphSequence,text=proposition,vector=embedding)
