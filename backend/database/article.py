from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
AUTH = ("neo4j","13320113557Hsh")



# 创建Article, 同时插入Paragraph
def createArticle_insertParagraph(videoTitle,sequence,title_en,title_zh,paragraphs):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            session.run("""
                MATCH (as:ArticleSet {title_en:$videoTitle})
                CREATE (as)-[:HAS]->(:Article {title_en:$title_en, title_zh:$title_zh,sequence:$sequence})
            """, videoTitle=videoTitle,title_en = title_en, title_zh = title_zh,sequence=sequence)

            for para in paragraphs:
                session.run("""
                    MATCH (:ArticleSet {title_en:$videoTitle})-[:HAS]->(a:Article {title_en:$title_en})
                    CREATE (a)-[:CONSTRUCTED_BY]->(:Paragraph {sequence:$sequence, text_en:$text_en, text_zh:$text_zh})
                """,videoTitle=videoTitle, title_en=title_en,sequence=para['sequence'],text_en=para['text_en'],text_zh=para['text_zh'])

# 添加summary属性
def insertSummary(videoTitle,articleSequence,summary_en,summary_zh):

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:

            session.run("""
                MATCH (:ArticleSet {title_en:$videoTitle})-[:HAS]->(a:Article {sequence:$articleSequence})
                SET a.summary_en = $summary_en, a.summary_zh = $summary_zh
            """, videoTitle=videoTitle,summary_en = summary_en, summary_zh = summary_zh,articleSequence=articleSequence)

# 获取某个articleSet的article的所有paragraph
def getArticle(articleSetTitle_en,articleSequence):
    articleSequence = int(articleSequence)
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        with driver.session(database="neo4j") as session:
            
            res = session.run("""
                MATCH (:ArticleSet {title_en:$articleSetTitle_en})-[:HAS]->(a:Article {sequence:$articleSequence})-[:CONSTRUCTED_BY]->(p:Paragraph)
                RETURN p.text_zh as text_zh, p.text_en as text_en
                ORDER BY p.sequence
            """, articleSetTitle_en=articleSetTitle_en,articleSequence=articleSequence)
            paragraphs = res.data()
            meta = session.run("""
                MATCH (t:Theme)<-[:BELONGS_TO]-(as:ArticleSet {title_en:$articleSetTitle_en})-[:HAS]->(a:Article {sequence:$articleSequence})
                RETURN t.title_en as themeTitle_en,t.title_zh as themeTitle_zh,  as.title_zh as articleSetTitle_zh, as.title_en as articleSetTitle_en, a.title_zh as articleTitle_zh, a.title_en as articleTitle_en
            """,articleSetTitle_en=articleSetTitle_en,articleSequence=articleSequence).data()

            print(paragraphs)
            return{
                "meta":meta,
                "paragraphs":paragraphs
            }
                
