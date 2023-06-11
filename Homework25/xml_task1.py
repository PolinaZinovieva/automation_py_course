from xml.etree import ElementTree


class XMLManager:
    def to_str(self, collection):
        return ElementTree.tostring(collection, encoding="unicode")

    def str_to_xml(self, string):
        return ElementTree.fromstring(string)

    def find_fav_movies(self, collection):
        for movie in collection.findall("./genre/decade/movie/[@favorite = 'True']"):
            print(movie.attrib)

    def change_xml(self, collection, tree, file):
        mov = collection.find("./genre/decade/movie[@title='THE KARATE KID']")
        mov.attrib["title"] = "The Karate Kid"
        tree.write(file)
        new_tree = ElementTree.parse(file)
        new_collection = new_tree.getroot()
        for movie in new_collection.iter("movie"):
            print(movie.attrib)


action = XMLManager()
tree = ElementTree.parse("file.xml")
collection = tree.getroot()
conversion_to_str = action.to_str(collection)
print(conversion_to_str)
conversion_to_xml = action.str_to_xml(conversion_to_str)
print(conversion_to_xml)
fav_movies = action.find_fav_movies(collection)
print(fav_movies)
change_file = action.change_xml(collection, tree, "file.xml")
