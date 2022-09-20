import marqo

mq = marqo.Client(url='http://localhost:8882')
def run():

    mq.index("firstIndex").add_documents([
        {
            "Title": "The Travels of Marco Polo",
            "Description": "A 13th-century travelogue describing Polo's travels"
        },
        {
            "Title": "Travel the world",
            "Description": "Traveling the world is fun"
        },
        {
            "Title": "Extravehicular Mobility Unit (EMU)",
            "Description": "The EMU is a spacesuit that provides environmental protection, "
                           "mobility, life support, and communications for astronauts",
            "_id": "article_14"
        }]
    )
    #search by query
    queryResults = mq.index("firstIndex").search(q="Who is traveling?")
    #search by title
    carsResult = mq.index("firstIndex").search('Cars', searchable_attributes=['Title'])
    #search by id
    articleResult = mq.index("my-first-index").get_document(document_id="article_14")

    print('carsResult => ', carsResult)
    print('queryResults => ', queryResults)
    print('articleResult => ', articleResult)

if __name__ == '__main__':
    run()

