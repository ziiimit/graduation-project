from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")


# 创建Article, 同时插入Paragraph
def createArticle_insertParagraph(sourceVideoURL,sequence,title_en,title_zh,paragraphs):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            session.run("""
                MATCH (as:ArticleSet {sourceVideoURL:$sourceVideoURL})
                CREATE (as)-[:HAS]->(:Article {title_en:$title_en, title_zh:$title_zh,sequence:$sequence})
            """, sourceVideoURL = sourceVideoURL, title_en = title_en, title_zh = title_zh,sequence=sequence)

            for para in paragraphs:
                session.run("""
                    MATCH (:ArticleSet {sourceVideoURL:$sourceVideoURL})-[:HAS]->(a:Article {title_en:$title_en})
                    CREATE (a)-[:CONSTRUCTED_BY]->(:Paragraph {sequence:$sequence, text_en:$text_en, text_zh:$text_zh})
                """,sourceVideoURL=sourceVideoURL, title_en=title_en,sequence=para['sequence'],text_en=para['text_en'],text_zh=para['text_zh'])


