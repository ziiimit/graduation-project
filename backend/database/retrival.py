import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)
from utils.embeddings import generateEmbedding
from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")




def getRelevantParagraphList(query_en, relevanceRate, upperLimit):

    queryEmbedding = generateEmbedding(query_en)

    # 过滤函数
    def relevant_enough(n):
        return n['score']>=relevanceRate

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            resp = session.run("""
                CALL db.index.vector.queryNodes('proposition-embeddings',$upperLimit,$queryEmbedding)
                YIELD node AS proposition, score
                MATCH (t:Theme)<-[:BELONGS_TO]-(as:ArticleSet)-[:HAS]->(a:Article)-[:CONSTRUCTED_BY]->(p:Paragraph)<-[:GENERATED_FROM]-(proposition)
                RETURN  a.sequence as articleSequence,a.summary_zh as articleSummary_zh,p.text_en as paragraphText_en, a.title_en as articleTitle_en, a.title_zh as articleTitle_zh, as.title_en as articleSetTitle_en, as.title_zh as articleSetTitle_zh, t.title_en as themeTitle_en, t.title_zh as themeTitle_zh, score
            """, queryEmbedding=queryEmbedding, upperLimit=upperLimit).data()

            return list(filter(relevant_enough, resp))

